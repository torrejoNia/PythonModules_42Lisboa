"""Creature factories and concrete creatures for ex1."""

from abc import ABC, abstractmethod

from .capabilities import HealCapability, TransformCapability


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


class Sproutling(Creature, HealCapability):
    """Base healing creature."""

    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self) -> str:
        return "Sproutling heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    """Evolved healing creature."""

    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def heal(self) -> str:
        return "Bloomelle heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    """Base transforming creature."""

    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")
        self._transformed = False

    def attack(self) -> str:
        if self._transformed:
            return "Shiftling performs a boosted strike!"
        return "Shiftling attacks normally."

    def transform(self) -> str:
        self._transformed = True
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        self._transformed = False
        return "Shiftling returns to normal."


class Morphagon(Creature, TransformCapability):
    """Evolved transforming creature."""

    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")
        self._transformed = False

    def attack(self) -> str:
        if self._transformed:
            return "Morphagon unleashes a devastating morph strike!"
        return "Morphagon attacks normally."

    def transform(self) -> str:
        self._transformed = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        self._transformed = False
        return "Morphagon stabilizes its form."


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


class HealingCreatureFactory(CreatureFactory):
    """Factory for the healing creature family."""

    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    """Factory for the transforming creature family."""

    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
