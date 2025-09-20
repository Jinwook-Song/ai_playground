import dotenv
import asyncio
import streamlit as st
from openai import OpenAI
from agents import Agent, Runner, SQLiteSession, WebSearchTool, FileSearchTool

dotenv.load_dotenv()

client = OpenAI()

VECTORE_STORE_ID = "vs_68ce6de8fe508191873dc05426ae0b01"

if "agent" not in st.session_state:
    agent = Agent(
        name="ChatGPT Agent",
        model="gpt-5-nano-2025-08-07",
        instructions="""
        You are a helpful assistant.

        You have access to the followign tools:
            - Web Search Tool: Use this when the user asks a questions that isn't in your training data. Use this tool when the users asks about current or future events, when you think you don't know the answer, try searching for it in the web first.
            - File Search Tool: Use this tool when the user asks a question about facts related to themselves. Or when they ask questions about specific files.
        """,
        tools=[
            WebSearchTool(),
            FileSearchTool(
                vector_store_ids=[VECTORE_STORE_ID],
                max_num_results=3,
            ),
        ],
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
                    st.write(message["content"][0]["text"].replace("$", "\$"))

        if "type" in message:
            if message["type"] == "web_search_call":
                with st.chat_message("ai"):
                    st.write("🔍 Searched the web...")
            elif message["type"] == "file_search_call":
                with st.chat_message("ai"):
                    st.write("🗂️ Searched your files...")


asyncio.run(paint_history())


def update_status(status_container, event):
    status_messages = {
        "response.web_search_call.searching": (
            "🔎 Starting to search web",
            "running",
        ),
        "response.web_search_call.in_progress": (
            "⏳ Searching web...",
            "running",
        ),
        "response.web_search_call.completed": (
            "✅ Searching web complete",
            "complete",
        ),
        "response.file_search_call.searching": (
            "🔎 Starting to search files",
            "running",
        ),
        "response.file_search_call.in_progress": (
            "⏳ Searching files...",
            "running",
        ),
        "response.file_search_call.completed": (
            "✅ Searching files complete",
            "complete",
        ),
        "response.completed": ("", "complete"),
    }

    if event in status_messages:
        label, status = status_messages[event]
        status_container.update(label=label, state=status)


async def run_agent(prompt):
    with st.chat_message("ai"):
        status_container = st.status("⏳", expanded=False)
        text_placeholder = st.empty()
        response = ""

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
                    text_placeholder.write(response.replace("$", "\$"))


prompt = st.chat_input(
    "Enter your message",
    accept_file=True,
    file_type=["pdf", "docx", "txt"],
)

if prompt:
    for file in prompt.files:
        if file.type.startswith("text/"):
            with st.chat_message("ai"):
                with st.status("📄 Uploading file...") as status:
                    uploaded_file = client.files.create(
                        file=(file.name, file.getvalue()),
                        purpose="user_data",
                    )
                    status.update(label="⏳ Attaching file...", state="running")
                    client.vector_stores.files.create(
                        vector_store_id=VECTORE_STORE_ID, file_id=uploaded_file.id
                    )
                    status.update(label="✅ File uploaded", state="complete")

    if prompt.text:
        with st.chat_message("user"):
            st.write(prompt.text)
        asyncio.run(run_agent(prompt.text))


with st.sidebar:
    reset = st.button("Reset memory")
    if reset:
        asyncio.run(session.clear_session())
    st.write(asyncio.run(session.get_items()))
