from audio.beat_events import BeatEvent, BeatEventDispatcher


def test_register_listener() -> None:
    dispatcher = BeatEventDispatcher()

    def listener(event: BeatEvent) -> None:
        pass

    dispatcher.register(listener)

    assert len(dispatcher._listeners) == 1


def test_dispatch_calls_listener() -> None:
    dispatcher = BeatEventDispatcher()
    received_events = []

    def listener(event: BeatEvent) -> None:
        received_events.append(event)

    dispatcher.register(listener)

    beat_event = BeatEvent(time_seconds=1.25, strength=0.8)
    dispatcher.dispatch(beat_event)

    assert len(received_events) == 1
    assert received_events[0] == beat_event


def test_dispatch_calls_multiple_listeners() -> None:
    dispatcher = BeatEventDispatcher()
    calls = []

    def listener_one(event: BeatEvent) -> None:
        calls.append(("one", event))

    def listener_two(event: BeatEvent) -> None:
        calls.append(("two", event))

    dispatcher.register(listener_one)
    dispatcher.register(listener_two)

    beat_event = BeatEvent(time_seconds=2.0, strength=1.0)
    dispatcher.dispatch(beat_event)

    assert len(calls) == 2
    assert calls[0] == ("one", beat_event)
    assert calls[1] == ("two", beat_event)


def test_dispatch_with_no_listeners_does_nothing() -> None:
    dispatcher = BeatEventDispatcher()
    beat_event = BeatEvent(time_seconds=0.5, strength=1.0)

    dispatcher.dispatch(beat_event)