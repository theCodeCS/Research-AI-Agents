import os
from crewai import Agent, Task, Crew, Process

from textwrap import dedent
from agents import CustomAgents
from tasks import CustomTasks

from dotenv import load_dotenv
load_dotenv()

# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py
# You can also define custom crew in this class.

# You can also define your environment variables here for your custom llm model.
# os.environ["OPENAI_API_BASE"] = 'https://api.openai.com/v1'
# os.environ["OPENAI_MODEL_NAME"] = 'gpt-4-turbo'
# os.environ["OPENAI_API_KEY"] = 'sk-1ZQ6'


class CustomCrew:
    def __init__(self, topic:str, task:str, openai:bool):
        self.topic = topic
        self.task = task
        self.openai = openai

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CustomAgents(self.topic, self.openai)
        tasks = CustomTasks(self.task)

        # Define your custom agents and tasks here
        custom_agent_1 = agents.agent_1_name()
        custom_agent_2 = agents.agent_2_name()
        custom_agent_3 = agents.agent_3_name()

        # Custom tasks include agent name and variables as input
        custom_task_1 = tasks.research(
            custom_agent_1
        )

        custom_task_2 = tasks.write_report(
            custom_agent_2,
        )
        custom_task_3 = tasks.summary_and_briefing_task(
            custom_agent_3,
        )

        # Define your custom crew here
        crew = Crew(
            agents=[custom_agent_1, custom_agent_2, custom_agent_3],
            tasks=[custom_task_1, custom_task_2, custom_task_3],
            verbose=True
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Crew AI Template")
    print("-------------------------------")
    openai = True if input(dedent("""Which Model do you want to use? (openai/groq): """)) == "openai" else False
    topic = input(dedent("""What is the Topic you want me to Research about?: """))
    task = input(dedent("""Ask Me what you want me to find: """))

    custom_crew = CustomCrew(topic, task, openai)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)
    # Create a markdown document with the result
    with open('../results/result.md', 'w') as file:
        file.write(result)
    print("Result saved as result.md")
