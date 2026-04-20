from alchemy.potions import healing_potion, strength_potion

def main() -> None:
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")

    healing = healing_potion()
    strength = strength_potion()
    print(f"Testing strength_potion: {strength}")
    print(f"Testing healing_potion: {healing}")


if __name__ == "__main__":
    main()
