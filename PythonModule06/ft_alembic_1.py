from elements import create_water


def main() -> None:
    print("=== Alembic 1 ===")
    print("Using: 'import ...' structure to access elements.py")

    water = create_water()
    print(f"Testing create_fire: {water}")

if __name__ == "__main__":
    main()
