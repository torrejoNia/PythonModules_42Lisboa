#!/usr/bin/env python3


def check_plant_health(plant_name, water_level, sunlight_hours):
    if len(plant_name) < 1:
        raise ValueError("Error: plant name can't be empty!")
    if water_level > 10:
        raise ValueError(f"Error: water level {water_level}"
                         f" is too high (max 10)")
    if water_level < 1:
        raise ValueError(f"Error: water level {water_level}"
                         f" is too low (min 1)")
    if sunlight_hours > 12:
        raise ValueError(f"Error: sunlight hours {sunlight_hours}"
                         f" is too high (max 12)")
    if sunlight_hours < 2:
        raise ValueError(f"Error: sunlight hours {sunlight_hours}"
                         f" is too low (min 2)")
    print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks():
    try:
        print("\nTesting good values...")
        check_plant_health("tomato", 5, 6)
    except ValueError as error_message:
        print(error_message.args[0])
    try:
        print(f"\nTesting empty plant name...")
        check_plant_health("", 5, 6)
    except ValueError as error_message:
        print(error_message.args[0])
    try:
        print(f"\nTesting bad water level...")
        check_plant_health("tomato", 15, 6)
    except ValueError as error_message:
        print(error_message.args[0])
    try:
        print(f"\nTesting bad sunlight hours...")
        check_plant_health("tomato", 5, 0)
    except ValueError as error_message:
        print(error_message.args[0])


test_plant_checks()
