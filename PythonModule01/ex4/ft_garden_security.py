class SecurePlant:
    def __init__(self, name, height, age):
        self.name = name
        self.__height = 0
        self.__age = 0

        print("Plant created:", self.name)

        self.set_height(height)
        self.set_age(age)

    def set_height(self, height):
        if height < 0:
            print()
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            print()
        else:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age):
        if age < 0:
            print()
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
            print()
        else:
            self.__age = age
            print(f"Age updated: {age} days [OK]")

    def get_info(self):
        return f"{self.name} ({self.__height}cm, {self.__age} days)"


if __name__ == "__main__":
    print("=== Garden Security System ===")

    plant = SecurePlant("Rose", 25, 30)

    plant.set_height(-5)

    print("Current plant:", plant.get_info())
