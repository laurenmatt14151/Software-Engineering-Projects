
import json

# Function to load tasks from a file
def load_tasks(file_name):
    try:
        with open(file_name, 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

# Function to save tasks to a file
def save_tasks(tasks, file_name):
    with open(file_name, 'w') as file:
        json.dump(tasks, file)

# Main program
def main():
    task_file = "tasks.json"
    tasks = load_tasks(task_file)

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            new_task = input("Enter task: ")
            tasks.append(new_task)
            save_tasks(tasks, task_file)
            print("Task added successfully.")
        elif choice == '2':
            print("\nTasks:")
            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task}")
        elif choice == '3':
            if not tasks:
                print("No tasks to delete.")
                continue
            print("\nTasks:")
            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task}")
            task_index = int(input("Enter the index of the task to delete: ")) - 1
            if 0 <= task_index < len(tasks):
                del tasks[task_index]
                save_tasks(tasks, task_file)
                print("Task deleted successfully.")
            else:
                print("Invalid task index.")
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
