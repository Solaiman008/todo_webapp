import streamlit as st
import functions
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"] + '\n'
    if new_todo == '\n':
        pass
    else:
        todos.append(new_todo)
        functions.write_todos(todos)
        st.session_state["new_todo"] = ''


st.title("My Todo Web-app")
st.subheader("This is my todo app")
st.write("It is the learning stage.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

    # my code
    # if st.session_state[todo]:
    #   todos.remove(todo)
    #   functions.write_todos(todos)
    #   del st.session_state[todo]
    #   st.rerun()

st.text_input(label="Hudai", placeholder="Add a todo...",
              label_visibility="hidden", key="new_todo",
              on_change=add_todo)