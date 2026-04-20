__version__ = "1.0.0"

__author__ = "esnavarr"

from .elements import create_air
from .potions import strength_potion, healing_potion

# alias
heal = healing_potion

__all__ = [
    "strength_potion",
    "healing_potion",
    "heal",
    "create_air",
    "__version__",
    "__author__"
]
