import alchemy


def main() -> None:
    print("=== Transmutation 2 ===")
    print("Import alchemy module only")

    lead_to_gold = alchemy.lead_to_gold()
    print(f"Testing lead to gold: {lead_to_gold}")


if __name__ == "__main__":
    main()
