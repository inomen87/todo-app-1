import functions
import PySimpleGUI as sg



label = sg.Text("Type a to-do")
inputbox = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add")

listbox = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=(45, 10))
editbutton = sg.Button("Edit")

complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("TO DO APP", layout=[[label], [inputbox, add_button], [listbox, editbutton, complete_button], [exit_button]], font=("Helvetica", 12))


while True:
	event, values = window.read()
	print(1,event)
	print(2,values)


	match event:
		case "Add":
			todos = functions.get_todos()
			new_todo = values["todo"] + "\n"
			todos.append(new_todo)
			functions.write_todos(todos)
			window["todos"].update(values=todos)


		case "Edit":
			todo_to_edit = values["todos"][0]
			new_todo = values["todo"]

			todos = functions.get_todos()
			index = todos.index(todo_to_edit)
			todos[index] = new_todo
			functions.write_todos(todos)
			window["todos"].update(values=todos)


		case "Complete":
			todo_to_complete = values["todos"][0]
			todos = functions.get_todos()
			todos.remove(todo_to_complete)
			functions.write_todos(todos)
			window["todos"].update(values=todos)
			window["todo"].update(value="")


		case "Exit":
			break


		case "todos":
			window["todo"].update(value=values["todos"][0])



		#we get error when we close window without the line below
		case sg.WIN_CLOSED:
			break

window.close()