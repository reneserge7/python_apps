from datetime import datetime
from functions import get_todos, set_todos, show
while True:
    user_action = input("Type add, show , edit, complete , done or exit ")
    user_action = user_action.strip()
    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()
        todos.append(todo.upper() + '\n')
        set_todos(todos)
        with open('todo.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        show('todo.txt')

    elif user_action.startswith("edit"):
        try:
            show('todo.txt')
            number = int(input("Enter the number you want to edit:"))
            number = number - 1

            todos = get_todos()

            edited = todos[number].strip('\n')
            new_todos = (input("Enter New Task: ")).upper()
            todos[number] = new_todos + '\n'

            set_todos(todos)

            message = f"Todo {edited} was replaced with {new_todos} from the list"
            print(message)
        except ValueError:
            print("invalid command")
            continue

    elif user_action.startswith("complete"):
        try:
            show('todo.txt')
            num_comp = int(input("Enter the completed Item num: "))

            todos = get_todos('todo.txt')
            index = num_comp - 1
            todo_to_removed = todos[index].strip('\n')
            todos.pop(index)

            set_todos(todos)

            todo_completed = get_todos('todo_completed.txt')

            now = datetime.now()
            current_time = now.strftime('%m-%d-%Y %H:%M')
            todo_completed.append(current_time + " " + todo_to_removed.upper() + '\n')
            set_todos(todo_completed, 'todo_completed.txt')

        except IndexError:
            print("There is no item with that number.")
            continue

        message = f"Todo {todo_to_removed}\t was removed from the list"
        print(message)
        show('todo.txt')

    elif user_action.startswith("done"):
        show('todo_completed.txt')
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is invalid!")

print("Bye!")


