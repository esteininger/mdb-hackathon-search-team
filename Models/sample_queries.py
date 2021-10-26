# from Controllers.IndexRoutes import index
import random
from config import db
from Models.introspect import get_schemas_set

schemas = get_schemas_set(db.config)
# print(schemas)

def get_sample_schemas(schemas):
    # schemas = random.sample(schemas, 2)
    #
    project = {"_id": 0}
    queries = []
    for schema in schemas:
        query = {}
        project[schema['fieldIdentifier']] = 1
        query[schema['fieldIdentifier']] = { '$not': {'$eq': None}}
        query[schema['fieldIdentifier']] = {'$not': {'$eq': "NaN"}}
        queries.append(query)
    pipeline = [{'$match': {'$and': queries}}, {'$sample': {'size': 1}}, {'$project': project} ]
    print(pipeline)
    cursor = db.data.aggregate(pipeline)
    for doc in cursor:
        print(doc)

get_sample_schemas(schemas)




# db.data.aggregate([
#    {
#        "$search": {
#            "index": "default",
#            "text": {
#                "query": "a",
#                "synonyms": "synonyms"
#            }
#        }
#    }
# ]);
