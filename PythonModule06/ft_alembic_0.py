import elements 


def main() -> None:
    print("=== Alembic 0 ===")
    print("Using: 'import ...' structure to access elements.py")

    fire = elements.create_fire()
    print(f"Testing create_fire: {fire}")


if __name__ == "__main__":
    main()
