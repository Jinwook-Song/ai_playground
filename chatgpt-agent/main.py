import dotenv
import asyncio
import streamlit as st
from agents import Agent, Runner, SQLiteSession, WebSearchTool

dotenv.load_dotenv()

if "agent" not in st.session_state:
    agent = Agent(
        name="ChatGPT Agent",
        model="gpt-5-nano-2025-08-07",
        instructions="""
            You are a helpful assistant that can answer questions and help with tasks.

            You can use the web search tool to get the latest information.
            You can use the tools provided to help the user.
        """,
        tools=[WebSearchTool()],
    )
    st.session_state["agent"] = agent
else:
    agent = st.session_state["agent"]

if "session" not in st.session_state:
    session = SQLiteSession(session_id="chat-history", db_path="chat-gpt-memory.db")
    st.session_state["session"] = session
else:
    session = st.session_state["session"]


async def paint_history():
    mesasges = await session.get_items()
    for message in mesasges:
        if "role" in message:
            with st.chat_message(message["role"]):
                if message["role"] == "user":
                    st.write(message["content"])
                else:
                    st.write(message["content"][0]["text"])

        if "type" in message and message["type"] == "web_search_call":
            with st.chat_message("assistant"):
                st.write("🔎 Searching the web...")


def update_status(status_container, event):
    status_messages = {
        "response.web_search_call.searching": ("🔎 Starting to search", "running"),
        "response.web_search_call.in_progress": ("⏳ Searching...", "running"),
        "response.web_search_call.completed": ("✅ Searching complete", "complete"),
        "response.completed": ("✅ Completed", "complete"),
    }

    if event in status_messages:
        label, status = status_messages[event]
        status_container.update(label=label, state=status)


asyncio.run(paint_history())


async def run_agent(prompt):
    with st.chat_message("assistant"):
        status_container = st.status("⏳", expanded=False)
        text_placeholder = st.empty()
        response = ""

        update_status(status_container, "name of the event")

        stream = Runner.run_streamed(
            agent,
            prompt,
            session=session,
        )

        async for event in stream.stream_events():
            if event.type == "raw_response_event":
                update_status(status_container, event.data.type)
                if event.data.type == "response.output_text.delta":
                    response += event.data.delta
                    text_placeholder.write(response)


prompt = st.chat_input("Enter your message")
if prompt:
    with st.chat_message("user"):
        st.write(prompt)
    asyncio.run(run_agent(prompt))


with st.sidebar:
    reset = st.button("Reset memory")
    if reset:
        asyncio.run(session.clear_session())
    st.write(asyncio.run(session.get_items()))
