import sys # This is a sample Python script.
import json

# Press ⌃F5 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
todo_file= 'todo.json'

def load_tasks():
    try:
        with open(todo_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(todo_file, 'w') as f:
        json.dump(tasks, f, indent=4)

def strikeout(task):
    result = ''
    for c in task:
        result = result + c + '\u0336'
    task=result
    return task


def main():

    if len(sys.argv) < 2:
        print('Usage: python todo.py [add/list/remove] [task/index]')
        return
    command = sys.argv[1].lower()
    tasks = load_tasks()

    if command=='add':
        task = " ".join(sys.argv[2:])
        if task:
            tasks.append({
                "task": task,
                "completed": False
            })
            save_tasks(tasks)
            print(f'{task} added into your tasks list')
    elif command=='list':
        if not tasks:
            print('No tasks added')
            return
        for i,task in enumerate(tasks,1):
            status="✅" if task["completed"] else "⬜"
            print(f'{i}. {status} {task["task"]}')

    elif command=='complete':
        if not tasks:
            print('No tasks added')
        try:
            idx=int(sys.argv[2])-1
            tasks[idx]["completed"]= True
            save_tasks(tasks)
            print(f'{tasks[idx]["task"]} marked as completed')

        except (IndexError, ValueError):
            print("Invalid index")


    elif command=='remove':
        try:
            idx = int(sys.argv[2])-1
            removed=tasks.pop(idx)
            save_tasks(tasks)
            print(f'{removed["task"]} removed from your tasks list')
        except (IndexError, ValueError):
            print('Invalid index error')
if __name__ == '__main__':
    main()



# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
