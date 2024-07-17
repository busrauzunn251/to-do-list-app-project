

def display_menu():
    print("\n--- To-Do List Application ---")
    print("1. Add a to-do")
    print("2. List all to-dos")
    print("3. Delete a to-do")
    print("4. Exit")

def add_todo():
    todo = input("Enter a to-do: ")
    todos.append(todo)
    print(f"'{todo}' has been added to the list.")

def list_todos():
    if len(todos) == 0:
        print("The to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for i, todo in enumerate(todos):
            print(f"{i + 1}. {todo}")

def delete_todo():
    list_todos()
    if len(todos) == 0:
        return
    try:
        index = int(input("Enter the number of the to-do to delete: ")) - 1
        if 0 <= index < len(todos):
            removed = todos.pop(index)
            print(f"'{removed}' has been removed from the list.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

todos = []

while True:
    display_menu()
    choice = input("Your choice (1-4): ")

    if choice == '1':
        add_todo()
    elif choice == '2':
        list_todos()
    elif choice == '3':
        delete_todo()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again.")
