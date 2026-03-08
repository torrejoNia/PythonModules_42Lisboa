#!/usr/bin/env python3


def garden_operations(exception):
    if exception is ValueError:
        i = int("abc")
        print(i)
    if exception is ZeroDivisionError:
        n = 1 / 0
        print(n)
    if exception is FileNotFoundError:
        missing = open("missing.txt")
        missing.close()
    if exception is KeyError:
        d = {"rose": 5, "b": 10}
        i = d["missing_plant"]
        print(i)


def test_error_types():
    print("=== Garden Error Types Demo ===")
    try:
        print("\nTesting ValueError...")
        garden_operations(ValueError)
    except ValueError as error_message:
        print(f"Caught ValueError: {error_message}")
    try:
        print("\nTesting ZeroDivisionError...")
        garden_operations(ZeroDivisionError)
    except ZeroDivisionError as error_message:
        print(f"Caught ZeroDivisionError: {error_message}")
    try:
        print("\nTesting FileNotFoundError...")
        garden_operations(FileNotFoundError)
    except FileNotFoundError as error_message:
        print(f"Caught FileNotFoundError: {error_message}")
    try:
        print("\nTesting KeyError...")
        garden_operations(KeyError)
    except KeyError as error_message:
        print(f"Caught KeyError: {error_message}")

    print("\nTesting multiple errors together...")
    try:
        n = 1 / int(input("What to divide 1 by? "
                          "(divide by 0 or string) "))
        print(n)
    except (ValueError, ZeroDivisionError):
        print("\nCaught an error, but program continues!")
        print("\nAll error types tested successfully!")


test_error_types()
