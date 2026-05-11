from abc import ABC, abstractmethod
from typing import List


class InvalidStrategyError(Exception):
    """Raised when a strategy is used with an invalid creature."""


class BattleStrategy(ABC):
    """Abstract battle strategy."""

    @abstractmethod
    def is_valid(self, creature: object) -> bool:
        """Return True if the creature is suitable for this strategy."""

    @abstractmethod
    def act(self, creature: object) -> List[str]:
        """Perform the strategy actions for the creature and
        return output lines.

        Raises:
            InvalidStrategyError: raised if the creature is not suitable
                for this strategy.
        """


class NormalStrategy(BattleStrategy):
    """Strategy that simply makes the creature attack."""

    def is_valid(self, creature: object) -> bool:
        return True

    def act(self, creature: object) -> List[str]:
        if not self.is_valid(creature):
            name = getattr(creature, "name", "?")
            msg = f"Invalid Creature '{name}' for this normal strategy"
            raise InvalidStrategyError(msg)
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):
    """Strategy for transforming creatures: transform, attack, revert."""

    def is_valid(self, creature: object) -> bool:
        has_transform = callable(getattr(creature, "transform", None))
        has_revert = callable(getattr(creature, "revert", None))
        return has_transform and has_revert

    def act(self, creature: object) -> List[str]:
        if not self.is_valid(creature):
            name = getattr(creature, "name", "?")
            msg = f"Invalid Creature '{name}' for this aggressive strategy"
            raise InvalidStrategyError(msg)
        outputs = [
            creature.transform(),
            creature.attack(),
            creature.revert(),
        ]
        return outputs


class DefensiveStrategy(BattleStrategy):
    """Strategy for healing creatures: attack then heal."""

    def is_valid(self, creature: object) -> bool:
        return callable(getattr(creature, "heal", None))

    def act(self, creature: object) -> List[str]:
        if not self.is_valid(creature):
            name = getattr(creature, "name", "?")
            msg = f"Invalid Creature '{name}' for this defensive strategy"
            raise InvalidStrategyError(msg)
        return [creature.attack(), creature.heal()]
