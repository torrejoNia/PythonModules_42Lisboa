#!/usr/bin/env python3
"""Test script for the ex1 creature capabilities."""

from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing_factory(factory: HealingCreatureFactory) -> None:
    """Exercise the healing creature family."""
    print("Testing Creature with healing capability")
    base_creature = factory.create_base()
    print("base:")
    print(base_creature.describe())
    print(base_creature.attack())
    print(base_creature.heal())
    evolved_creature = factory.create_evolved()
    print("evolved:")
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    print(evolved_creature.heal())
    print()


def test_transform_factory(factory: TransformCreatureFactory) -> None:
    """Exercise the transforming creature family."""
    print("Testing Creature with transform capability")
    base_creature = factory.create_base()
    print("base:")
    print(base_creature.describe())
    print(base_creature.attack())
    print(base_creature.transform())
    print(base_creature.attack())
    print(base_creature.revert())
    evolved_creature = factory.create_evolved()
    print("evolved:")
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    print(evolved_creature.transform())
    print(evolved_creature.attack())
    print(evolved_creature.revert())


def main() -> None:
    """Run the ex1 scenario."""
    test_healing_factory(HealingCreatureFactory())
    test_transform_factory(TransformCreatureFactory())


if __name__ == "__main__":
    main()
