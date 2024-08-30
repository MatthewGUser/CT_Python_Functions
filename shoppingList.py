shopping_list = []

# [ Task 1 ]
def add_to_cart(item):
    shopping_list.append(item)

# [ Task 2 ]
def remove_from_cart(item):
    if item in shopping_list:
        shopping_list.remove(item)
    else:
        print(f"{item} is not in the shopping list.")

# [ Task 3 ]
def display_cart():
    if shopping_list:
        print("Your shopping list:")
        for i, item in enumerate(sorted(shopping_list), start=1):
            print(f"{i}. {item}")
    else:
        print("Your shopping list is empty.")

# [ Operation ]
shopping = True
while shopping:
    choice = input("add, remove, print, or quit? ").lower()
    
    if choice == "add":
        item = input("Please enter item name: ")
        add_to_cart(item)
    elif choice == "remove":
        item = input("Please enter item name: ")
        remove_from_cart(item)
    elif choice == "print":
        display_cart()
    elif choice == "quit":
        print("Exiting the shopping list program. Goodbye!")
        break
    else:
        print("Unknown input, please enter a valid action.")
