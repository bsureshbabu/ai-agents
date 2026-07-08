import streamlit as st
from llm.ollama_client import get_llm

st.set_page_config(
    page_title="Travel AI Agent",
    page_icon="✈️",
    layout="wide"
)

with st.sidebar:
    st.title("⚙️ Settings")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.write("Model")
    st.success("Gemma3:4B (Local)")

st.title("✈️ Travel AI Agent")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Plan your trip...")

if prompt:
    st.session_state.messages.append(
        {"role":"user","content":prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    llm = get_llm()

    response = ""

    with st.chat_message("assistant"):

        placeholder = st.empty()

        for chunk in llm.stream(prompt):
            response += chunk.content
            placeholder.markdown(response + "▌")

        placeholder.markdown(response)

    st.session_state.messages.append(
        {"role":"assistant","content":response}
    )