import functions
import PySimpleGUI as sg



label = sg.Text("Type a to-do")
inputbox = sg.InputText(tooltip="Enter to-do", key="todo")
button1 = sg.Button("Add")

listbox = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=(45, 10))
editbutton = sg.Button("Edit")


window = sg.Window("TO DO APP", layout=[[label], [inputbox, button1], [listbox, editbutton]], font=("Helvetica", 12))


while True:
	event, values = window.read()
	print(1,event)
	print(2,values)
	print(3,values["todos"])

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

		case "todos":
			window["todo"].update(value=values["todos"][0])



		#we get error when we close window without the line below
		case sg.WIN_CLOSED:
			break

window.close()