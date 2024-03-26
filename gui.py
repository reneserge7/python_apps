import functions
import PySimpleGUI as sg

label = sg.Text(" Type in a To_do")
input_box = sg.InputText(tooltip="Enter todo" , key="todo")
add_button = sg.Button("Add")

window = sg.Window('My Todo -App',
                   layout=[[label], [input_box, add_button]],
                   font=("Helvetica", 20))
while True:

    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos=functions.get_todos()
            new_todo = value['todo'] + "\n"
            todos.append(new_todo)
            functions.set_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()

