import os
import pymongo

app_config = {
    'ROOT_PATH': os.path.dirname(os.path.abspath(__file__))
}

mongo_config = {
    'IP': '',
    'PORT': 1,
    'USERNAME': '',
    'PASSWORD': '',
    'DB': '',
    'AUTH': ''
}

client = pymongo.MongoClient("mongodb+srv://cinnamon:cinnamon@sa-shared-demo.lbvlu.mongodb.net/cinnamonSynonyms?retryWrites=true&w=majority")
db = client.cinnamon
