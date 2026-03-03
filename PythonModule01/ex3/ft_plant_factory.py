class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        return f"{self.name} ({self.height}cm, {self.age} days)"


if __name__ == "__main__":
    # Streamlined creation
    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]

    plants = []

    # Create plants
    for i in range(len(plant_data)):
        name, height, age = plant_data[i]
        plant = Plant(name, height, age)
        plants.append(plant)

    print("=== Plant Factory Output ===")

    for i in range(len(plants)):
        print(f"Created: {plants[i].get_info()}")

    print("Total plants created:", len(plants))
