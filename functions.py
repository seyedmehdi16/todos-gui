def get_todos(filepath):
    """
    Read a text file and return the list of to-do items.
    :return:
    """
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos

def write_todos(filepath, todos):
    """
    Write the to-do items list in the next file.
    :param todos:
    :return:
    """
    with open(filepath, "w") as file:
        file.writelines(todos)