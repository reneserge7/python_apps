
def get_todos(filename="todo.txt"):
    with open(filename, 'r') as file1:
        task = file1.readlines()
    return task


def set_todos(todos_agr, filename="todo.txt"):
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
        task = task.strip('\n')  # inserting a line to remove \n
        print(f'{task_index + 1}.{task}')

