#!/usr/bin/env python3

X = "\033[0m"
R = "\033[91m"
G = "\033[92m"
H = "\033[1m"
D = "\033[2m"

print(f"{H}\n=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ==={X}")
print(f"{D}Initiating secure vault access...{X}")
print("Vault connection established with failsafe protocols")
print(f"{D}\nSECURE EXTRACTION:{X}")
with open("classified_data.txt") as f:
    data = f.read()
print(data)
print(f"{D}\nSECURE PRESERVATION:{X}")
with open("new_protocols.txt", "w") as f:
    f.write("[CLASSIFIED] New security protocols archived")
print("[CLASSIFIED] New security protocols archived")
print(f"{G}Vault automatically sealed upon completion{X}")
print(f"{G}\nAll vault operations completed with maximum security.{X}")