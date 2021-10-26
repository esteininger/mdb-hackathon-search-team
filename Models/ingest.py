from config import db
import urllib.request
import requests
import json
import pandas as pd
from datetime import datetime, timezone, timedelta

class ingest:
    # def __init__(self):
    #     self.base_url = ''

    def addSynonym(original, synonym):
        print("Add synonym now: ", original, ", " + synonym)
 
        d = db.synonym.find_one({'input': original, 'mappingType': 'explicit'})
        if d:
             print("Synonym doc found. Append synonym")
             d["synonyms"].append(synonym)
             print(d["synonyms"])
             db.synonym.update({'_id': d["_id"]}, {'$push': {'synonyms': synonym}})
        else:
             print("Synonym doc not found")
             db.synonym.insert_one({"mappingType": "explicit", "input": [original], "synonyms": [synonym]})       

    def load(datasource):
        print("Ingest the data source now: ", datasource)

        # First step is we will drop all collections to clean the slate
        print("Dropping data, synonym, and dictionary collections for cleanup")
        db.data.drop()
        db.synonym.drop()
        db.dictionary.drop()
       
        # Track if json vs csv
        # Support json and csv by looking at the extension
        isJson = True
        if '.csv' in datasource:
            isJson = False
            df = pd.read_csv(datasource)
            rows = df.to_dict(orient="records")
        elif '.json' in datasource:
            rows = urllib.request.urlopen(datasource)
 
        # manage bulk inserting
        i = 0
        arr = []

        # start processing now
        for l in rows:
            if isJson:
                d = json.loads(l)
            else:
                d = l

            if i<100: # load up our bulk array
                arr.append(d)
            else: # insert now
                db.data.insert_many(arr)
                arr = [] # reinitialize to start over

        # Final check to see if we have more data
        if len(arr)>0:
           db.data.insert_many(arr)

    def test(datasource):
        print("Ingest Model Test function: ", datasource)
        # Insert a dummy doc into a collection
        db.test.insert_one({"abc":"test"})

