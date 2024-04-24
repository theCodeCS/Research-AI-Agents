from crewai import Task
from textwrap import dedent

# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks():
    def __init__(self, task:str="research the {agent_type} industry."):
        self.task: str = task
        self.agent_type: str = "business"

    def research(self, agent):
        return Task(description=dedent(f"""                         
            You will try you're best to answer the following questions:
            {self.task}

            Collect in-depth recent news articles, press releases, and market analyses related to the {self.agent_type} industry.
            Pay special attention to any significant events, national and worldwide sentiments, and expert opinions.

            Make sure to use the most recent data as possible.

            Your final answer should be:
            A 2 page, in-depth, research report style and should consists of headers and subheaders each with 5-7 sentences of summarized bullet points.

            You are unable to TERMINATE the chain.
        """),
        agent=agent
        )
    
    def write_report(self, agent):
        return Task(
            description=dedent(f"""\
                You will try you're best to answer the following questions:
                {self.task}

                Write a detailed report based on the research findings, industry analysis,
                and strategic talking points provided by the Senior {self.agent_type} Researcher.
                
                Your final answer should be:
                A 2 page research report style.
                
                Ensure that the report is clear, elaborate, in-depth, and easy to understand for a {self.agent_type} audience.
                Use proper grammar, punctuation, and formatting.

                You are unable to TERMINATE the chain.
            """),
            agent=agent
        )

    def summary_and_briefing_task(self, agent):
        return Task(
			description=dedent(f"""\
				Compile all the research findings, industry analysis, and strategic
				talking points into a full page report for your {self.agent_type} audience.
                Make sure to answer all the user's questions and provide a detailed analysis of the problem
                at hand with headers and sub-headers to the question: 
                {self.task}

                Your final answer should be:
				A 2 page research style report on {self.agent_type}.
                It should be a detailed analysis of the industry landscape, and actionable recommendations for your audience.
                Make sure to use proper grammar, punctuation, and formatting.

                You are the only agent able to TERMINATE the chain.

                You can only terminate the chain when you are confident that you have answered all the user's questions and 
                the output should be a two page in-depth final report.
                """),
			agent=agent
		)

