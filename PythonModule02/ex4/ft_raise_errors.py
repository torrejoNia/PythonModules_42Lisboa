#!/usr/bin/env python3


X = "\033[0m"
R = "\033[91m"
G = "\033[92m"
B = "\033[94m"
C = "\033[96m"
M = "\033[95m"
Y = "\033[93m"
D = "\033[2m"


def check_plant_health(plant_name, water_level, sunlight_hours):
    if len(plant_name) < 1:
        raise ValueError(f"{R}Error: plant name can't be empty!{X}")
    if water_level > 10:
        raise ValueError(f"{R}Error: water level {water_level}"
                         f" is too high (max 10){X}")
    if water_level < 1:
        raise ValueError(f"{R}Error: water level {water_level}"
                         f" is too low (min 1){X}")
    if sunlight_hours > 12:
        raise ValueError(f"{R}Error: sunlight hours {sunlight_hours}"
                         f" is too high (max 12){X}")
    if sunlight_hours < 2:
        raise ValueError(f"{R}Error: sunlight hours {sunlight_hours}"
                         f" is too low (min 2){X}")
    print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks():
    try:
        print(f"{D}\nTesting good values...{X}")
        check_plant_health("tomato", 5, 6)
    except ValueError as e:
        print(e.args[0])
    try:
        print(f"{D}\nTesting empty plant name...{X}")
        check_plant_health("", 5, 6)
    except ValueError as e:
        print(e.args[0])
    try:
        print(f"{D}\nTesting bad water level...{X}")
        check_plant_health("tomato", 15, 6)
    except ValueError as e:
        print(e.args[0])
    try:
        print(f"{D}\nTesting bad sunlight hours...{X}")
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(e.args[0])


test_plant_checks()
