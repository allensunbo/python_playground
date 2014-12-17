from pymongo import MongoClient
import datetime
client = MongoClient()

#client = MongoClient('localhost', 27017)
#client = MongoClient('mongodb://localhost:27017/')

db = client.python_mongo
# db = client['test-database']
#

post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}
posts = db.posts
post_id = posts.insert(post)

def foo():
    return 'hello, world!'
