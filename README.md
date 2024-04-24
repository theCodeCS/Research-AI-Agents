# Research-AI-Agents

## Introduction
This repository contains custom large language models (Open AI / Groq for Open source models) and Crew AI agents utilizing the Serper to scrape and query information on the user's specified topic on the web. The agents are built using Python and Serper API. The agents are capable of performing the following tasks:

1. Search for the top 4 search results on the user's specified topic and return the summary of the search results.
2. The research agent will search and query the web then create a research summary on the user's specified topic.
3. The writer agent will then correct grammatical errors in the research agent's summary.
4. Finally the Managerial Lead agent will vet and summarize the research agent's summary and the writer agent's corrected summary, then output the final research summary on the user's specified topic back to the user.


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
3. Or use their own custom models by updating the `os.environ["OPENAI_API_BASE"]` variable.

## Output
The agents will output the final research summary on the user's specified topic.
