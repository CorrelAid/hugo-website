import tempfile
from pathlib import Path
import shutil
import random

import pytest

from sync_events import Event


@pytest.fixture
def TestEvent():
    dirpath = tempfile.mkdtemp()

    class E(Event):
        base_dir = dirpath

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

    assert event.filepath == Path(TestEvent.base_dir) / "2021-11/my-nice-event.md"

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


def test_create_update_delete_subevent(TestEvent):
    """
    We can create, update & delete a subevent.
    """
    # an example response from pretix
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
    assert event.languages == []
    assert event.tags == []
    assert (
        event.description
        == "Join our Open Onboarding Call to learn more about the structure..."
    )

    api_subevent["name"]["en"] = "A new name"
    event.update(api_subevent)
    assert event.filename == "open-onboarding-call--e41jr"
    assert event.pretix_slug == "open-onboarding/1234322"
    assert event.title == "A new name"

    event.delete()
    assert event.is_deleted == True
