todos = []

while True:
  user_action= input("Type add, show, edit or exit: ")
  user_action= user_action.strip()
  match user_action:
    case "add":
      task= input("Enter a todo: ")
      todos.append(task)
    case "show":
      print("Here is a list of your stask for this day.")
      for index, task in enumerate(todos) :
        print (f"{index + 1} . {task}")
    case "edit":
      old_task_numper = int(input("Enter the task number you will like to Edit: "))
      old_task_numper= old_task_numper - 1
      new_task = input("Enter the new task: ")
      todos[old_task_numper] = new_task
      print("Here is a the new list of your stask for this day.")
      for index, task in enumerate(todos) :
        print (f"{index + 1} . {task}")
    case "exit":
      print("Bye")
