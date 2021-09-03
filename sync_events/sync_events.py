import os
import pytz
import glob
import random
import string
from dataclasses import dataclass
from pathlib import Path

import requests
import yaml
import html2text
from slugify import slugify
from dateutil.parser import parse as parse_date
from bs4 import BeautifulSoup


def is_subevent(api_event):
    assert api_event.get("name") is not None  # small sanity check
    return api_event.get("slug") is None


def get_pretix_slug(api_event):
    if is_subevent(api_event):
        return f"{api_event['event']}/{api_event['id']}"
    return api_event["slug"]


def try_scrape_description(pretix_slug):
    try:
        response = requests.get("https://pretix.eu/correlaid/" + pretix_slug)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        description_div = soup.select_one("main h2.content-header").find_next_sibling(
            "div"
        )
        h = html2text.HTML2Text()
        h.ignore_links = True
        return h.handle(str(description_div))
    except Exception as e:
        print(f"ERROR scraping event description ({pretix_slug}): {e}")
        return ""


@dataclass
class EventEn:
    filename: str
    pretix_slug: str
    is_deleted: bool
    is_subevent: bool
    title: str
    event_date: str
    event_time: str
    event_registration: str
    correlaidx: bool
    languages: list[str]
    tags: list[str]
    description: str

    base_dir = "../content/en/events/"
    lang_preference = ["en", "de-informal", "de"]

    def __str__(self):
        return f"{self.title} ({self.event_date}, {self.pretix_slug})"

    @classmethod
    def create(cls, api_event):
        pretix_slug = get_pretix_slug(api_event)
        event = cls(
            filename=cls._create_filename(api_event),
            pretix_slug=pretix_slug,
            is_deleted=False,
            is_subevent=is_subevent(api_event),
            title=cls._parse_title(api_event),
            event_date=cls._parse_date(api_event),
            event_time=cls._parse_time(api_event),
            event_registration="https://pretix.eu/correlaid/" + pretix_slug,
            correlaidx=False,
            languages=cls._parse_languages(api_event),
            tags=[],
            description=cls._parse_description(api_event),
        )

        event.save()
        print(f"[created] {event}")
        return event

    def update(self, api_event):
        self.is_deleted = False
        self.title = self._parse_title(api_event)
        self.event_date = self._parse_date(api_event)
        self.event_time = self._parse_time(api_event)
        self.description = self._parse_description(api_event)
        self.save()
        print(f"[updated] {self}")

    def delete(self):
        self.is_deleted = True
        self.save()
        print(f"[deleted] {self}")

    @classmethod
    def load(cls, filepath):
        filepath = Path(filepath)

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

    @classmethod
    def load_all(cls):
        events = {}
        for path in [p for p in glob.glob(cls.base_dir + "*/*.md")]:
            event = cls.load(path)
            if event is None:
                # not a pretix event
                continue
            events[event.pretix_slug] = event

        return events

    @property
    def filepath(self):
        return Path(self.base_dir) / (f"{self.event_date[:7]}/{self.filename}.md")

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

        self.filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(self.filepath, "w") as f:
            f.write(content)

    @classmethod
    def _parse_title(cls, api_event):
        for lang in cls.lang_preference:
            name = api_event["name"].get(lang)
            if name is not None:
                return name

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
    def _parse_languages(api_event):
        langs = api_event["name"].keys()
        if "en" in langs:
            return ["english"]
        elif "de" in langs or "de-informal" in langs:
            return ["german"]
        else:
            return []

    @classmethod
    def _parse_description(cls, api_event):
        if is_subevent(api_event):
            # for subevents the api_event contains the description
            for lang in cls.lang_preference:
                frontpage_text = api_event["frontpage_text"].get(lang)
                if frontpage_text is not None:
                    return frontpage_text
            return ""
        else:
            # for events the api_event does not contain the description
            # let's try to scrape it
            return try_scrape_description(api_event["slug"])

    @classmethod
    def _create_filename(cls, api_event):
        title = cls._parse_title(api_event)
        filename = slugify(title, max_length=50)
        # filename must be unique (we can have multiple events with same title per month)
        uid = "".join(random.choices(string.ascii_lowercase + string.digits, k=5))
        filename += "--" + uid
        return filename


class EventDe(EventEn):
    base_dir = "../content/de/events/"
    lang_preference = ["de-informal", "de", "en"]


def fetch_api_events(token):
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
        get_pretix_slug(api_event): api_event for api_event in response_json["results"]
    }

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
            **api_events,
            **{
                get_pretix_slug(api_event): api_event
                for api_event in response_json["results"]
            },
        }

    return api_events


def sync_events(Event, api_events):
    events = Event.load_all()

    created, updated, deleted = 0, 0, 0

    # events new on pretix
    for pretix_slug in set(api_events) - set(events):
        Event.create(api_events[pretix_slug])
        created += 1
    # events already on pretix and website
    for pretix_slug in set(api_events).intersection(set(events)):
        events[pretix_slug].update(api_events[pretix_slug])
        updated += 1
    # events deleted on pretix -> delete from website
    for pretix_slug in set(events) - set(api_events):
        events[pretix_slug].delete()
        deleted += 1

    return created, updated, deleted


if __name__ == "__main__":
    with open("../PRETIX_API_TOKEN") as f:
        token = f.readline()

    api_events = fetch_api_events(token)

    for Event in [EventEn, EventDe]:
        sync_events(Event, api_events)
