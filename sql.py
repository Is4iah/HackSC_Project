import mysql.connector
import json

# create connection to my SQL
cnx =mysql.connector.connect(user='admin', password='password',
host='hacksc.cojn5ewfdu5p.us-west-1.rds.amazonaws.com', database='HackSC')
cursor = cnx.cursor()


with open('sample.json') as json_file:
    dic = json.load(json_file)
 
    # Print the type of data variable
    # print("Type:", type(dic))
    
# cnt = 0
# for title in dic.keys():
#     print(str(cnt) + ": "+  title + "\n")
#     print(str(cnt) + ": "+ dic[title])
#     cnt += 1


# create variables passed into query
id_     = "70"
authors = "authorsByline"
title   = "Inside Biden's decision to 'take care of' the Chinese spy balloon that triggered a diplomatic crisis"
image   = "imageUrl"
response = "temp"

# create query
# query = "INSERT INTO master (`idmaster`, `question`, `response`) VALUES ('" + id + "', '" + question + "', '" + answer + "');"

# execute and commit query
# cursor.execute(query)
# cnx.commit()

# try 2
# my_string = """INSERT INTO master (`idmaster`, `question`, `response`) VALUES (%s, %s, %s)""", (id, question, answer)

cursor.execute("""INSERT INTO master (`id`, `authors`, `title`, `image`, `response`) 
               VALUES (%s, %s, %s, %s, %s)""", (id_, authors, title, image, response))
cnx.commit()

# print(my_string)
# cursor.execute("""INSERT INTO master (person_id, category, type)
#                    VALUES(%s, %s, %s)""", (number, category, value))



# # If all goes well, we should reach this print statement
print("Done with query")

    
cursor.close()
cnx.close()
