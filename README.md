# Research-AI-Agents

<h3>[<a href='https://ai-research-agents.streamlit.app/'> Link </a>] 🤖<a href='https://ai-research-agents.streamlit.app/'> Try Out the Researcher Agents </a> </h3>

## Introduction
This repository hosts custom large language models from OpenAI and Groq, as well as Crew AI agents, which utilize the Serper API to scrape and query web information related to topics specified by the user. These agents are developed in Python and are designed to execute a series of tasks efficiently:

1. They search for the top 10 results related to the specified topic and provide a concise summary of these results.
2. The research agent delves deeper by searching and querying the web to compile a detailed summary on the chosen topic.
3. Subsequently, the writer agent reviews the research summary to correct any grammatical errors.
4. Finally, the Managerial Lead agent evaluates and synthesizes both the research and the corrected summaries, producing a final polished research summary that is then delivered back to the user.


## Installation
To install the required packages run the requirements.txt file using the following command:
```bash
pip install -r requirements.txt
```

## Usage
To run the agents, run the following command:
```bash
python main.py
```
1. Make sure to have a stable internet connection to run the crew of agents.
2. The user will be prompted to enter the topic they would like to research. (e.g. "Healthcare")
3. The user will then be prompted to ask the question they would like to research. (e.g. "Write me a papaer summarizing anxiety within children?")
4. The agents will then output the final research summary on the user's specified topic.

### Large Language Model Selection
The user can select the large language model to use for the agents by changing updating the environment variables in the `main.py`. The user can choose between the following models:
1. `openai`: OpenAI's GPT model.
2. `groq`: Groq's large language model.
3. `custom`: Can use own custom models by updating the `os.environ["OPENAI_API_BASE"]` variable.

## Output
The agents will output the final research summary on the user's specified topic.
