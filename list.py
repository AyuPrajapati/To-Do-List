todo = []

def menu():
    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        todo.append(task)
        print("Task added.")

    elif choice == "2":
        if not todo:
            print("No tasks added.")
        else:
            for i, t in enumerate(todo, 1):
                print(f"{i}. {t}")

    elif choice == "3":
        if not todo:
            print("No tasks to remove.")
        else:
            for i, t in enumerate(todo, 1):
                print(f"{i}. {t}")
            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(todo):
                removed = todo.pop(num - 1)
                print("Removed:", removed)
            else:
                print("Invalid choice.")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid input.")
