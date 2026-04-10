from alchemy.elements import create_air


def main() -> None:
    print("=== Alembic 3 ===")
    print("Using: 'import ...' structure to access elements.py")

    air = create_air()
    print(f"Testing create_fire: {air}")

if __name__ == "__main__":
    main()
