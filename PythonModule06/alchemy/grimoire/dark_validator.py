from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:

    valid_elements = dark_spell_allowed_ingredients()
    ing_list = ingredients.lower().split()

    for ingredient in ing_list:
        if ingredient in valid_elements:
            return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
