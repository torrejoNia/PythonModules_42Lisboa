"""
Creature card factory package.

This package implements the abstract factory design pattern for creating
creature cards with different families.
"""

from .creatures import FlameFactory, AquaFactory

__all__ = ["FlameFactory", "AquaFactory"]
