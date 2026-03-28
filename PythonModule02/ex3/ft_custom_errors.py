#!/usr/bin/env python3


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
        print("\nTesting PlantError...")
        test_moisture(0)
    except PlantError as error_message:
        print(f"Caught PlantError: {error_message}")

    try:
        print(f"\nTesting WaterError...")
        test_water(0)
    except WaterError as error_message:
        print(f"Caught WaterError: {error_message}")

    try:
        exceptions: list[Exception] = []
        print("\nTesting all garden errors...")

        try:
            test_moisture(0)
        except PlantError as error_message:
            exceptions = exceptions + [error_message]
        try:
            test_water(0)
        except WaterError as error_message:
            exceptions = exceptions + [error_message]

        raise GardenError(*exceptions)
    except GardenError as error_message:
        for exception in error_message.args:
            print(f"Caught a garden error: {exception}")
    print(f"\nAll custom error types work correctly!")


test_errors()
