def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Prompt for and add an item
           item = input("Enter the item add: ")
           shopping_list.append(item)
           print(f"'{item}' added to the shopping list.")
        elif choice == 2:
            # Prompt for and remove an item
            item = input("What do you want to remove: ")
            if item not in shopping_list:
                print(f'{item} not in Shopping List')
            else:
                shopping_list.remove(item)
                print(f"'{item}' revomed from the shopping list.")
                
        elif choice == 3:
            # Display the shopping list
            print("Shopping List:")
            for item in shopping_list:
                print(item)
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()