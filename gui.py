import functions
import PySimpleGUI as Sg
import os

if not os.path.exists('todo.txt'):
    with open('todo.txt', 'w') as file:
        pass

Sg.theme("Black")

clock = Sg.Text('', key='clock')

label = Sg.Text(" Type in a To_do")
input_box = Sg.InputText(tooltip="Enter todo", key="todo", do_not_clear=False)
add_button = Sg.Button("Add")
list_box = Sg.Listbox(values=functions.get_todos(), key='todos_in_List_box',
                      enable_events=True, size=(45, 10))
edit_button = Sg.Button('Edit')
complete_button = Sg.Button('Complete')
Exit_button = Sg.Button('Exit')
window = Sg.Window('My Todo -App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [Exit_button]],

                   font=("Helvetica", 20))
while True:

    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, f"selected task: {values['todos_in_List_box']}")
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.set_todos(todos)
            window['todos_in_List_box'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos_in_List_box'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            functions.set_todos(todos)
            window['todos_in_List_box'].update(values=todos)
        case "Complete":
            todo_to_complete = values['todos_in_List_box'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.set_todos(todos)
            window['todos_in_List_box'].update(values=todos)
        case "todos_in_List_box":
            window['todo'].update(value=values['todos_in_List_box'][0])
        case "Exit":
            break
        case Sg.WIN_CLOSED:
            break
print("bye")
window.close()
