import alchemy.elements


def main() -> None:
    print("=== Alembic 2 ===")
    print("Using: 'import ...' structure to access elements.py")

    earth = alchemy.elements.create_earth()
    print(f"Testing create_fire: {earth}")


if __name__ == "__main__":
    main()
