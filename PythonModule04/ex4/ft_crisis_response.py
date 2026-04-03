#!/usr/bin/env python3


print("\n=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
try:
    print("\nCRISIS ALERT: Attempting access to 'lost_archive.txt'")
    with open("lost_archive.txt") as f:
        print(f"SUCCESS: Archive recovered - \"{f.read()}\"")
except FileNotFoundError:
    print("RESPONSE: Archive not found in storage matrix")
print("STATUS: Crisis handled, system stable")

try:
    print("\nCRISIS ALERT: Attempting access to 'classified_vault.txt'")
    with open("classified_vault.txt") as f:
        print(f"SUCCESS: Archive recovered - \"{f.read()}\"")
except PermissionError:
    print("RESPONSE: Security protocols deny access")
print("STATUS: Crisis handled, security maintained")

try:
    print("\nROUTINE ACCESS: Attempting access to 'standard_archive.txt'")
    with open("standard_archive.txt") as f:
        print(f"SUCCESS: Archive recovered - \"{f.read()}\"")
except OSError as e:
    print(f"RESPONSE: {e}")
print("STATUS: Normal operations resumed")

print(f"\nAll crisis scenarios handled successfully. Archives secure.")
