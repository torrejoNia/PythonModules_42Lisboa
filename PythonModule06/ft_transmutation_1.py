import alchemy.transmutation


def main() -> None:
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")

    lead_to_gold = alchemy.transmutation.lead_to_gold()
    print(f"Testing lead to gold: {lead_to_gold}")


if __name__ == "__main__":
    main()
