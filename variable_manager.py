def main():
    variables = {}

    while True:
        print("\n--- Variable Manager ---")
        print("1. Add variable")
        print("2. Show all variables")
        print("3. Get variable value")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter variable name: ")
            value = input("Enter variable value: ")
            variables[name] = value
            print(f"Added '{name}' = {value}")

        elif choice == "2":
            if not variables:
                print("No variables stored.")
            else:
                print("\nStored variables:")
                for name, value in variables.items():
                    print(f"{name} = {value}")

        elif choice == "3":
            name = input("Enter variable name to look up: ")
            if name in variables:
                print(f"{name} = {variables[name]}")
            else:
                print(f"Variable '{name}' not found.")

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

