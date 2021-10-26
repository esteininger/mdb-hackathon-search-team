from config import db


def get_sample_data(collection):
    pipeline = [{"$sample": {"size": 10}}]
    cursor = collection.aggregate(pipeline)
    for doc in cursor:
        for key in doc:
            print(key)
            print(type(doc[key]))

get_sample_data(db.bankingRewards_sampleData)