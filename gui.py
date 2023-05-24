import functions
import PySimpleGUI as sg



label = sg.Text("Type a to-do")
inputbox = sg.InputText(tooltip="Enter to-do", key="to-do")
button1 = sg.Button("Add")

window = sg.Window("TO DO APP", layout=[[label], [inputbox, button1]], font=("Helvetica", 12))


while True:
	event, values = window.read()
	print(event)
	print(values)

	match event:
		case "Add":
			todos = functions.get_todos()
			new_todo = values["to-do"] + "\n"
			todos.append(new_todo)
			functions.write_todos(todos)
		#we get error when we close window without the line below
		case sg.WIN_CLOSED:
			break

window.close()