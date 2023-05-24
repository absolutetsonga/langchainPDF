from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain

openai_api_key = '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'

llm = OpenAI(temperature=1, openai_api_key=openai_api_key)

template = '''Your job is to come up with a classic dish from the area that the users suggests.
% USER LOCATION
{user_location}

YOUR RESPONSE:
'''

prompt_template_location = PromptTemplate(input_variables=["user_location"], template=template)
location_chain = LLMChain(llm=llm, prompt=prompt_template_location)

template = '''Given a meal, give a short and simple recipe on how to make that dish at home
% MEAL
{user_meal}

YOUR RESPONSE:
'''

prompt_template_meal = PromptTemplate(input_variables=["user_meal"], template=template)
meal_chain = LLMChain(llm=llm, prompt=prompt_template_meal)

overall_chain = SimpleSequentialChain(chains=[location_chain, meal_chain], verbose=True)

review = overall_chain.run('Kazakhstan')

print(review)