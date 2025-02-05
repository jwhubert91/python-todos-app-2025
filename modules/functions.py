FILEPATH = "files/todos.txt"

def get_todos(filepath=FILEPATH):
    """
      Read the text file and return the list of to-do items
    :param filepath: Local filepath of todos txt file as a string
    :return: Returns a list of strings
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """ Takes an argument for the todos list, and writes the txt file of todos to the filepath """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello from main!")