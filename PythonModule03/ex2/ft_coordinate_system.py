#!/usr/bin/env python3

"""Game Coordinate System - tuple based 3D coordinate processing."""

import math


def get_player_pos() -> tuple[float, float, float]:
    """Read and validate a 3D coordinate tuple in the format x,y,z."""
    while True:
        raw_value = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        parts = []
        current = ""
        for char in raw_value:
            if char == ",":
                parts = parts + [current]
                current = ""
            else:
                current = current + char
        parts = parts + [current]

        try:
            x_text, y_text, z_text = parts
        except ValueError:
            print("Invalid syntax")
            continue

        try:
            x_value = float(x_text)
        except ValueError as error:
            print(f"Error on parameter '{x_text}': {error}")
            continue

        try:
            y_value = float(y_text)
        except ValueError as error:
            print(f"Error on parameter '{y_text}': {error}")
            continue

        try:
            z_value = float(z_text)
        except ValueError as error:
            print(f"Error on parameter '{z_text}': {error}")
            continue
        return (x_value, y_value, z_value)


print("=== Game Coordinate System ===\n")
print("Get a first set of coordinates")
first_pos = get_player_pos()
print("Got a first tuple:", first_pos)
print(f"It includes: X={first_pos[0]}, Y={first_pos[1]}, Z={first_pos[2]}")

distance_to_center = math.sqrt(
    (first_pos[0] ** 2) + (first_pos[1] ** 2) + (first_pos[2] ** 2)
)
print("Distance to center:", round(distance_to_center, 4))

print("\nGet a second set of coordinates")
second_pos = get_player_pos()

distance_between = math.sqrt(
    ((second_pos[0] - first_pos[0]) ** 2)
    + ((second_pos[1] - first_pos[1]) ** 2)
    + ((second_pos[2] - first_pos[2]) ** 2)
)
print(
    "Distance between the 2 sets of coordinates:",
    round(distance_between, 4),
)
