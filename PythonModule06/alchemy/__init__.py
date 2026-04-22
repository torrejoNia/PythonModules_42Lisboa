__version__ = "1.0.0"

__author__ = "esnavarr"

from .elements import create_air
from .potions import strength_potion, healing_potion
from .transmutation import lead_to_gold

# alias
heal = healing_potion

__all__ = [
    "strength_potion",
    "healing_potion",
    "heal",
    "create_air",
    "lead_to_gold",
    "__version__",
    "__author__"
]
