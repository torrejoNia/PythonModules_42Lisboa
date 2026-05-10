from abc import ABC, abstractmethod


class HealCapability(ABC):
    """Abstract capability for healing actions."""

    @abstractmethod
    def heal(self) -> str:
        """Return the healing action description."""


class TransformCapability(ABC):
    """Abstract capability for transform actions."""

    @abstractmethod
    def transform(self) -> str:
        """Return the transform action description."""

    @abstractmethod
    def revert(self) -> str:
        """Return the revert action description."""
