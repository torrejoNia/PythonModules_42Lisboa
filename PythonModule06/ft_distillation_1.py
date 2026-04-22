import alchemy


def main() -> None:
    print("=== Distillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")

    healing = alchemy.heal()
    strength = alchemy.strength_potion()
    print(f"Testing strength_potion: {strength}")
    print(f"Testing healing_potion: {healing}")


if __name__ == "__main__":
    main()
