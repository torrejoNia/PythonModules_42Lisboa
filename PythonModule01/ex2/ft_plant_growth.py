class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1

    def age_one_day(self):
        self.age += 1

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)

    plants = [rose]

    print("=== Day 1 ===")
    for i in range(len(plants)):
        print(plants[i].get_info())

    initial_height = rose.height

    # Simulate 6 more days (Day 2 to Day 7)
    for day in range(6):
        for i in range(len(plants)):
            plants[i].grow()
            plants[i].age_one_day()

    print("=== Day 7 ===")
    for i in range(len(plants)):
        print(plants[i].get_info())

    growth = rose.height - initial_height
    print(f"Growth this week: +{growth}cm")
