#!/usr/bin/env python3


def garden_operations(operation_number)-> None:
    if operation_number == 0:
        i = int("abc")
        print(i)
    if operation_number == 1:
        n = 1 / 0
        print(n)
    if operation_number == 2:
        missing = open("missing.txt")
        missing.close()
    if operation_number == 3:
        num = "5" + 2
        print(num)
        print(i)


def test_error_types()-> None:
    print("=== Garden Error Types Demo ===")
    try:
        print("\nTesting operation 0...")
        garden_operations(0)
    except ValueError as error_message:
        print(f"Caught ValueError: {error_message}")
    try:
        print("\nTesting operation 1...")
        garden_operations(1)
    except ZeroDivisionError as error_message:
        print(f"Caught ZeroDivisionError: {error_message}")
    try:
        print("\nTesting operation 2...")
        garden_operations(2)
    except FileNotFoundError as error_message:
        print(f"Caught FileNotFoundError: {error_message}")
    try:
        print("\nTesting operation 3...")
        garden_operations(3)
    except TypeError as error_message:
        print(f"Caught TypeError: {error_message}")
    try:
        print("\nTesting multiple errors together...")
        n = 1 / int("abc")
        print(n)
    except (ValueError, ZeroDivisionError):
        print("Caught ValueError and ZeroDivisionError")
    
    print("\nTesting operation 4...")
    garden_operations(4)
    print("Operation completed successfully")

    print()
    print("All error types tested successfully!")

if __name__ == "__main__":
    test_error_types()
