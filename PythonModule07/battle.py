#!/usr/bin/env python3
"""Battle script for testing the ex0 creature factory system."""

from ex0 import AquaFactory, FlameFactory
from ex0.creatures import CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    """Test a creature factory by creating and
    testing base and evolved creatures."""
    print("Testing factory")
    base_creature = factory.create_base()
    print(base_creature.describe())
    print(base_creature.attack())
    evolved_creature = factory.create_evolved()
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    print()


def battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    """Simulate a battle between two base creatures
    from different factories."""
    print("Testing battle")
    creature1 = factory1.create_base()
    creature2 = factory2.create_base()
    print(creature1.describe())
    print("vs.")
    print(creature2.describe())
    print("fight!")
    print(creature1.attack())
    print(creature2.attack())


def main() -> None:
    """Run the battle tests."""
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    test_factory(flame_factory)
    test_factory(aqua_factory)
    battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
