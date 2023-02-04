import mysql.connector
import json

# create connection to my SQL
cnx =mysql.connector.connect(user='admin', password='password',
host='hacksc.cojn5ewfdu5p.us-west-1.rds.amazonaws.com', database='HackSC')
cursor = cnx.cursor()


with open('sample.json') as json_file:
    dic = json.load(json_file)
 
    # Print the type of data variable
    print("Type:", type(dic))
    
cnt = 0
for title in dic.keys():
    print(str(cnt) + ": "+  title + "\n")
    print(str(cnt) + ": "+ dic[title])
    cnt += 1


# # create variables passed into query
# id = "69"
# question = "why"
# answer = "because"

# # create query
# query = "INSERT INTO master (`idmaster`, `question`, `response`) VALUES ('" + id + "', '" + question + "', '" + answer + "');"

# # execute and commit query
# cursor.execute(query)
# cnx.commit()

# # If all goes well, we should reach this print statement
# print("Done with query")

    
cursor.close()
cnx.close()
