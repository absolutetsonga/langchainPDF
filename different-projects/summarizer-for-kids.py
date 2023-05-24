from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

openai_api_key = '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'

llm = OpenAI(temperature=0, model_name='text-davinci-003', openai_api_key=openai_api_key)

template = '''
    % INSTRUCTIONS:
    Please summarize the following piece of text. Respond in a manner that a 5 year old kid would understand.

    % TEXT:
    {text}
'''

prompt = PromptTemplate(input_variables=["text"], template=template)

analyze_text = 'Neurophysics is an interdisciplinary science using physics and combining it with other neurosciences ' \
               'to better understand neural processes. The methods used include the techniques of experimental ' \
               'biophysics and other physical measurements such as EEG[1] mostly to study electrical, mechanical or ' \
               'fluidic properties, as well as theoretical and computational approaches.[2] The term "neurophysics" ' \
               'is a portmanteau of "neuron" and "physics".'

final_prompt = prompt.format(text=analyze_text)
output = llm(final_prompt)

print(output)