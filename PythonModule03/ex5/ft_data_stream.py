#!/usr/bin/env python3

"""Game data stream processor using generators."""

import random
from typing import Generator


PLAYERS = ["bob", "alice", "charlie", "dylan"]
ACTIONS = [
    "run",
    "eat",
    "sleep",
    "grab",
    "move",
    "climb",
    "swim",
    "release",
    "use",
]


def gen_event() -> Generator[tuple[str, str], None, None]:
    """Generate an endless stream of random player actions."""
    while True:
        name = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (name, action)


def consume_event(
    event_list: list[tuple[str, str]],
) -> Generator[tuple[str, str], None, None]:
    """Yield and remove random events from a list until it is empty."""
    while len(event_list) > 0:
        index = random.randrange(len(event_list))
        event = event_list[index]
        del event_list[index]
        yield event


print("=== Game Data Stream Processor ===")

event_generator = gen_event()

for event_index in range(1000):
    name, action = next(event_generator)
    print(f"Event {event_index}: Player {name} did action {action}")

event_list = []
event_generator = gen_event()

for _ in range(10):
    event_list = event_list + [next(event_generator)]

print("Built list of 10 events:", event_list)

for event in consume_event(event_list):
    print("Got event from list:", event)
    print("Remains in list:", event_list)
