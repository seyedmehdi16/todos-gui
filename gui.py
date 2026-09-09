import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window('To-Do List', layout=[
    [label],
    [input_box],
    [add_button]
], font=('helvetica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos("todos.txt")
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos("todos.txt", todos)
        case sg.WINDOW_CLOSED:
            break

window.close()