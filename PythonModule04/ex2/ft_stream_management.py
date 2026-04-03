#!/usr/bin/env python3

import sys

X = "\033[0m"
G = "\033[92m"
Y = "\033[93m"
H = "\033[1m"

print(f"{H}\n=== CYBER ARCHIVES - COMMUNICATION SYSTEM ==={X}")
id = input(f"{Y}Input Stream active. Enter archivist ID: {X}ARCH_")
status = input(f"{Y}Input Stream active. Enter status report: {X}")
print(f"\n[STANDARD] Archive status from ARCH_{id}: {status}",
      file=sys.stdout)
print("[ALERT] System diagnostic: Communication channels verified",
      file=sys.stderr)
print("[STANDARD] Data transmission complete",
      file=sys.stdout)
print(f"{G}\nThree-channel communication test successful.{X}")