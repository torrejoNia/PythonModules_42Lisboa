#!/usr/bin/env python3

"""Inventory analyzer using dictionary operations."""

import sys


print("=== Inventory System Analysis ===")

inventory = {}

for raw_param in sys.argv[1:]:
    colon_count = 0
    colon_index = -1
    i = 0
    while i < len(raw_param):
        if raw_param[i] == ":":
            colon_count += 1
            colon_index = i
        i += 1

    if colon_count != 1:
        print(f"Error - invalid parameter '{raw_param}'")
        continue

    item_name = raw_param[:colon_index]
    quantity_text = raw_param[colon_index + 1:]

    if item_name == "" or quantity_text == "":
        print(f"Error - invalid parameter '{raw_param}'")
        continue

    if item_name in inventory:
        print(f"Redundant item '{item_name}' - discarding")
        continue

    try:
        quantity_value = int(quantity_text)
    except ValueError as error:
        print(f"Quantity error for '{item_name}': {error}")
        continue

    inventory[item_name] = quantity_value

print("Got inventory:", inventory)

item_list = list(inventory.keys())
print("Item list:", item_list)

total_quantity = sum(inventory.values())
print(f"Total quantity of the {len(item_list)} items:", total_quantity)

for item_name in item_list:
    if total_quantity == 0:
        percentage = 0.0
    else:
        percentage = round((inventory[item_name] * 100) / total_quantity, 1)
    print(f"Item {item_name} represents {percentage}%")

if len(item_list) > 0:
    most_item = item_list[0]
    least_item = item_list[0]

    for item_name in item_list[1:]:
        if inventory[item_name] > inventory[most_item]:
            most_item = item_name
        if inventory[item_name] < inventory[least_item]:
            least_item = item_name

    print(
        f"Item most abundant: {most_item} with quantity "
        f"{inventory[most_item]}"
    )
    print(
        f"Item least abundant: {least_item} with quantity "
        f"{inventory[least_item]}"
    )

inventory.update({"magic_item": 1})
print("Updated inventory:", inventory)
