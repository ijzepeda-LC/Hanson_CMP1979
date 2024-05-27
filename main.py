from todo_class import TodoList
from second_file import test_add_task
import second_file
import third_file

todo_list = TodoList()
while True:
    print("\nTo-Do List Application")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Clear all tasks")
    print("5. Exit")
    print("6. Test View Task")
    print("5. Test Add task")
    choice = input("Enter choice: ")

    if choice == '1':
        task = input("Enter task: ")
        print(todo_list.add_task(task))
    elif choice == '2':
        tasks = todo_list.view_tasks()
        if tasks:
            for idx, task in enumerate(tasks):
                print(f"{idx}. {task}")
        else:
            print("No tasks available.")
    elif choice == '3':
        try:
            index = int(input("Enter task index to delete: "))
            print(todo_list.delete_task(index))
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == '4':
        print(todo_list.clear_tasks())
    elif choice == '5':
        break
    elif choice == '6':
        # What is happening here
        second_file.test_view_tasks()
    elif choice == '7':
        # What is happening here
        test_add_task()
    else:
        print("Invalid choice. Please try again.")
