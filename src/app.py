import streamlit as st
from langchain_core.callbacks import BaseCallbackHandler
from typing import TYPE_CHECKING, Any, Dict, List, Optional
from textwrap import dedent

from main import CustomCrew

st.title("Your Personal Team of Research Assistants.")

st.text_input("What is the Topic you want me to Research about?:", key="topic")
st.text_input("Ask Me what you want me to find:", key="task")

if st.button("Run Crew AI Research Assistant!"):
    # Start custom crew
    custom_crew = CustomCrew(st.session_state["topic"], st.session_state["task"])
    result = custom_crew.run()
    st.write(result)

    # Create a markdown document with the result
    # with open('../results/result.md', 'w') as file:
    #     file.write(result)
    # print("Result saved as result.md")