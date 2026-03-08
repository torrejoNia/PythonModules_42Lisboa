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
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, water: int, sun: int):
        self.name = name
        self.water = water
        self.sun = sun

    def add_water(self, amount):
        self.water += amount

    def info(self):
        print(f"{self.name}: healthy (water: {self.water}, sun: {self.sun})")


class GardenManager:
    def __init__(self, tanksize: int):
        self.plants: list[Plant] = []
        self.tanksize = tanksize
        self.water = tanksize

    def add_plants(self, plants: list[Plant]):
        print(f"{D}\nAdding plants to garden...{X}")
        try:
            for plant in plants:
                if len(plant.name) < 1:
                    raise ValueError("plant name cannot be empty")
                print(f"Added {plant.name} successfully")
                self.plants.append(plant)
        except ValueError as e:
            print(f"{R}Error adding plant: {e.args[0]}{X}")

    def water_plants(self, amount: int):
        print(f"{D}\nWatering plants...{X}")
        print(f"{C}Opening watering system{X}")

        try:
            if len(self.plants) < 1:
                raise GardenError("no plants to water")
            consumption = len(self.plants) * amount
            if consumption == 0:
                raise WaterError("0 water used")
            if consumption > self.water:
                raise WaterError("not enough water in tank")

            self.water -= consumption
            for plant in self.plants:
                plant.add_water(amount)
                print(f"Watering {plant.name} - success")

        except GardenError as e:
            print(f"{R}Error watering plants: {e.args[0]}{X}")
        finally:
            print(f"{B}Closing watering system (cleanup){X}")

    @staticmethod
    def check_plant_health(plant: Plant):
        if plant.water > 10:
            raise PlantError(f"water level {plant.water}"
                             " is too high (max 10)")
        if plant.water < 1:
            raise PlantError(f"water level {plant.water}"
                             " is too low (min 1)")
        if plant.sun > 12:
            raise PlantError(f"sunlight hours {plant.sun}"
                             " is too high (max 12)")
        if plant.sun < 2:
            raise PlantError(f"sunlight hours {plant.sun}"
                             " is too low (min 2)")
        plant.info()

    def check_plants(self):
        print(f"{D}\nChecking plant health...{X}")
        for plant in self.plants:
            try:
                self.check_plant_health(plant)
            except PlantError as e:
                print(f"{R}Error checking {plant.name}: {e.args[0]}{X}")

    def recover(self):
        print(f"{D}\nTesting error recovery...{X}")
        try:
            if self.water < self.tanksize:
                raise WaterError("not enough water in tank")
            print("Water tank OK!")
        except WaterError as e:
            print(f"{R}Caught {type(e).__name__}: {e.args[0]}{X}")
            self.water = self.tanksize
            print("System recovered and continuing")


print("=== Garden Management System ===")

manager = GardenManager(30)
tomato = Plant("tomato", 2, 8)
lettuce = Plant("lettuce", 12, 8)
carrot = Plant("", 0, 8)

manager.add_plants([tomato, lettuce, carrot])
manager.water_plants(0)
manager.check_plants()
manager.recover()

print(f"{G}\nGarden Management system test complete!{X}")
