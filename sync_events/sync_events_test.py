import tempfile
from pathlib import Path
import shutil

import pytest

from sync_events import Event


@pytest.fixture
def TestEvent():
    dirpath = tempfile.mkdtemp()

    class E(Event):
        base_dir = dirpath

    yield E

    shutil.rmtree(dirpath)


def test_event_save_load(TestEvent):
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
