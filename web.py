import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
	todo = st.session_state["new_todo"] + "\n"
	todos.append(todo)
	functions.write_todos(todos)


st.title("My to-do App")
st.subheader("This is my to-do App")
st.write("This app increases your productivity")






for item in todos:
	st.checkbox(item)




st.text_input(label="Enter a to-do", placeholder="Add a new to-do", on_change=add_todo, key="new_todo")


st.session_state