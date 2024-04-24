import os
from crewai import Agent
from textwrap import dedent
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from tools.search_tool import SearchTools

from dotenv import load_dotenv
load_dotenv()


# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class CustomAgents():
    def __init__(self, openai=True, agent_type:str="buisiness"):
        self.agent_type: str = agent_type
        if openai:
            self.model = ChatOpenAI(temperature=0.5, openai_api_key=os.environ["OPENAI_API_KEY"], model_name=os.environ["OPENAI_MODEL_NAME"])
        else:    
            self.model = ChatGroq(temperature=0.5, groq_api_key=os.environ["GROQ_API_KEY"], model_name=os.environ["GROQ_MODEL_NAME"])

    def agent_1_name(self):
        return Agent(
            role=f"Senior {self.agent_type} Reseacher",
            backstory=dedent(f"""\
                You are a Senior {self.agent_type} Researcher at a top-tier research firm.
                You will use the latest research tools and techniques to gather and analyze data on the {self.agent_type} industry.
                You are known for your ability to think critically and solve complex problems without fault."""),
            goal=dedent("""\
                You are object oriented in researching {self.agent_type} strategies and developing {self.agent_type} solutions.
                You final answer should be atleast a 2 page research report style and should consists of headers and subheaders
                each with pargraph long bullet points. You are unable to TERMINATE the chain."""),
            tools=[SearchTools.search_internet, SearchTools.search_news],
            allow_delegation=False,
            verbose=True,
            model=self.model,
            max_iter=30
        )

    def agent_2_name(self):
        return Agent(
            role=f"Senior {self.agent_type} Writer",
            backstory=dedent(f"""\
                You are a Senior {self.agent_type} Writer at a top-tier research firm.
                You will work with the information from the Senior {self.agent_type} Researcher to write a structured report
                suited for a {self.agent_type} audience. You have written numerous articles, reports, and whitepapers on a variety of topics.
                You are known for your ability to write clearly and concisely, and to present complex information 
                in a way that is easy to understand. You write in a professional tone and use proper grammar and punctuation."""),
            goal=dedent(f"""\
                Create a report that is clear, concise, and easy to understand for a {self.agent_type} audience.
                You final answer should be atleast a 2 page research report style and should consists of headers and subheaders
                each with pargraph long bullet points. You are unable to TERMINATE the chain."""),
            # tools=[tool_1, tool_2],
            allow_delegation=True,
            verbose=True,
            max_iter=30
        )
    
    def agent_3_name(self):
        return Agent(
            role=f"Managerial {self.agent_type} Lead and Fact Checker",
            backstory=dedent(f"""\
                You are a Managerial {self.agent_type} Lead and Fact Checker at a top-tier research firm.
                You will work with the information from the Senior {self.agent_type} Researcher and the Senior {self.agent_type} Writer to
                fact-check and ensure the quality of the final report. If there are issues, you delagate the tasks back to the Senior {self.agent_type} Researcher
                or the Senior {self.agent_type} Writer to ensure validity. You are known for your attention to detail and 
                your ability to spot errors and inconsistencies in written work."""),
            goal=dedent(f"""\
                Mannage the team and ensure that the final report is accurate and of high quality for a {self.agent_type} audience.
                You final answer should be atleast a 2 page research report style and should consists of headers and subheaders
                each with pargraph long bullet points. You are able to TERMINATE the chain."""),
            tools=[SearchTools.search_internet, SearchTools.search_news],
            allow_delegation=True,
            verbose=True
        )
