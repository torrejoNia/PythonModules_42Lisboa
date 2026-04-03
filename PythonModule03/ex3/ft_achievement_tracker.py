#!/usr/bin/env python3

"""Achievement tracker using set operations across multiple players."""

import random


ACHIEVEMENT_POOL = [
    "First Steps",
    "Speed Runner",
    "Treasure Hunter",
    "Strategist",
    "Survivor",
    "Crafting Genius",
    "Master Explorer",
    "Collector Supreme",
    "Untouchable",
    "World Savior",
    "Boss Slayer",
    "Unstoppable",
    "Sharp Mind",
    "Hidden Path Finder",
]


def gen_player_achievements() -> set[str]:
    """Generate a random set of achievements for one player."""
    count = random.randint(3, len(ACHIEVEMENT_POOL))
    picks = random.sample(ACHIEVEMENT_POOL, count)
    return set(picks)


print("=== Achievement Tracker System ===\n")

player_names = ["Alice", "Bob", "Charlie", "Dylan"]
player_achievements = {}

for name in player_names:
    player_achievements[name] = gen_player_achievements()
    print(f"Player {name}:", player_achievements[name])

all_achievements = set()
for name in player_names:
    all_achievements = all_achievements.union(player_achievements[name])

common_achievements = player_achievements[player_names[0]]
for name in player_names[1:]:
    common_achievements = common_achievements.intersection(
        player_achievements[name]
    )

print(f"\nAll distinct achievements: {all_achievements}")
print(f"\nCommon achievements: {common_achievements}\n")

for name in player_names:
    others_union = set()
    for other_name in player_names:
        if other_name != name:
            others_union = others_union.union(player_achievements[other_name])
    only_this_player = player_achievements[name].difference(others_union)
    print(f"Only {name} has:", only_this_player)

print()
all_possible = set(ACHIEVEMENT_POOL)
for name in player_names:
    missing = all_possible.difference(player_achievements[name])
    print(f"{name} is missing:", missing)
