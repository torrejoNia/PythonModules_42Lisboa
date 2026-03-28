#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    """Returns the temperature."""

    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    try:
        print("Input data is '25'")
        t = input_temperature("25")
        print(f"Temperature is now {t}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    try:
        print("Input data is 'abc'")
        t = input_temperature("abc")
        print(f"Temperature is now {t}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    test_temperature()

