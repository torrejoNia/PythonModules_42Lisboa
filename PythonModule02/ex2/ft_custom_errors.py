#!/usr/bin/env python3


X = "\033[0m"
R = "\033[91m"
G = "\033[92m"
B = "\033[94m"
C = "\033[96m"
M = "\033[95m"
Y = "\033[93m"
D = "\033[2m"


class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __str__(self):
        return "The tomato plant is wilting!"


class WaterError(GardenError):
    def __str__(self):
        return "Not enough water in the tank!"


def test_moisture(moisture):
    if moisture < 1:
        raise PlantError()
    print("Plant OK!")


def test_water(water):
    if water < 1:
        raise WaterError()
    print("Water OK!")


def test_errors():
    try:
        print(f"{D}\nTesting PlantError...{X}")
        test_moisture(0)
    except PlantError as e:
        print(f"{R}Caught PlantError: {str(e)}{X}")

    try:
        print(f"{D}\nTesting WaterError...{X}")
        test_water(0)
    except WaterError as e:
        print(f"{R}Caught WaterError: {str(e)}{X}")

    try:
        exceptions: list[Exception] = []
        print(f"\n{D}Testing all garden errors...{X}")

        try:
            test_moisture(0)
        except PlantError as e:
            exceptions.append(e)
        try:
            test_water(0)
        except WaterError as e:
            exceptions.append(e)

        if len(exceptions) > 0:
            raise GardenError(*exceptions)
    except GardenError as e:
        for exception in e.args:
            print(f"{R}Caught a garden error: {str(exception)}{X}")
    print(f"{G}\nAll custom error types work correctly!{X}")


test_errors()
