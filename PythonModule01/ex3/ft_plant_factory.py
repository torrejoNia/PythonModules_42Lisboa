class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        return f"{self.name} ({self.height}cm, {self.age} days)"


if __name__ == "__main__":
    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]

    plants = []
    count = 0

    for i in range(5):
        name, height, age = plant_data[i]
        plant = Plant(name, height, age)
        plants.append(plant)
        count += 1

    print("=== Plant Factory Output ===")

    for i in range(5):
        print(f"Created: {plants[i].get_info()}")

    print()
    print("Total plants created:", count)
