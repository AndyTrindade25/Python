from pymongo import MongoClient

client = MongoClient()

mydb = client.obcblog
mycol = mydb.posts

result = mycol.find()

for r in result: 
    print(r)