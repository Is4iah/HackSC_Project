import os
import openai
import json

with open('sample.json') as json_file:
    dic = json.load(json_file)
 
    # Print the type of data variable
    # print("Type:", type(dic))

titles = list(dic.keys())
first_sum = dic[titles[0]]
first_sum = first_sum.replace('\n', ' ')
# print(first_sum)

openai.api_key = "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"

model_engine = "text-davinci-003"
prompt="Summarize this in 150 words:\n\n" + first_sum

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    top_p = 1.0,
    frequency_penalty = 0.0,
    presence_penalty = 0.0,
    stop=None,
    temperature=0.7, # higher values correspond to corr with crazier responses
)

# print(completion)

response = completion.choices[0].text
print(response)


with open("openAI.txt", "a") as f:
  print(prompt + "\n", file = f)  
  print("Original: \n", file = f)
  print(first_sum + "\n\n", file = f) 
  print("OpenAI:\n", file = f)
  print(response + "\n\n\n\n", file=f)
  
  

