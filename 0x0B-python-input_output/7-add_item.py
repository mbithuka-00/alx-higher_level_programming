#!/usr/bin/python3
"""Add command-line arguments to a Python list and save them to a JSON file."""
import sys

if __name__ == "__main__":
    # Import the functions for saving and loading JSON files
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    try:
        # Attempt to load an existing JSON file, or create an empty list if it doesn't exist
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    # Extend the list with command-line arguments (excluding the script name)
    items.extend(sys.argv[1:])

    # Save the updated list to a JSON file
    save_to_json_file(items, "add_item.json")

