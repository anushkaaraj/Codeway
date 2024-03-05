def display_menu():
    print("\nMenu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark as Done")
    print("4. Save and Exit")

#add a task to the tasks list
def add_task(tasks):
    task = input("Enter task description: ")
    tasks.append(task)
    print("Task added successfully!")

#view all tasks in the tasks list
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
        return
    
    print("\nTasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

#mark a task as done and remove it from the tasks list
def mark_task_done(tasks):
    if not tasks:
        print("\nNo tasks available to mark as done.")
        return

    view_tasks(tasks)
    index = int(input("Enter task index to mark as done: ")) - 1

    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f"Task '{removed_task}' marked as done and removed.")
    else:
        print("Invalid task index.")

#save tasks to a file
def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + '\n')
    print("Tasks saved successfully!")

#load tasks from a file
def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []

#main function to manage the task list
def main():
    #load existing tasks or start with an empty list
    tasks = load_tasks()

    #user interaction loop
    while True:
        display_menu()

        #get user choice
        choice = input("Enter your choice: ")

        #execute the chosen action
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            print("Saving and Exiting.")
            save_tasks(tasks)
            break
        else:
            print("Invalid choice. Please select a valid option.")

main()
