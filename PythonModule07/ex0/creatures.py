"""
Abstract factory pattern implementation for creature cards.

This module defines the Creature hierarchy and the CreatureFactory pattern
for creating base and evolved creatures from different families.
"""

from abc import ABC, abstractmethod


class Creature(ABC):
    """Abstract base class for all creatures."""

    def __init__(self, name: str, creature_type: str) -> None:
        """
        Initialize a creature with a name and type.

        Args:
            name: The name of the creature.
            creature_type: The type/family of the creature.
        """
        self.name = name
        self.creature_type = creature_type

    @abstractmethod
    def attack(self) -> str:
        """
        Return the attack action of the creature.

        Returns:
            A string describing the creature's attack.
        """
        pass

    def describe(self) -> str:
        """
        Return a standard description of the creature.

        Returns:
            A string describing the creature's name and type.
        """
        return f"{self.name} is a {self.creature_type} type Creature"


class Flameling(Creature):
    """Fire-type base creature from the Flame family."""

    def __init__(self) -> None:
        """Initialize Flameling."""
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        """Return Flameling's attack action."""
        return "Flameling uses Ember!"


class Pyrodon(Creature):
    """Fire/Flying-type evolved creature from the Flame family."""

    def __init__(self) -> None:
        """Initialize Pyrodon."""
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        """Return Pyrodon's attack action."""
        return "Pyrodon uses Flamethrower!"


class Aquabub(Creature):
    """Water-type base creature from the Aqua family."""

    def __init__(self) -> None:
        """Initialize Aquabub."""
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        """Return Aquabub's attack action."""
        return "Aquabub uses Water Gun!"


class Torragon(Creature):
    """Water-type evolved creature from the Aqua family."""

    def __init__(self) -> None:
        """Initialize Torragon."""
        super().__init__("Torragon", "Water")

    def attack(self) -> str:
        """Return Torragon's attack action."""
        return "Torragon uses Hydro Pump!"


class CreatureFactory(ABC):
    """Abstract factory for creating creatures."""

    @abstractmethod
    def create_base(self) -> Creature:
        """
        Create a base creature.

        Returns:
            A base Creature instance.
        """
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        """
        Create an evolved creature.

        Returns:
            An evolved Creature instance.
        """
        pass


class FlameFactory(CreatureFactory):
    """Factory for creating Fire-type creatures."""

    def create_base(self) -> Creature:
        """
        Create a base Fire-type creature.

        Returns:
            A Flameling instance.
        """
        return Flameling()

    def create_evolved(self) -> Creature:
        """
        Create an evolved Fire-type creature.

        Returns:
            A Pyrodon instance.
        """
        return Pyrodon()


class AquaFactory(CreatureFactory):
    """Factory for creating Water-type creatures."""

    def create_base(self) -> Creature:
        """
        Create a base Water-type creature.

        Returns:
            An Aquabub instance.
        """
        return Aquabub()

    def create_evolved(self) -> Creature:
        """
        Create an evolved Water-type creature.

        Returns:
            A Torragon instance.
        """
        return Torragon()
