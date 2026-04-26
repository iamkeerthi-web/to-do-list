tasks = []

def show_task():
    if not tasks:
        print("no tasks exists")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks, 1):
          print(i, ".", task)
        
def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task sucesfully  added")

def remove_task():
    show_task()
    if tasks:
        num = int(input("Enter number of task to be removed: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            print("Task sucesfully removed")
        else:
            print("Invalid number")

while True:
    print("\nTo do list")
    print("1.view task")
    print("2.add task")
    print("3.remove task")
    print("4.exit task")

    choice = input("Enter your choice(1/2/3/4): ")

    if choice == "1":
        show_task()

    elif choice == "2":
        add_task()

    elif choice == "3":
        remove_task()

    elif choice == "4":
        print("Bye")
        break 

    else:
        print("Invalid input")


