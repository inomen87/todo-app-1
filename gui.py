import functions
import PySimpleGUI as sg



label = sg.Text("Type a to-do")
inputbox = sg.InputText(tooltip="Enter to-do")
button1 = sg.Button("Add")

window = sg.Window("TO DO APP", layout=[[label], [inputbox, button1]])
window.read()
window.close()