import streamlit as st
from backend import ask_ollama

st.set_page_config(
    page_title="Llama 3.2 Chatbot",
    page_icon="🤖"
)

st.title("🤖 Llama 3.2 Chatbot")

# Store conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
question = st.chat_input("Ask something...")

if question:

    # Display user message
    with st.chat_message("user"):
        st.write(question)

    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    # Get response from Ollama
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = ask_ollama(question)

        st.write(answer)

    # Store assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })