#!/usr/bin/env python3


X = "\033[0m"
R = "\033[91m"
G = "\033[92m"
B = "\033[94m"
C = "\033[96m"
M = "\033[95m"
Y = "\033[93m"
D = "\033[2m"


def water_plants(plant_list: list[str]):
    print(f"{C}Opening watering system{X}")
    try:
        for plant in plant_list:
            print("Watering " + plant)
    except TypeError:
        print(f"{R}Error: can't water {plant} - invalid plant!{X}")
    finally:
        print(f"{B}Closing watering system{X}")


def test_watering_system():
    print(f"{D}\nTesting normal watering...\n{X}")
    water_plants(["tomato", "lettuce", "carrots"])
    print(f"{D}\nTesting with error...\n{X}")
    water_plants(["tomato", None, "carrots"])


test_watering_system()
