tasks = []  # list to store tasks

def show_tasks():
    if len(tasks) == 0:
        print("\nNo tasks yet.")
    else:
        print("\nYour To-Do List:")
        for i in range(len(tasks)):
            print(str(i+1) + ". " + tasks[i])

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added.")

def remove_task():
    show_tasks()
    if len(tasks) > 0:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            print("Removed:", removed)
        else:
            print("Invalid number.")

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
