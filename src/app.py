### Necessary imports for Streamlit Cloud Deployment to work ###

__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

################################################################

import streamlit as st
from main import CustomCrew

st.title("Your Personal Team of Research Assistants.")

# Create chat history
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []

# Display chat history
for chat_message in st.session_state.chat_messages:
    if "user" in chat_message:
        with st.chat_message("user"):
            st.markdown(chat_message["user"])
    if "Researcher Agents" in chat_message:
        with st.chat_message("Researcher Agents"):
            st.markdown(chat_message["Researcher Agents"])


# Create Sidebar
st.sidebar.header('User Input Features')

st.sidebar.text_input("What Topic Should Our Conversation Revolve Around?:", key="topic", placeholder="Business")

# Define a function to start the custom crew
def start_custom_crew(task):
    # Start custom crew
    custom_crew = CustomCrew(st.session_state["topic"], task)
    with st.spinner('Chillin, just searching the web for ya...'):
        result = custom_crew.run()
    return result

prompt = st.chat_input("Run Crew AI Research Assistants!", key="run")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user input to chat history
    st.session_state.chat_messages.append({"user": prompt})

    with st.chat_message("Researcher Agents"):
        st.markdown(start_custom_crew(prompt))

    # Add agent response to chat history
    st.session_state.chat_messages.append({"Researcher Agents": start_custom_crew(prompt)})