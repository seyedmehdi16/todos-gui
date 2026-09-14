from unittest import case

import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
exit_button = sg.Button("Exit")

list_box = sg.Listbox(values=functions.get_todos("todos.txt"), key="todos",
                    enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

window = sg.Window('To-Do List', layout=[
    [label],
   [ input_box,
    add_button],
    [list_box, edit_button, complete_button],
    [exit_button]
], font=('8514oem', 23))
while True:
    event, values = window.read()
    print(event)
    print(values)
    print(values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos("todos.txt")
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos("todos.txt", todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos("todos.txt")
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos("todos.txt", todos)
            window['todos'].update(values=todos)
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case "Complete":
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos("todos.txt")
            todos.remove(todo_to_complete)
            functions.write_todos("todos.txt", todos)

            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case "Exit":
            break
        case sg.WINDOW_CLOSED:
            break

window.close()