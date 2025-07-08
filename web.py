import streamlit as st
import Functions


st.title("Hello, Streamlit!")

todos = Functions.read_todos()

if not todos:
    st.write("No todos found. Please add some.")

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    # pdb.set_trace()  # Uncomment this line to set a breakpoint for debugging
    if not todo.strip():  # todo empty check
        st.warning("Please enter a todo.")
        return
    todos.append(todo)
    Functions.write_todos(todos)


st.write("## Your Todos")

for todo in todos:
    st.checkbox(todo)


new_todo = st.text_input(label="", placeholder="Add a new todo..", key="new_todo",on_change=add_todo)
