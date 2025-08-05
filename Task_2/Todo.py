import os
import json

to_do_file = "TO-Do.json"
def load_tasks():
    if not os.path.exists(to_do_file):
        return []
    with open(to_do_file, "r") as file:
        return json.load(file)

def save_tasks(operation):
    with open(to_do_file, "w") as file:
        json.dump(operation, file, indent=4)

def view_task(operation):
    if not operation:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(operation, start=1):
            status = "Completed" if task["done"] else "Pending"
            print(f"{i}. {task['task']} [{status}]")
        print()

def add_task(operation):
    new_task = input("Enter your task here: ")
    task = {"task": new_task, "done": False}
    operation.append(task)
    save_tasks(operation)
    print(f"Task is successfully added\nTask: {new_task}")

def remove_task(operation):
    view_task(operation)
    try:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(operation):
            removed = operation.pop(index)
            save_tasks(operation)
            print(f"Task removed: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_task(operation):
    view_task(operation)
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(operation):
            operation[index]["done"] = True
            save_tasks(operation)
            print(f"Task marked as done: {operation[index]['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    operation = load_tasks()

    while True:
        print("\n======== Welcome TO TO-DO list Console ========")
        print("1. View Task")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task As Done")
        print("5. Exit")
        
        try:
            choice = int(input("What Operation do you want to do?\nYour choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 to 5.")
            continue

        if choice == 1:
            view_task(operation)
        elif choice == 2:
            add_task(operation)
        elif choice == 3:
            remove_task(operation)
        elif choice == 4:
            mark_task(operation)
        elif choice == 5:
            print("\n======== Exiting TO-DO list Console ========")
            print("Thank you for using the CLI application!!")
            break
        else:
            print("Invalid option! Please enter a number between 1 to 5.")

if __name__ == "__main__":
    main()