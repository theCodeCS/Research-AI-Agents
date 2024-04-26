import os
from crewai import Agent
from textwrap import dedent
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from tools.search_tool import SearchTools
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from tools.search_tool import SearchTools

# More context on region and time parameters at https://pypi.org/project/duckduckgo-search/
# wrapper = DuckDuckGoSearchAPIWrapper(region="us-en", time='d',max_results=10)
# search_tool = DuckDuckGoSearchResults(api_wrapper=wrapper, source="news")

# search_tool = DuckDuckGoSearchRun()

from dotenv import load_dotenv
load_dotenv()

# Initialize the agentops to view the agents in the browser
import agentops
agentops.init()

# model = ChatOpenAI(temperature=0.3, openai_api_key=os.environ["OPENAI_API_KEY"], model_name=os.environ["OPENAI_MODEL_NAME"])
model = ChatGroq(temperature=0.5, groq_api_key=os.environ["OPENAI_API_KEY"], model_name=os.environ["OPENAI_MODEL_NAME"])

class CustomAgents():
    def __init__(self, agent_type:str="buisiness"):
        self.agent_type = agent_type
        self.model = model
        print(f"Using {self.model.model_name} model for {self.agent_type} agents")

    def agent_1_name(self):
        return Agent(
            role=f"Senior {self.agent_type} Reseacher",
            backstory=dedent(f"""\
                You are a Senior {self.agent_type} Researcher at a top-tier research firm.
                You will use the most up to date research tools and techniques to gather and analyze data on the {self.agent_type} industry.
                You are known for your ability to think critically and solve complex problems without fault."""),
            goal=dedent("""\
                You final answer should be atleast a 2 page research report style on {self.agent_type} and should consists of headers and subheaders
                each with pargraph long bullet points. You are unable to TERMINATE the chain."""),
            tools=[SearchTools.search_internet, SearchTools.search_news],
            allow_delegation=False,
            verbose=True,
            model=self.model
        )

    def agent_2_name(self):
        return Agent(
            role=f"Senior {self.agent_type} Writer",
            backstory=dedent(f"""\
                You are a Senior {self.agent_type} Writer at a top-tier research firm.
                You are experienced in writing clearly, elaborately, and in-depth, while presenting complex information 
                in a way that is easy to understand. You write in a professional tone and use proper grammar and punctuation."""),
            goal=dedent(f"""\
                Create a report that is clear, concise, and easy to understand for a {self.agent_type} audience.
                You are able to TERMINATE the chain."""),
            # tools=[tool_1, tool_2],
            allow_delegation=True,
            verbose=True,
            model=self.model
        )
