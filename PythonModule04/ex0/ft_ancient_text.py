
print("\n=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
print("Accessing storage vault: \"ancient_fragment.txt\"")
try:
    f = open("ancient_fragment.txt")
    print("Connection established.")
    print(f"\nRECOVERED DATA:\n{f.read()}")
    print("\nData recovery complete. Storage unit disconnected.")
    f.close()
except FileNotFoundError:
    print("Error: storage vault not found")