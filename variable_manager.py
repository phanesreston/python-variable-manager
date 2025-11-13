# variable_manager_simple.py

import json
import os

DB_PATH = "variables.json"

def load_vars():
    """Load saved variables (or return empty dict)."""
    if os.path.exists(DB_PATH):
        try:
            with open(DB_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {}

def save_vars(data):
    """Save variables to disk."""
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    variables = load_vars()

    while True:
        print("\n--- Variable Manager ---")
        print("1. Add variable")
        print("2. Show all variables")
        print("3. Get variable value")
        print("4. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            name = input("Variable name: ").strip()
            value = input("Variable value: ").strip()
            variables[name] = value          # store as strings (simple!)
            save_vars(variables)             # persist immediately
            print(f"Saved: {name} = {value}")

        elif choice == "2":
            if not variables:
                print("(no variables yet)")
            else:
                print("\nStored variables:")
                for k, v in variables.items():
                    print(f"{k} = {v}")

        elif choice == "3":
            name = input("Name to look up: ").strip()
            if name in variables:
                print(f"{name} = {variables[name]}")
            else:
                print(f"'{name}' not found.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

