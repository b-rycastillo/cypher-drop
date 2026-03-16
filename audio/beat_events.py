from dataclasses import dataclass
from typing import Callable, List


@dataclass
class BeatEvent:
    time_seconds: float
    strength: float = 1.0


class BeatEventDispatcher:
    def __init__(self) -> None:
        self._listeners: List[Callable[[BeatEvent], None]] = []

    def register(self, listener: Callable[[BeatEvent], None]) -> None:
        self._listeners.append(listener)

    def dispatch(self, event: BeatEvent) -> None:
        for listener in self._listeners:
            listener(event)


def print_beat_listener(event: BeatEvent) -> None:
    print(
        f"[EVENT] Beat detected at {event.time_seconds:.2f}s "
        f"| strength={event.strength:.2f}"
    )


if __name__ == "__main__":
    dispatcher = BeatEventDispatcher()
    dispatcher.register(print_beat_listener)

    sample_events = [
        BeatEvent(time_seconds=0.50),
        BeatEvent(time_seconds=1.00),
        BeatEvent(time_seconds=1.50),
    ]

    for event in sample_events:
        dispatcher.dispatch(event)