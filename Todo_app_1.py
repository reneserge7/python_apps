from datetime import datetime


def show(filename):

    with open(filename, 'r') as file:
        todos = file.readlines()
    new_todos = [item.strip('\n') for item in todos]

    for index, task in enumerate(new_todos):
        task = task.strip('\n')  # inserting a single line to remove \n
        print(f'{index + 1}.{task}')


while True:
    user_action = input("Type add, show , edit, complete , done or exit ")
    user_action = user_action.strip()
    if user_action.startswith("add"):
        todo = user_action[4:]

        with open('todo.txt', 'r') as file:
            todos = file.readlines()
        todos.append(todo.upper() + '\n')
        
        with open('todo.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        show('todo.txt')

    elif user_action.startswith("edit"):
        try:
            show('todo.txt')
            number = int(input("Enter the number you want to edit:"))
            number = number - 1

            with open("todo.txt", "r") as file:
                todos = file.readlines()

            edited = todos[number].strip('\n')
            new_todos = (input("Enter New Task: ")).upper()
            todos[number] = new_todos + '\n'

            with open('todo.txt', 'w') as file:
                file.writelines(todos)

                message = f"Todo {edited} was replaced with {new_todos} from the list"
                print(message)
        except ValueError:
            print("invalid command")
            continue

    elif user_action.startswith("complete"):
        try:
            show('todo.txt')
            num_comp = int(input("Enter the completed Item num: "))

            with open("todo.txt", "r") as file:
                todos = file.readlines()
            index = num_comp-1
            todo_to_removed = todos[index].strip('\n')
            todos.pop(index)

            with open('todo.txt', 'w') as file:
                file.writelines(todos)

            with open('todo_completed.txt', 'r') as file:
                todo_completed = file.readlines()
            now = datetime.now()
            current_time = now.strftime('%m-%d-%Y %H:%M')
            todo_completed.append(current_time + " " + todo_to_removed.upper() + '\n')

            with open('todo_completed.txt', 'w') as file:
                file.writelines(todo_completed)
        except IndexError:
            print("There is no item with that number.")
            continue

        message = f"Todo {todo_to_removed}\t was removed from the list"
        print(message)
        show('todo.txt')

    elif user_action.startswith("done"):
        with open('todo_completed.txt', 'r') as file:
            file.readlines()
        show('todo_completed.txt')
    elif user_action.startswith("exit"):
        break
    else:
        print("Bye!")
print("Command is invalid!")
