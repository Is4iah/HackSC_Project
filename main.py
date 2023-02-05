import os
import openai
import json
import requests
import mysql.connector

    

# make a call to news api for new new
def newsCall():
    API_KEY = "29f05eb0-2754-4686-be13-e563213e5621"
    ALL_URL = f"https://api.goperigon.com/v1/all?apiKey={API_KEY}"
    extra = "&from=2023-02-01&sourceGroup=top10&showNumResults=true&showReprints=false&excludeLabel=Non-news&excludeLabel=Opinion&excludeLabel=Paid News&excludeLabel=Roundup&excludeLabel=Press Release&sortBy=date&excludeSource=foxnews.com&category=Politics&category=Finance&q=Current World Political News"
    extra2 = "&from=2023-02-01&sourceGroup=top10&showNumResults=true&showReprints=false&paywall=false&excludeLabel=Non-news&excludeLabel=Opinion&excludeLabel=Paid News&excludeLabel=Roundup&excludeLabel=Press Release&sortBy=date&excludeSource=foxnews.com&category=Politics&category=Finance&q=Current World Political News"
    ALL_URL += extra2

    resp = requests.get(f"{ALL_URL}")
    return resp.json()

    # extra stuff 
    # article = resp.json()["articles"][0]

    # print(article["title"])


    # dic = {}
    # # print(type(resp.json()["articles"][0]['title']))


    # for article in resp.json()["articles"]:
    #     dic[article["title"]] = article["summary"]
    
def aiCall(summary):
    openai.api_key = "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"

    model_engine = "text-davinci-003"
    prompt="Summarize this in 150 words:\n\n" + summary

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
    # print(response)


    # with open("openAI.txt", "a") as f:
    #     print(prompt + "\n", file = f)  
    #     print("Original: \n", file = f)
    #     print(first_sum + "\n\n", file = f) 
    #     print("OpenAI:\n", file = f)
    #     print(response + "\n\n\n\n", file=f)
    
    return response
  

def insert(id_, authors, title, image, response):
    cnx =mysql.connector.connect(user='admin', password='password',
    host='hacksc.cojn5ewfdu5p.us-west-1.rds.amazonaws.com', database='HackSC')
    cursor = cnx.cursor()
    
    # execute and commit query
    cursor.execute("""INSERT INTO master (`id`, `authors`, `title`, `image`, `response`) 
               VALUES (%s, %s, %s, %s, %s)""", (id_, authors, title, image, response))
    cnx.commit()
    cursor.close()
    cnx.close()
    print("completed query")
    
def getOldNews():
    cnx =mysql.connector.connect(user='admin', password='password',
    host='hacksc.cojn5ewfdu5p.us-west-1.rds.amazonaws.com', database='HackSC')
    cursor = cnx.cursor()
    
    # execute and commit query
    cursor.execute("""SELECT id FROM master""")
    oldNews_temp = list(cursor)
    oldNews = []
    
    for each in oldNews_temp:
        oldNews.append(each[0])
    

    cnx.commit()
    cursor.close()
    
    return oldNews
    
    
    
    
    

def main():
    # make a call to newsAPI and capture the returned json file
    news = newsCall()
    oldNews = getOldNews()
    
    test = False
    # cnt = 0
    
    if not test:
        for article in news["articles"]:
            # check if news article is in database. if it is not, then it is new news!
            if article["articleId"] not in oldNews:
                
                # make a call to openAI to write a summary
                response = aiCall(article["summary"])
                
                # add the article information to SQL database
                id_     = article["articleId"]
                authors = article["authorsByline"]
                title   = article["title"]
                image   = article["imageUrl"]
                
                insert(id_, authors, title, image, response)
            else:
                print("dupe--" + article["articleId"])
            # cnt += 1
            # if cnt > 5:
            #     print("done! CHECK MYSQL")
            #     break
                
            
    else:
        # oldNews = getOldNews()
        
        # print("this is the old news list of id's:")
        # for ids in oldNews:
        #     print(ids)
        
        print("\n\n")
        article = news["articles"][0]
        id_      = article["articleId"]
        authors  = article["authorsByline"]
        title    = article["title"]
        image    = article["imageUrl"]
        response = "temporary response :)"
        
        print("our id: " + id_)
        
        if id_ not in oldNews:
            insert(id_, authors, title, image, response)
        else:
            print("dupe, we dont add it")
            
        
main()