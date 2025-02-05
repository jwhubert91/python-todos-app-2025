from modules.functions import get_todos, write_todos
import time

now = time.strftime("%b %d %Y %H:%M:%S")
print("It is ", now)

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = input("Enter a todo: ") + "\n"
        todos = get_todos()
        todos.append(todo)
        write_todos(todos)

    # | is a bitwise OR operator
    elif user_action.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n").title()
            print(f"{index} - {item}")

    elif user_action.startswith("edit"):
        try:
            todo_index = int(input("Enter todo item index: "))

            todos = get_todos()
            current_todo = todos[todo_index]

            updated_todo = input(f"What would you like to replace {current_todo.strip("\n")} with? ")
            todos[todo_index] = updated_todo + "\n"

            write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            completed_todo_index = int(input("Todo index you would like to complete: "))

            todos = get_todos("files/todos.txt")

            removed_todo = todos.pop(completed_todo_index)

            write_todos(todos)

            print(f"{removed_todo.strip("\n")} was removed from the list")
        except IndexError:
            print("There is no item with that index number")

    elif user_action.startswith("exit"):
        break

    else:
        print("This command is not valid.")