import tempfile
from pathlib import Path
import shutil
import random
from unittest import mock
from collections import namedtuple

import pytest

from sync_events import EventEn, try_scrape_description


@pytest.fixture
def TestEvent():
    dirpath = tempfile.mkdtemp()

    class E(EventEn):
        base_dir = dirpath + "/"

    yield E

    shutil.rmtree(dirpath)


def test_save_load(TestEvent):
    """
    We can save an event and then load it. We should get the same data back.
    """
    event = TestEvent(
        filename="my-nice-event",
        pretix_slug="abcde",
        is_deleted=False,
        is_subevent=False,
        title="My nice event",
        event_date="2021-11-12",
        event_time="7:00 - 8:00 CET",
        event_registration="https://pretix.eu/correlaid/abcde/ ",
        correlaidx=False,
        languages=["english"],
        tags=[],
        description="This will be a very nice event",
    )
    event.save()

    expected_filepath = Path(TestEvent.base_dir) / "2021-11/my-nice-event.md"
    assert expected_filepath.exists()
    assert event.filepath == expected_filepath

    loaded_event = TestEvent.load(event.filepath)

    assert loaded_event.filename == event.filename
    assert loaded_event.pretix_slug == event.pretix_slug
    assert loaded_event.is_deleted == event.is_deleted
    assert loaded_event.is_subevent == event.is_subevent
    assert loaded_event.title == event.title
    assert loaded_event.event_date == event.event_date
    assert loaded_event.event_time == event.event_time
    assert loaded_event.event_registration == event.event_registration
    assert loaded_event.correlaidx == event.correlaidx
    assert loaded_event.languages == event.languages
    assert loaded_event.tags == event.tags
    assert loaded_event.description == event.description


def test_load_all(TestEvent):
    event_1 = TestEvent(
        filename="my-nice-event",
        pretix_slug="abcde",
        is_deleted=False,
        is_subevent=False,
        title="My nice event",
        event_date="2021-11-12",
        event_time="7:00 - 8:00 CET",
        event_registration="https://pretix.eu/correlaid/abcde/ ",
        correlaidx=False,
        languages=["english"],
        tags=[],
        description="This will be a very nice event",
    )
    event_1.save()
    expected_filepath = Path(TestEvent.base_dir) / "2021-11/my-nice-event.md"
    assert expected_filepath.exists()

    event_2 = TestEvent(
        filename="my-nice-event-2",
        pretix_slug="fghij",
        is_deleted=False,
        is_subevent=False,
        title="My nice event 2",
        event_date="2021-12-12",
        event_time="7:00 - 8:00 CET",
        event_registration="https://pretix.eu/correlaid/fghij/ ",
        correlaidx=False,
        languages=["english"],
        tags=[],
        description="This will be a very nice event 2",
    )
    event_2.save()
    expected_filepath = Path(TestEvent.base_dir) / "2021-12/my-nice-event-2.md"
    assert expected_filepath.exists()

    events = TestEvent.load_all()

    assert len(events) == 2
    assert events["abcde"].title == "My nice event"
    assert events["fghij"].title == "My nice event 2"


def test_create_update_delete_subevent(TestEvent):
    """
    We can create, update & delete a subevent.
    """
    # an example subevent from pretix
    api_subevent = {
        "id": 1234322,
        "name": {"en": "Open Onboarding Call"},
        "date_from": "2021-10-04T19:00:00+02:00",
        "date_to": "2021-10-04T20:00:00+02:00",
        "active": True,
        "date_admission": None,
        "presale_start": None,
        "presale_end": None,
        "location": {"en": "Online - Zoom"},
        "geo_lat": None,
        "geo_lon": None,
        "event": "open-onboarding",
        "is_public": True,
        "frontpage_text": {
            "en": "Join our Open Onboarding Call to learn more about the structure..."
        },
        "seating_plan": None,
        "item_price_overrides": [],
        "variation_price_overrides": [],
        "meta_data": {},
        "seat_category_mapping": {},
        "last_modified": "2021-04-29T10:47:01.307952+02:00",
    }

    random.seed(1)

    event = TestEvent.create(api_subevent)
    assert event.filename == "open-onboarding-call--e41jr"
    assert event.pretix_slug == "open-onboarding/1234322"
    assert event.is_deleted == False
    assert event.is_subevent == True
    assert event.title == "Open Onboarding Call"
    assert event.event_date == "2021-10-04"
    assert event.event_time == "19:00 - 20:00 CET"
    assert (
        event.event_registration
        == "https://pretix.eu/correlaid/open-onboarding/1234322"
    )
    assert event.correlaidx == False
    assert event.languages == ["english"]
    assert event.tags == []
    assert (
        event.description
        == "Join our Open Onboarding Call to learn more about the structure..."
    )
    expected_filepath = (
        Path(TestEvent.base_dir) / "2021-10/open-onboarding-call--e41jr.md"
    )
    assert expected_filepath.exists()

    api_subevent["name"]["en"] = "A new name"
    event.update(api_subevent)
    assert event.filename == "open-onboarding-call--e41jr"
    assert event.pretix_slug == "open-onboarding/1234322"
    assert event.title == "A new name"
    assert expected_filepath.exists()

    event.delete()
    assert event.is_deleted == True
    assert expected_filepath.exists()


@mock.patch("requests.get")
def test_try_scrape_description(mock_requests_get):
    with open("./jena-workshop.html") as f:
        pretix_event_html = f.read()

    mock_requests_get.return_value = mock.Mock(text=pretix_event_html)

    description = try_scrape_description("jena-workshop")
    assert description.startswith(
        "I don’t need to know everything, I just need to know where to"
    )
