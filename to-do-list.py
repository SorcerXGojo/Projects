to_do_list = []

def add_task(task):
    """Add a task to the to-do list."""
    to_do_list.append(task)
    print(f"Task '{task}' added to the list.")

def remove_task(task):
    """Remove a task from the to-do list."""    
    if task in to_do_list:
        to_do_list.remove(task)
        print(f"Task '{task}' removed from the list.")
    else:
        print(f"Task '{task}' not found in the list.")

def view_tasks():
    """View all tasks in the to-do list."""
    if to_do_list:
        print("To-Do List:")
        for i, task in enumerate(to_do_list, start=1):
            print(f"{i}. {task}")
    else:
        print("The to-do list is empty.")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            remove_task(task)
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Call the main function to run the program
main()
