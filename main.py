

import os
import openai
import mysql.connector

cnx = mysql.connector.connect(user='admin', password='password',
host='mydb.cojn5ewfdu5p.us-west-1.rds.amazonaws.com', database='Poker_Venmo_Integreation')
cursor = cnx.cursor()

openai.api_key = "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"

model_engine = "text-davinci-003"
prompt="What is the current news on the Kyrie Irving Trade in 30 words or less in 2023"

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.01, # higher values correspond to corr with crazier responses
)

print(completion)

response = completion.choices[0].text
print(response)

with open("output.txt", "a") as f:
  print(response, file=f)
  


# sample query 1
query = "INSERT INTO `HackSC`.`master` (`idmaster`, `question`, `response`) VALUES ('1', '\"why?\"', '\"because\"');"

# execute query command
cursor.execute(query)

# sample query 2
# query = 'DROP TABLE `Poker_Venmo_Integreation`.`todaysTable`'
