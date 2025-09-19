import streamlit as st
import time

st.header("ChatGPT Agent")

st.write("Hello from chatgpt-agent!!!!")

st.button("Click me")

st.text_input("Enter your name")

st.feedback("faces")


with st.sidebar:
    st.badge("Badge")


tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.write("This is tab 1")

with tab2:
    st.write("This is tab 2")

with tab3:
    st.write("This is tab 3")


with st.chat_message("ai"):
    st.text("Hello, how are you?")
    with st.status("thinking") as status:
        status.update(label="thinking", state="running")
        time.sleep(2)
        status.update(label="thinking", state="complete")
with st.chat_message("human"):
    st.text("Hi")


st.chat_input("Enter your message", accept_file=True)
