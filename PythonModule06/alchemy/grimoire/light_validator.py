def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    valid_elements = light_spell_allowed_ingredients()
    ing_list = ingredients.lower().split()

    for ingredient in ing_list:
        if ingredient in valid_elements:
            return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
