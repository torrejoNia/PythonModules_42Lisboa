X = "\033[0m"
R = "\033[91m"
G = "\033[92m"
Y = "\033[93m"
H = "\033[1m"
D = "\033[2m"

print(f"{H}\n=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ==={X}")
try:
    print("\nCRISIS ALERT: Attempting access to 'lost_archive.txt'")
    with open("lost_archive.txt") as f:
        print(f"{Y}SUCCESS: Archive recovered - \"{f.read()}\"{X}")
except FileNotFoundError:
    print(f"{R}RESPONSE: Archive not found in storage matrix{X}")
print(f"{G}STATUS: Crisis handled, system stable{X}")

try:
    print("\nCRISIS ALERT: Attempting access to 'classified_vault.txt'")
    with open("classified_vault.txt") as f:
        print(f"{Y}SUCCESS: Archive recovered - \"{f.read()}\"{X}")
except PermissionError:
    print(f"{R}RESPONSE: Security protocols deny access{X}")
print(f"{G}STATUS: Crisis handled, security maintained{X}")

try:
    print("\nROUTINE ACCESS: Attempting access to 'standard_archive.txt'")
    with open("standard_archive.txt") as f:
        print(f"{Y}SUCCESS: Archive recovered - \"{f.read()}\"{X}")
except OSError as e:
    print(f"{R}RESPONSE: {e}{X}")
print(f"{G}STATUS: Normal operations resumed{X}")

print(f"{G}\nAll crisis scenarios handled successfully. Archives secure.{X}")