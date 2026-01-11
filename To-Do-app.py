# simple todo list app

todo_list = []

def add_task():
    task = input("Enter a task: ")
    todo_list.append(task)
    print("Task added successfully\n")

def view_task():
    if len(todo_list) == 0:
        print("No tasks available\n")
    else:
        print("Your Tasks:")
        for i in range(len(todo_list)):
            print(i + 1, ".", todo_list[i])
        print()

def remove_task():
    view_task()
    if len(todo_list) == 0:
        return
    num = int(input("Enter task number to remove: "))
    if num > 0 and num <= len(todo_list):
        todo_list.pop(num - 1)
        print("Task removed successfully\n")
    else:
        print("Invalid number\n")

def menu():
    while True:
        print("---- MENU ----")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Program closed")
            break
        else:
            print("Invalid choice, try again\n")

menu()





