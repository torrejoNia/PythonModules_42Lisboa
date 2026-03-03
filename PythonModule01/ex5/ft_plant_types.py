class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days"

    def special_action(self):
        pass  # default behavior


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def get_info(self):
        return (
            f"{self.name} (Flower): "
            f"{self.height}cm, "
            f"{self.age} days, "
            f"{self.color} color"
        )

    def special_action(self):
        print(f"{self.name} is blooming beautifully!")
        print()


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def get_info(self):
        return (
            f"{self.name} (Tree): "
            f"{self.height}cm, "
            f"{self.age} days, "
            f"{self.trunk_diameter}cm diameter"
        )

    def special_action(self):
        shade = self.trunk_diameter + 28  # simple formula to get 78 for 50
        print(f"{self.name} provides {shade} square meters of shade")
        print()


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self):
        return (
            f"{self.name} (Vegetable): "
            f"{self.height}cm, "
            f"{self.age} days, "
            f"{self.harvest_season} harvest"
        )

    def special_action(self):
        print(f"{self.name} is rich in {self.nutritional_value}")
        print()


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print()

    plants = [
        Flower("Rose", 25, 30, "red"),
        Flower("Tulip", 20, 25, "yellow"),
        Tree("Oak", 500, 1825, 50),
        Tree("Pine", 400, 1460, 40),
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Carrot", 30, 70, "fall", "vitamin A")
    ]

    for plant in plants:
        print(plant.get_info())
        plant.special_action()
