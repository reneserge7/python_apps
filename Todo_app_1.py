from datetime import datetime
import functions
# CSV glob, webbrowser, shutil
now = datetime.now()
current_time = now.strftime('%m-%d-%Y %H:%M')

while True:
    user_action = input("Type add, show , edit, complete , done or exit ")
    user_action = user_action.strip()
    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()
        todos.append(todo.upper() + "," + current_time + '\n')
        functions.set_todos(todos)

    elif user_action.startswith("show"):
        functions.show('todo.txt')

    elif user_action.startswith("edit"):
        try:
            functions.show('todo.txt')
            number = int(input("Enter the number you want to edit:"))
            number = number - 1

            todos = functions.get_todos()

            edited = todos[number].strip('\n')
            new_todos = (input("Enter New Task: ")).upper()
            todos[number] = new_todos + '\n'

            functions.set_todos(todos)

            message = f"Todo {edited} was replaced with {new_todos} from the list"
            print(message)
        except ValueError:
            print("invalid command")
            continue

    elif user_action.startswith("complete"):
        try:
            functions.show('todo.txt')
            num_comp = int(input("Enter the completed Item num: "))

            todos = functions.get_todos('todo.txt')
            index = num_comp - 1
            todo_to_removed = todos[index].strip('\n')
            todos.pop(index)

            functions.set_todos(todos)

            todo_completed = functions.get_todos('todo_completed.txt')

            todo_completed.append(current_time + ", " + todo_to_removed.upper() + '\n')
            functions.set_todos(todo_completed, 'todo_completed.txt')

        except IndexError:
            print("There is no item with that number.")
            continue

        message = f"Todo {todo_to_removed}\t was removed from the list"
        print(message)
        functions.show('todo.txt')

    elif user_action.startswith("done"):
        functions.show('todo_completed.txt')
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is invalid!")

print("Bye!")


