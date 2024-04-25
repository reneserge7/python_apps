import re


def get_todos(filename="todo.txt"):
    with open(filename, 'r') as file1:
        task = file1.readlines()
    return task


def set_todos(todos_agr, filename="todo.txt"):
    # if todos_agr == todos:
    #     filename = "todo.txt"
    # else:
    #     filename = "todo_completed.txt"
    with open(filename, 'w') as file1:
        file1.writelines(todos_agr)


def show(filename):
    """
    read the content of a text file and print the
    output in the form of a numbered list
    """
    with open(filename, 'r') as file1:
        task = file1.readlines()
    new_task = [item.strip('\n') for item in task]

    for task_index, task in enumerate(new_task):
        task = task.strip('\n')
        task_only = task.split(',') #inserting a line to remove \n
        if filename == "todo.txt":
            final_task = task_only[0]
        else:
            final_task = task_only[1]
        print(f'{task_index + 1}.{final_task}')


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
