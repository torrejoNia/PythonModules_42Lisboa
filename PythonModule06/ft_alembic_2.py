import alchemy.elements


def main() -> None:
    print("=== Alembic 2 ===")
    print("Accessing alchemy/elements.py using"
          " 'import ...' structure")

    earth = alchemy.elements.create_earth()
    print(f"Testing create_earth: {earth}")


if __name__ == "__main__":
    main()
