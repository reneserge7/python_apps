def show():
    with open('todo.txt', 'r') as file:
        todos = file.readlines()
    new_todos = [item.strip('\n') for item in todos]

    for index, task in enumerate(new_todos):
        task = task.strip('\n')  # inserting a single line to remove \n
        print(f'{index + 1}.{task}')

while True:

    user_action = input("Type add, show , edit, complete or exit ")
    user_action = user_action.strip()
    if "add" in  user_action:
        todo = user_action[4:]# slicing a sting

        with open('todo.txt', 'r') as file:
            todos = file.readlines()
        todos.append(todo.upper())
        
        with open('todo.txt', 'w') as file:
                file.writelines(todos)

    elif "show" in user_action:
        show()

    elif "edit" in user_action:
            show()
            number = int(input("Enter the number you want to edit"))
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

    elif "complete" in user_action:
            show()
            num_comp = int(input("Enter the completed Item num: "))

            with open("todo.txt", "r") as file:
                todos = file.readlines()
            index = num_comp-1
            todo_to_removed = todos[index].strip('\n')
            todos.pop(index)

            with open('todo.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_removed}\t was removed from the list"
            print(message)
            show()
    elif "exit" in user_action:
        break
    else:
        print("Bye!")
