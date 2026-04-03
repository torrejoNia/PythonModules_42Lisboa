#!/usr/bin/env python3
"""
Command Quest - Display command-line arguments
Shows the program name and all arguments passed to the script.
"""

import sys

program_name = sys.argv[0]

num_args = len(sys.argv) - 1

print("=== Command Quest ===")
print("Program name:", program_name)

if num_args == 0:
    print("No arguments provided!")
else:
    print("Arguments received:", num_args)
    i = 1
    while i < len(sys.argv):
        print(f"Argument {i}: {sys.argv[i]}")
        i += 1

print("Total arguments:", len(sys.argv))
