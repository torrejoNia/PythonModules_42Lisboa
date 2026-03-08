#!/usr/bin/env python3

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
            print(f"Error: '{temp_str}' "
                  f"is too hot for plants (max 40°C)")
            return -2
        if t < 0:
            print(f"Error: '{temp_str}' "
                  f"is too cold for plants (min 0°C)")
            return -3
    except ValueError:
        print(f"Error: '{temp_str}' "
              f"is not a valid number")
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
        t = check_temperature(input("\nTesting temperature: "))
        match t:
            case -1:
                check_bad = True
            case -2:
                check_toohot = True
            case -3:
                check_toocold = True
            case _:
                print("Temperature °C is perfect for plants!")
                check_good = True
    print("\nAll tests completed - program didn't crash!")


test_temperature_input()
