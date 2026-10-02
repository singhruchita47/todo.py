import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        tasks = file.readlines()
    return [task.strip() for task in tasks]

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks in your to-do list.")
    else:
        print("\n--- To-Do List ---")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    print("------------------")

def main():
    tasks = load_tasks()

    while True:
        display_tasks(tasks)
        print("\nOptions:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. View tasks")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            task = input("Enter the new task: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
                print(f"Task '{task}' added successfully.")
            else:
                print("Task cannot be empty.")
        elif choice == '2':
            try:
                task_num = int(input("Enter the task number to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    save_tasks(tasks)
                    print(f"Task '{removed_task}' removed successfully.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            # Tasks are already displayed at the top of the loop
            pass
        elif choice == '4':
            print("Exiting To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
