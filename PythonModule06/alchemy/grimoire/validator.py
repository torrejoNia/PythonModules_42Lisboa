def validate_ingredients(ingredients: str) -> str:
    valid_elements = ["fire", "water", "earth", "air"]
    ing = ingredients.split()
    for ingredient in ing:
        if ingredient not in valid_elements:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
