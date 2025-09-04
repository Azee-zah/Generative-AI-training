from task_the_mind import *

tasks = []


def add_task(task):
    tasks.append(task)
    return task
    # print(f"{task}A new task has been added!")



def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("This task has been removed from the to-do list")
    else:
        print("Task is not on the list")


def view_task(tasks):
    # if tasks:
    print(f"This is your to-do list\n{tasks}")
        

def completed_task(task):
    for task in tasks:
        if task == True:
            print(f"You have completed this {task}")

while True:
    print("\nMy options")
    print("1. Add tasks")
    print("2. Remove tasks")
    print("3. View tasks")
    print("4. Exit")
    option = input("Select from options 1-4 ")


    if option == "1":
        task = input("Enter the task here: ")
        add_task(task)
        view_task(tasks)

    elif option == "2":
        task = input("Enter the task to remove: ")
        remove_task(task)
        

    elif option == "3":
        print(f"Below is your to-do list\n{tasks}")
        view_task(tasks)

    elif option == "4":
        print("The End, Thank you")
        break

    else:
        print("Invalid input!")



