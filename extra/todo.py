import os
import json

with open("todo.json") as f:
    read = f.read()
if not read:
    tasks = {}
else:
    tasks = json.load(open("todo.json"))

def update_tasks():
    global tasks
    if tasks:
        i = 1
        updated_tasks = {}
        for task in tasks:
            updated_tasks[i] = tasks[task]
            i += 1
        tasks = updated_tasks
        with open("todo.json","w") as j:
            json.dump(tasks,j,indent=2)

while True:

    os.system('cls' if os.name == 'nt' else 'clear')

    print("\n### To Do List ###\n")

    if not tasks:
        print("No tasks yet!")
    else:
        for task in tasks:
            print(f"### {task}: {tasks[task]}")
    
    print("\nCommands: 'add' 'remove' 'quit' ")
    user_input = input("Enter: ").strip().lower()

    if user_input == 'quit':
        break
    
    elif user_input == 'add':
        add = input("Add task: ")
        tasks[len(tasks) + 1] = add
        update_tasks()
    
    elif user_input == 'remove':
        rem = int(input("Remove task #: "))
        if not tasks:
            print("No tasks to remove!")
            continue
        if int(rem) in range(1,len(tasks) + 1):
            del tasks[rem]
            update_tasks()
        else:
            print("Not a task number!")


