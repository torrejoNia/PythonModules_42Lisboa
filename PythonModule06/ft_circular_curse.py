from alchemy.grimoire import validate_ingredients, record_spell


def method() -> None:

    print()
    print("=== Circular Curse Breaking ===\n")

    ing1 = "fire air"
    ing2 = "dragon scales"
    ing3 = "shadow"
    ing4 = "air"

    spell1 = "Fireball"
    spell2 = "Dark Magic"
    spell3 = "Lightning"

    print("Testing ingredient validation:")
    print(f'validate_ingredients("{ing1}"): {validate_ingredients(ing1)}')
    print(f'validate_ingredients("{ing2}"): {validate_ingredients(ing2)}')

    print("Testing spell recording with validation:")
    print(f'record_spell("{spell1}", "{ing1}): {record_spell(spell1, ing1)}')
    print(f'record_spell("{spell2}", "{ing3}): {record_spell(spell2, ing3)}')

    print("Testing late import technique:")
    print(f'record_spell("{spell3}", "{ing4}"): {record_spell(spell3, ing4)}')


if __name__ == "__main__":
    method()
    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")
