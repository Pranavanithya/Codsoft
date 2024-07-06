tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def remove_task(task):
    """Function to remove a task from the list"""
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed.")
    else:
        print(f"Task '{task}' not found in the list.")

def view_tasks():
    """Function to display all tasks"""
    if tasks:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks found.")

def main():
    """Main function to run the to-do list application"""
    while True:
        print("\nTODO LIST APPLICATION")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            n=int(input("enter no of task:"))
            for i in range(n):
                task=input("enter task:")
                add_task(task)
        elif choice == '2':
            task = input("Enter task to remove: ")
            remove_task(task)
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
