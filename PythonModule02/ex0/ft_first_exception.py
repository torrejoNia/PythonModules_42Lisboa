#!/usr/bin/env python3


X = "\033[0m"
R = "\033[91m"
G = "\033[92m"
B = "\033[94m"
C = "\033[96m"
M = "\033[95m"
Y = "\033[93m"
D = "\033[2m"
H = "\033[1m"


def check_temperature(temp_str: str) -> int:
    """Returns the temperature, or a negative number on any error.

    - `-1` -> `ValueError`
    - `-2` -> Temperature is too hot
    - `-3` -> Temperature is too cold
    """
    t = -1
    try:
        t = int(temp_str)
        if t > 40:
            print(f"{R}Error: '{temp_str}' "
                  f"is too hot for plants (max 40°C){X}")
            return -2
        if t < 0:
            print(f"{R}Error: '{temp_str}' "
                  f"is too cold for plants (min 0°C){X}")
            return -3
    except ValueError:
        print(f"{R}Error: '{temp_str}' "
              f"is not a valid number{X}")
    return t


def test_temperature_input():
    """Takes input from the user and checks if it is a correct temperature."""
    print("=== Garden Temperature Checker ===")
    check_good = False
    check_bad = False
    check_toohot = False
    check_toocold = False
    while not check_good \
            or not check_bad \
            or not check_toohot \
            or not check_toocold:
        t = check_temperature(input(f"{H}\nTesting temperature: {X}"))
        match t:
            case -1:
                check_bad = True
            case -2:
                check_toohot = True
            case -3:
                check_toocold = True
            case _:
                print(f"Temperature {t}°C is perfect for plants!")
                check_good = True
    print(f"{G}\nAll tests completed - program didn't crash!{X}")


test_temperature_input()
