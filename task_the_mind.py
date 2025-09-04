# tasks = []

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





    
