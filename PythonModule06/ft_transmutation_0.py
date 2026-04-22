import alchemy.transmutation.recipes


def main() -> None:
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")

    lead_to_gold = alchemy.transmutation.recipes.lead_to_gold()
    print(f"Testing lead to gold: {lead_to_gold}")


if __name__ == "__main__":
    main()
