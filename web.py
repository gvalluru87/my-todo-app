import streamlit as st
import Functions


st.title("Hello, Streamlit!")

todos = Functions.read_todos()

st.set_page_config(page_title="Todo App",
    page_icon=":clipboard:",
    layout="wide",
    initial_sidebar_state="expanded"
)

if not todos:
    st.write("No todos found. Please add some.")

def add_todo():
    todo = st.session_state["new_todo"]
    # pdb.set_trace()  # Uncomment this line to set a breakpoint for debugging
    if not todo.strip():  # todo empty check
        st.warning("Please enter a todo.")
        return
    todos.append(todo)
    Functions.write_todos(todos)

new_todo = st.text_input(label="", placeholder="Add a new todo..", key="new_todo",on_change=add_todo)


st.write("## Your Todos")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        Functions.write_todos(todos)
        st.experimental_rerun()  # Refresh the page to update the todo list



