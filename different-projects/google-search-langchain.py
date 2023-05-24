from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
import json

openai_api_key = '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'
serpapi_api_key = 'f2b65a5e6cfc63b03204d729040158026677dd59d2d49d76f261cc8abe937e38'

llm = OpenAI(temperature=0, openai_api_key=openai_api_key)

toolkit = load_tools(['serpapi'], llm=llm, serpapi_api_key=serpapi_api_key)
agent = initialize_agent(toolkit, llm, agent='zero-shot-react-description', verbose=True, return_intermediate_steps=True)

response = agent({"input": 'Where is Ronaldo currently is playing?'})

print(json.dumps(response["intermediate_steps"], indent=2))