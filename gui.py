import functions
import PySimpleGUI as sg
import time



sg.theme("DarkGreen6")


label = sg.Text("Type a to-do")
inputbox = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add", size=7)

listbox = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=(45, 10))
editbutton = sg.Button("Edit")

complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")


clock = sg.Text("", key="clock")


window = sg.Window("TO DO APP", layout=[[clock], [label], [inputbox, add_button], [listbox, editbutton, complete_button], [exit_button]], font=("Helvetica", 12))


while True:
	event, values = window.read(timeout=200)
	window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

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
			try:
				todo_to_edit = values["todos"][0]
				new_todo = values["todo"]

				todos = functions.get_todos()
				index = todos.index(todo_to_edit)
				todos[index] = new_todo
				functions.write_todos(todos)
				window["todos"].update(values=todos)

			except IndexError:
				sg.popup("Please select an item first", font=("Helvetica", 12))


		case "Complete":
			try:
				todo_to_complete = values["todos"][0]
				todos = functions.get_todos()
				todos.remove(todo_to_complete)
				functions.write_todos(todos)
				window["todos"].update(values=todos)
				window["todo"].update(value="")

			except IndexError:
				sg.popup("Please select an item first", font=("Helvetica", 12))




		case "Exit":
			break


		case "todos":
			window["todo"].update(value=values["todos"][0])



		#we get error when we close window without the line below
		case sg.WIN_CLOSED:
			break

window.close()