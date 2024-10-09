from pymongo import MongoClient

client = MongoClient()
mydb = client.obcblog
mycol = mydb.posts

post1 = {
    "title": "FastApi",
    "category": "Backend",
    "author": {
        "name": "Anderson",
        "email": "anderson@email.com"
    },
}

result = mycol.insert_one(post1)
print("Documendo incluído com sucesso!")