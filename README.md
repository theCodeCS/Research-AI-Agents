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
Make sure to have a stable internet connection to run the crew of agents.

### Large Language Model Selection
The user can select the large language model to use for the agents by changing the `model` variable in the `main.py` file. The user can choose between the following models:
1. `openai-gpt`: OpenAI's GPT model.
2. `groq`: Groq's large language model.

## Output
The agents will output the final research summary on the user's specified topic.
