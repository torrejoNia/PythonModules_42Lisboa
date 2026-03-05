class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age_in_days = age

    def grow(self):
        self.height += 1

    def age(self):
        self.age_in_days += 1

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age_in_days} days old"


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)

    plants = [rose]

    print("=== Day 1 ===")
    for i in range(1):
        print(plants[i].get_info())

    initial_height = rose.height

    for day in range(6):
        for i in range(1):
            plants[i].grow()
            plants[i].age()

    print("=== Day 7 ===")
    for i in range(1):
        print(plants[i].get_info())

    growth = rose.height - initial_height
    print(f"Growth this week: +{growth}cm")
