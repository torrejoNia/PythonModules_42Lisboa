class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")
        return 1

    def get_info(self):
        return f"{self.name}: {self.height}cm"

    def get_type(self):
        return "regular"


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color

    def get_info(self):
        return (
            f"{self.name}: {self.height}cm, "
            f"{self.color} flowers (blooming)"
        )

    def get_type(self):
        return "flowering"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def get_info(self):
        return (
            f"{self.name}: {self.height}cm, "
            f"{self.color} flowers (blooming), "
            f"Prize points: {self.prize_points}"
        )

    def get_type(self):
        return "prize"


class GardenManager:

    total_gardens = 0  # class-level variable

    class GardenStats:
        def __init__(self):
            self.plants_added = 0
            self.total_growth = 0

        def record_add(self):
            self.plants_added += 1

        def record_growth(self, amount):
            self.total_growth += amount

        def summary(self):
            return (
                f"Plants added: {self.plants_added}, "
                f"Total growth: {self.total_growth}cm"
            )

    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.stats = GardenManager.GardenStats()
        GardenManager.total_gardens += 1

    # Instance method
    def add_plant(self, plant):
        self.plants.append(plant)
        self.stats.record_add()
        print(f"Added {plant.name} to {self.owner}'s garden")

    # Instance method
    def help_plants_grow(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            growth = plant.grow()
            self.stats.record_growth(growth)

    # Instance method
    def garden_report(self):
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")

        regular = 0
        flowering = 0
        prize = 0

        for plant in self.plants:
            print(f"- {plant.get_info()}")

            plant_type = plant.get_type()

            if plant_type == "prize":
                prize += 1
            elif plant_type == "flowering":
                flowering += 1
            else:
                regular += 1

        print(self.stats.summary())
        print(
            f"Plant types: {regular} regular, "
            f"{flowering} flowering, {prize} prize flowers"
        )
        print()

    # Class method
    @classmethod
    def create_garden_network(cls, owner_names):
        gardens = []
        for owner in owner_names:
            gardens.append(cls(owner))
        return gardens

    # Static method (utility)
    @staticmethod
    def validate_height(height):
        return height >= 0


# Utility function (still inside system file, not scattered)
def calculate_garden_score(garden):
    total = 0
    for plant in garden.plants:
        total += plant.height
    return total


if __name__ == "__main__":

    print("=== Garden Management System Demo ===")
    print()

    # Create network of gardens
    gardens = GardenManager.create_garden_network(["Alice", "Bob"])
    alice = gardens[0]
    bob = gardens[1]

    # Create plants
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    # Add plants
    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)
    print()

    # Grow plants
    alice.help_plants_grow()
    print()

    # Report
    alice.garden_report()

    print("Height validation test:",
          GardenManager.validate_height(10))

    # Scores
    print(
        f"Garden scores - Alice: {calculate_garden_score(alice)}, "
        f"Bob: {calculate_garden_score(bob)}"
    )

    print("Total gardens managed:",
          GardenManager.total_gardens)
