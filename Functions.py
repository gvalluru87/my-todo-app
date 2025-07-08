FILE_PATH = 'Files/todos.txt'
# Path to the todo file
# This file is used to store the list of todos
todos = []

def read_todos():
    try:
        with open(FILE_PATH, 'r') as file:
            todos = file.readlines()
            return [todo.strip() for todo in todos]
    except FileNotFoundError:
        return []

def write_todos(todos):
    with open(FILE_PATH, 'w') as file:
        file.writelines(f"{todo}\n" for todo in todos)
        

def edit_todo(todos, number, new_todo):
    if 0 <= number < len(todos):
        todos[number] = new_todo
        print(f"Todo {number + 1} has been updated to '{new_todo}'.")
    else:
        print("Invalid todo number.")

def complete_todo(todos, number):
    if 0 <= number < len(todos):
        completed_todo = todos.pop(number)
        print(f"Todo '{completed_todo}' completed and removed from the list.")
    else:
        print("Invalid todo number.")   


def show_todos(todos):
    if not todos:
        print("No todos found.")
    else:
        for index, todo in enumerate(todos):
            print(f"{index + 1}: {todo}")   


def add_todo(todos, todo):
    todos.append(todo)
    print(f"Todo '{todo}' added.")
    with open(FILE_PATH, 'w') as file:
        file.writelines(f"{todo}\n" for todo in todos)  

def exit_program():
    print("Exiting the program.")
    exit(0)

print("Welcome to custom functions!")