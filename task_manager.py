import json
import os

FILE_NAME = "tasks.json"

# ==============================
# Load tasks from file
# ==============================
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

# ==============================
# Save tasks to file
# ==============================
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# ==============================
# Add task
# ==============================
def add_task(tasks):
    title = input("Enter task name: ").strip()

    if not title:
        print("Task name cannot be empty!")
        return

    task = {
        "title": title,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

# ==============================
# View tasks
# ==============================
def view_tasks(tasks):
    if not tasks:
        print("No tasks available!")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['title']} - {status}")

# ==============================
# Complete task
# ==============================
def complete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("\nEnter task number to complete: "))
        if number < 1 or number > len(tasks):
            raise ValueError

        tasks[number - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    except:
        print("Invalid task number!")

# ==============================
# Delete task
# ==============================
def delete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("\nEnter task number to delete: "))
        if number < 1 or number > len(tasks):
            raise ValueError

        removed = tasks.pop(number - 1)
        save_tasks(tasks)
        print(f"Task '{removed['title']}' deleted!")
    except:
        print("Invalid task number!")

# ==============================
# Menu
# ==============================
def show_menu():
    print("\n===== TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Completed")
    print("4. Delete Task")
    print("5. Exit")

# ==============================
# Main loop
# ==============================
def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

# ==============================
# Run program
# ==============================
if __name__ == "__main__":
    main()
