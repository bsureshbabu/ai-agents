# ==========================================================================================

# # from langchain_ollama import ChatOllama
# # from langchain_core.messages import SystemMessage, HumanMessage

# # # Initialize the model
# # llm = ChatOllama(
# #     model="qwen2.5:1.5b",
# #     temperature=0.2,
# #     num_predict=80
# # )

# # print("🤖 AI Chat Agent")
# # print("Type 'exit' to quit.\n")

# # while True:
# #     question = input("You: ")

# #     if question.lower() == "exit":
# #         print("👋 Goodbye!")
# #         break

# #     # System + User Messages
# #     messages = [
# #         SystemMessage(
# #             content="""
# # You are an AI tutor.

# # Rules:
# # - Answer in 2-4 lines.
# # - Be concise.
# # - Give examples.
# # - Don't explain unnecessarily.
# # """
# #         ),
# #         HumanMessage(content=question)
# #     ]

# #     # Get AI Response
# #     answer = llm.invoke(messages)

# #     print("AI:", answer.content)
# #     print("-" * 50)

# ==================================================================================



# import streamlit as st
# from langchain_ollama import ChatOllama

# st.set_page_config(
#     page_title="My AI Chat",
#     page_icon="🤖",
#     layout="wide"
# )

# st.title("🤖 Ayaan AI Assistant")

# llm = ChatOllama(
#     model="qwen2.5:1.5b",
#     # temperature=0.2,
#     # num_predict=100
# )

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Show previous messages
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["content"])

# # Chat input
# prompt = st.chat_input("Ask anything...")

# if prompt:
#     st.session_state.messages.append(
#         {"role": "user", "content": prompt}
#     )

#     with st.chat_message("user"):
#         st.markdown(prompt)

#     response = llm.invoke(prompt).content

#     with st.chat_message("assistant"):
#         st.markdown(response)

#     st.session_state.messages.append(
#         {"role": "assistant", "content": response}
#     )

#===========================================================================================
import streamlit as st

from langchain_ollama import ChatOllama

import config
import utils

# ----------------------------
# Page
# ----------------------------

st.set_page_config(
    page_title=config.PAGE_TITLE,
    page_icon="🤖",
    layout="wide"
)

st.title(config.PAGE_TITLE)

# ----------------------------
# Sidebar
# ----------------------------

with st.sidebar:

    st.header("⚙ Settings")

    model = st.selectbox(

        "Choose Model",

        [
            "qwen2.5:1.5b",
            "gemma3:4b",
            "llama3.2"
        ],

        index=0

    )

    temperature = st.slider(

        "Temperature",

        0.0,

        1.0,

        config.DEFAULT_TEMPERATURE

    )

    if st.button("🗑 Clear Chat"):

        st.session_state.messages = []

        st.rerun()

# ----------------------------
# Load LLM
# ----------------------------

llm = ChatOllama(

    model=model,

    temperature=temperature,

    num_predict=config.MAX_TOKENS

)

# ----------------------------
# Session
# ----------------------------

utils.initialize_session()

utils.display_chat()

# ----------------------------
# Input
# ----------------------------

prompt = st.chat_input("Ask me anything...")

if prompt:

    utils.add_message("user", prompt)

    with st.chat_message("user"):

        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = llm.invoke(prompt)

            st.markdown(response.content)

    utils.add_message(

        "assistant",

        response.content

    )