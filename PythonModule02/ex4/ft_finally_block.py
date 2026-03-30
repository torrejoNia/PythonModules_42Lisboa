#!/usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


def water_plant(plant_name: str) -> None:
    if plant_name != str.capitalize(plant_name):
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print()

    print("Testing valid plants...")
    try:
        print("Opening watering system")
        valid_plants = ["Tomato", "Lettuce", "Carrots"]

        for plant in valid_plants:
            water_plant(plant)

    except PlantError as error_message:
        print(f"Caught PlantError: {error_message}")
        print(".. ending tests and returning to main")

    finally:
        print("Closing watering system")

    print()
    print("Testing invalid plants...")
    try:
        print("Opening watering system")
        invalid_plants = ["Tomato", "lettuce", "carrots"]

        for plant in invalid_plants:
            water_plant(plant)

    except PlantError as error_message:
        print(f"Caught PlantError: {error_message}")
        print(".. ending tests and returning to main")

    finally:
        print("Closing watering system")

    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
