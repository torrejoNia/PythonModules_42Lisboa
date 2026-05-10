#!/usr/bin/env python3
"""Tournament runner using battle strategies (ex2)."""

from typing import List, Tuple

from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
)
from ex2.strategies import BattleStrategy


Opponent = Tuple[object, BattleStrategy]


def run_tournament(name: str, opponents: List[Opponent]) -> None:
    print(f"Tournament {name}")
    brief = ", ".join(
        (
            f"({getattr(fac.create_base(), 'name', '?')}+"
            f"{type(strat).__name__.replace('Strategy', '')})"
        )
        for fac, strat in opponents
    )
    print(f"[ {brief} ]")
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    print()

    try:
        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):
                fac_i, strat_i = opponents[i]
                fac_j, strat_j = opponents[j]
                print("* Battle *")
                c1 = fac_i.create_base()
                c2 = fac_j.create_base()
                print(c1.describe())
                print("vs.")
                print(c2.describe())
                print("now fight!")
                for outputs in (strat_i.act(c1), strat_j.act(c2)):
                    for line in outputs:
                        print(line)
                print()
    except InvalidStrategyError as exc:
        print(f"Battle error, aborting tournament: {exc}")


def main() -> None:
    # Tournament 0 (basic)
    opponents0 = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ]
    run_tournament("0 (basic)", opponents0)
    print()

    # Tournament 1 (error)
    opponents1 = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ]
    run_tournament("1 (error)", opponents1)
    print()

    # Tournament 2 (multiple)
    opponents2 = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ]
    run_tournament("2 (multiple)", opponents2)


if __name__ == "__main__":
    main()
