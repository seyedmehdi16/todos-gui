#from functions import get_todos, write_todos
import functions
import time

todos = []
user_prompt = "Enter a todo: "

now = time.strftime("%b %d, %Y %H:%M:%S")
print('It is', now)

while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        # Read todos from file
        todos = functions.get_todos("todos.txt")

        todos.append(todo)

        # Write todos in the file
        functions.write_todos("todos.txt", todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos("todos.txt")

        for number, todo in enumerate(todos):
            todo = todo.strip("\n")
            todo = todo.capitalize()
            number = number + 1
            print(f"{number}- {todo}")
    elif user_action.startswith("edit"):
        try:
            todos = functions.get_todos("todos.txt")

            number = user_action[5:]
            number = int(number) - 1
            new_todo = input(user_prompt) + "\n"
            todos[number] = new_todo

            # Write todos in the file
            functions.write_todos("todos.txt", todos)
        except ValueError:
            print("Hey, you should enter a number!")
        except IndexError:
            print("There is no item with that number")
    elif user_action.startswith("complete"):
        try:
            number = user_action[9:]

            todos = functions.get_todos("todos.txt")

            number = int(number) - 1
            todo_to_remove = todos[number].strip("\n")
            todos.pop(number)

            # Write todos in the file
            functions.write_todos("todos.txt", todos)

            message = f"Todo: {todo_to_remove} was successfully completed."
            print(message)
        except IndexError:
            print("There is no item with that number")
        except ValueError:
            print("Hey, you should enter a number!")
    elif user_action.startswith("exit"):
        break
    else:
        print("Hey, the command not found!!")