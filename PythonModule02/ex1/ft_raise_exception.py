#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    """Returns the temperature, or raises an error.
    """
    t = int(temp_str)

    if t > 40:
        raise ValueError(
            f"{t}°C is too hot for plants (max 40°C)"
        )

    if t < 0:
        raise ValueError(
            f"{t}°C is too cold for plants (min 0°C)"
        )
    return t


def test_temperature() -> None:
    """Takes input from the user and checks if it is a correct temperature."""
    print("=== Garden Temperature Checker ===")
    print()

    tests = ["25", "abc", "100", "-50"]

    for temp in tests:
        try:
            print(f"Input data is '{temp}'")
            t = input_temperature(temp)
            print(f"Temperature is now {t}°C\n")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
