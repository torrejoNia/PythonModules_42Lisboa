#!/usr/bin/env python3

import sys

print("\n=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
archivist_id = input("Input Stream active. Enter archivist ID: ARCH_")
status = input("Input Stream active. Enter status report: ")
print(f"\n[STANDARD] Archive status from ARCH_{archivist_id}: {status}",
      file=sys.stdout)
print("[ALERT] System diagnostic: Communication channels verified",
      file=sys.stderr)
print("[STANDARD] Data transmission complete",
      file=sys.stdout)
print("\nThree-channel communication test successful.")
