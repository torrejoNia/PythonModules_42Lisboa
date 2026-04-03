#!/usr/bin/env python3

"""Game Data Alchemist - comprehensions for collections."""

import random


print("=== Game Data Alchemist ===\n")

players = [
    "Alice",
    "bob",
    "Charlie",
    "dylan",
    "Emma",
    "Gregory",
    "john",
    "kevin",
    "Liam",
]
print("Initial list of players:", players)

player_names = {
    "Alice": "Alice",
    "bob": "Bob",
    "Charlie": "Charlie",
    "dylan": "Dylan",
    "Emma": "Emma",
    "Gregory": "Gregory",
    "john": "John",
    "kevin": "Kevin",
    "Liam": "Liam",
}

all_capitalized = [player_names[name] for name in players]
print("New list with all names capitalized:", all_capitalized)

capitalized_only = [name for name in players if player_names[name] == name]
print("New list of capitalized names only:", capitalized_only)

score_dict = {name: random.randint(0, 1000) for name in all_capitalized}
print("\nScore dict:", score_dict)

score_average = round(
    sum(score_dict[name] for name in score_dict) / len(score_dict),
    2,
)
print("Score average is", score_average)

high_scores = {
    name: score_dict[name]
    for name in score_dict
    if score_dict[name] > score_average
}
print("High scores:", high_scores)
