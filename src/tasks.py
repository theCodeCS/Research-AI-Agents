from crewai import Task
from textwrap import dedent

# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks():
    def __init__(self, task:str="research the {agent_type} industry.", agent_type:str="business"):
        self.task: str = task
        self.agent_type: str = agent_type

    def research(self, agent):
        return Task(description=dedent(f"""                         
                You will try you're best to answer the following questions:
                {self.task}

                Use the tool, collect in-depth recent news articles, press releases, and market analyses related to the {self.agent_type} industry.
                Pay special attention to any significant events, national and worldwide sentiments, and expert opinions.

                Make sure to use the most recent data as possible and provide a detailed analysis of the problem at hand.
                
                No need to use the tool multiple times, just use it once and provide a detailed analysis of the problem at hand."""),
            expected_output=dedent(f"""\
                A 2 page, in-depth, research report style and should consists of headers and subheaders each with 5-7 sentences of summarized bullet points.
                The report should be a detailed analysis of the industry landscape, and actionable recommendations for your {self.agent_type} audience."""),
            agent=agent
        )
    
    def write_report(self, agent):
        return Task(
            description=dedent(f"""\
                Write a detailed report based on the research findings, industry analysis,
                and strategic talking points. The report should be tailored to a {self.agent_type} audience.
                No need to use the tool multiple times, just use it once and provide a detailed analysis of the problem at hand."""),
            expected_output=dedent(f"""\
                A 2 page, in-depth, research report style and should consists of headers and subheaders each with 5-7 sentences of summarized bullet points.
                The report should be a detailed analysis of the industry landscape, and actionable recommendations for the {self.agent_type} audience."""),
            agent=agent
        )

