import os
import pytz
import glob
from dataclasses import dataclass
from pathlib import Path
from typing import List


import requests
import yaml
from slugify import slugify
from dateutil.parser import parse as parse_date


@dataclass
class Event:
    filename: str
    pretix_slug: str
    is_deleted: bool
    is_subevent: bool
    title: str
    event_date: str
    event_time: str
    event_registration: str
    correlaidx: bool
    languages: List[str]
    tags: List[str]
    description: str

    @classmethod
    def create(cls, api_event):
        is_subevent = api_event.get("slug") is None
        pretix_slug = cls._create_slug(api_event, is_subevent)

        event = cls(
            filename=slugify(cls._parse_title(api_event), max_length=50),
            pretix_slug=pretix_slug,
            is_deleted=False,
            is_subevent=is_subevent,
            title=cls._parse_title(api_event),
            event_date=cls._parse_date(api_event),
            event_time=cls._parse_time(api_event),
            event_registration="https://pretix.eu/correlaid/" + pretix_slug,
            correlaidx=False,
            languages=[],
            tags=[],
            description=cls._parse_description(api_event),
        )

        event.save()
        return event

    def update(self, api_event):
        self.is_deleted = False
        self.title = self._parse_title(api_event)
        self.event_date = self._parse_date(api_event)
        self.event_time = self._parse_time(api_event)
        self.description = self._parse_description(api_event)
        self.save()

    def delete(self):
        self.is_deleted = True
        self.save()

    @classmethod
    def load(cls, filepath):
        with open(filepath) as f:
            contents = f.read()
            _, contents = contents.split("---", 1)
            front_matter, description = contents.split("---", 1)

        front_matter = yaml.load(front_matter, Loader=yaml.FullLoader)
        description = description.strip()

        if front_matter.get("pretixSlug") is None:
            # not a pretix event
            return None

        filename = filepath.name[: -len(filepath.suffix)]

        return cls(
            filename=filename,
            pretix_slug=front_matter["pretixSlug"],
            is_deleted=front_matter["isDeleted"],
            is_subevent=front_matter["isSubevent"],
            title=front_matter["title"],
            event_date=front_matter["eventDate"],
            event_time=front_matter["eventTime"],
            event_registration=front_matter["eventRegistration"],
            correlaidx=front_matter["correlaidx"],
            languages=front_matter["languages"],
            tags=front_matter["tags"],
            description=description,
        )

    def save(self):
        front_matter = yaml.dump(
            {
                "pretixSlug": self.pretix_slug,
                "isDeleted": self.is_deleted,
                "isSubevent": self.is_subevent,
                "title": self.title,
                "eventDate": self.event_date,
                "eventTime": self.event_time,
                "eventRegistration": self.event_registration,
                "correlaidx": self.correlaidx,
                "languages": self.languages,
                "tags": self.tags,
            },
            sort_keys=False,
        )

        content = f"---\n{front_matter}---\n\n{self.description}"

        filepath = Path(f"content/en/events/{self.event_date[:7]}/{self.filename}.md")
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, "w") as f:
            f.write(content)

    @staticmethod
    def _parse_title(api_event):
        # TODO langs
        return (
            api_event["name"].get("en")
            or api_event["name"].get("de")
            or api_event["name"].get("de-informal")
        )

    @staticmethod
    def _parse_date(api_event):
        date_from = parse_date(api_event["date_from"]).astimezone(pytz.timezone("CET"))
        return str(date_from.date())

    @staticmethod
    def _parse_time(api_event):
        date_from = parse_date(api_event["date_from"]).astimezone(pytz.timezone("CET"))
        if api_event.get("date_to") is None:
            return f"{date_from.strftime('%H:%M')} CET"
        date_to = parse_date(api_event["date_to"]).astimezone(pytz.timezone("CET"))
        return f"{date_from.strftime('%H:%M')} - {date_to.strftime('%H:%M')} CET"

    @staticmethod
    def _parse_description(api_event, lang="en"):
        # get html and create bs object
        description_dict = api_event.get("frontpage_text")
        description = description_dict[lang]
        return description

    @staticmethod
    def _create_slug(api_event, is_subevent):
        if not is_subevent:
            # event
            pretix_slug = api_event["slug"]
        else:
            # subevent
            pretix_slug = f"{api_event['event']}/{api_event['id']}"
        return pretix_slug


def load_events():
    events = {}
    for path in [Path(p) for p in glob.glob("content/en/events/*/*.md")]:
        event = Event.load(path)
        if event is None:
            # not a pretix event
            continue
        events[event.pretix_slug] = event

    return events


if __name__ == "__main__":
    # load events from file tree
    events = load_events()

    with open("PRETIX_API_TOKEN") as f:
        token = f.readline()

    # events from pretix
    response = requests.get(
        "https://pretix.eu/api/v1/organizers/correlaid/events/"
        "?is_future=true&has_subevents=false&is_public=true&live=true",
        headers={"Authorization": f"Token {token}"},
    )
    response.raise_for_status()

    response_json = response.json()
    if response_json["next"] is not None:
        raise Exception("pagination not implemented")

    api_events = {
        api_event["slug"]: api_event for api_event in response_json["results"]
    }

    # what does that do?
    # events new on pretix
    for pretix_slug in set(api_events) - set(events):
        Event.create(api_events[pretix_slug])
    # events already on pretix and website
    for pretix_slug in set(api_events).intersection(set(events)):
        events[pretix_slug].update(api_events[pretix_slug])
    # events deleted on pretix -> delete from website
    for pretix_slug in set(events) - set(api_events):
        events[pretix_slug].delete()

    # subevents
    response = requests.get(
        "https://pretix.eu/api/v1/organizers/correlaid/events/"
        "?has_subevents=true&is_public=true&live=true",
        headers={"Authorization": f"Token {token}"},
    )
    response.raise_for_status()

    response_json = response.json()
    if response_json["next"] is not None:
        raise Exception("pagination not implemented")

    for slug in [
        api_event["slug"]
        for api_event in response_json["results"]
        if api_event["has_subevents"]
    ]:
        # get subevents
        response = requests.get(
            f"https://pretix.eu/api/v1/organizers/correlaid/events/{slug}/subevents/"
            "?is_future=true&active=true",
            headers={"Authorization": f"Token {token}"},
        )
        response.raise_for_status()

        response_json = response.json()
        if response_json["next"] is not None:
            raise Exception("pagination not implemented")

        api_events = {
            f"{api_event['event']}/{api_event['id']}": api_event
            for api_event in response_json["results"]
        }
        for pretix_slug in set(api_events) - set(events):
            Event.create(api_events[pretix_slug])
        for pretix_slug in set(api_events).intersection(set(events)):
            events[pretix_slug].update(api_events[pretix_slug])
        for pretix_slug in set(events) - set(api_events):
            events[pretix_slug].delete()
    print(events)
