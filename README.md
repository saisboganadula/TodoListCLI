# TodoListCLI
This is a simple Command-line TODO List application built with Python. 
It allows users to add, list, complete, and remove tasks, with tasks saved between runs using JSON. 

##Features
- Add new tasks from the terminal
- View all the saved tasks
- Mark tasks that are completed
- Remove Tasks from the list by Index

## TechStack
- Python
- JSON file storage
- CLI arguments using 'sys.argv'

##Usage

Add a task:
```bash
python script.py add "Buy Groceries"
```
List all tasks:
```bash
python script.py list
```
Mark a task as completed based on the index:
```bash
python script.py complete 1
```
Remove a task based on its index: 
```bash
python script.py remove 1
```


### 6. Installation instructions

Since this is basic Python, no external libraries are needed.

```md
## Installation

Clone the repository:
```
```bash
git clone https://github.com/saisboganadula/TodoListCLI.git
cd TodoListCLI
```


## Data Persistence
Tasks are stored in 'text.json'
When the program starts, it loads existing tasks from the JSON file
Whenever a task is added, completed, or removed, the updated task list is savedback to the file.


