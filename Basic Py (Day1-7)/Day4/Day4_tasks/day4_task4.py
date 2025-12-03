# Todo System with Match and For Loops

def display_tasks(todo_list):
    if not todo_list:
        print("No tasks in the list!")
        return
    
    print("\nYour Todo List:")
    print("-" * 20)
    for index, task in enumerate(todo_list, 1):
        print(f"{index}. {task}")
    print("-" * 20)

def main():
    todo_list = []
    
    print("TO-DO System")
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Add task")
        print("2. Remove task")
        print("3. View all tasks")
        print("4. Clear all tasks")
        print("5. Count tasks")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        match choice:
            case "1":
                # Add multiple tasks using loop
                print("\nAdd Tasks (enter 'done' to finish):")
                while True:
                    task = input("Enter task: ").strip()
                    if task.lower() == 'done':
                        break
                    if task:
                        todo_list.append(task)
                        print(f"Added: {task}")
                    else:
                        print("Task cannot be empty!")
                        
            case "2":
                # Remove task with for loop display
                if not todo_list:
                    print("No tasks to remove!")
                    continue
                    
                display_tasks(todo_list)
                
                try:
                    task_num = int(input("Enter task number to remove: "))
                    if 1 <= task_num <= len(todo_list):
                        removed_task = todo_list.pop(task_num - 1)
                        print(f"✓ Removed: '{removed_task}'")
                    else:
                        print("Invalid task number!")
                except ValueError:
                    print("Please enter a valid number!")
                    
            case "3":
                # View tasks
                display_tasks(todo_list)
                
            case "4":
                # Clear all tasks using for loop confirmation
                if not todo_list:
                    print("No tasks to clear!")
                    continue
                    
                display_tasks(todo_list)
                confirm = input("Are you sure you want to clear all tasks? (y/n): ")
                if confirm.lower() == 'y':
                
                    print("Removing tasks:")
                    for task in todo_list:
                        print(f"  - {task}")
                    todo_list.clear()
                    print("All tasks cleared!")
                    
            case "5":
                if not todo_list:
                    print("No tasks in the list!")
                else:
                    print(f"Total tasks: {len(todo_list)}")
                    # Using for loop to show task
                    print("Task lengths:")
                    for i, task in enumerate(todo_list, 1):
                        print(f"  {i}. '{task}' - {len(task)} characters")
                        
            case "6":
                # Exit with summary using for loop
                print("\nFinal Todo List Summary:")
                display_tasks(todo_list)
                print("Thank you for using Todo System! Goodbye!")
                break
                
            case _:
                print("Invalid choice! Please enter 1-6.")

if __name__ == "__main__":
    main()