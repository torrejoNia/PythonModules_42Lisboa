#!/usr/bin/env python3
import alchemy
import alchemy.elements


def sacred_scroll_direct() -> None:
    print()
    print("=== Sacred Scroll Mastery ===\n")

    print("Testing direct module access:")

    fire = alchemy.elements.create_fire()
    print(f'alchemy.elements.create_fire(): {fire}')

    water = alchemy.elements.create_water()
    print(f'alchemy.elements.create_water(): {water}')

    earth = alchemy.elements.create_earth()
    print(f'alchemy.elements.create_earth(): {earth}')

    air = alchemy.elements.create_air()
    print(f'alchemy.elements.create_air(): {air}')


def sacred_scroll_package() -> None:
    print()
    print("Testing package-level access (controlled by __init__.py):")

    fire = alchemy.create_fire()
    print(f"alchemy.create_fire(): {fire}")
    water = alchemy.create_water()
    print(f"alchemy.create_water(): {water}")

    try:
        earth = alchemy.create_earth()
        print(f"alchemy.create_earth(): {earth}")
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")

    try:
        air = alchemy.create_air()
        print(f"alchemy.create_air(): {air}")
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")


if __name__ == "__main__":
    sacred_scroll_direct()
    sacred_scroll_package()

    print()
    print("Package metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")
