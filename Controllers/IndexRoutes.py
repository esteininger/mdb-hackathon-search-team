from flask import request, Blueprint, render_template, make_response, redirect
from Models.introspect import get_schemas_set
from Utilities.IndexBuilder import buildIndex
import requests
from requests.auth import HTTPDigestAuth
import json
from config import db

mod = Blueprint('index_routes', __name__)


@mod.route('/index-creation', methods=['POST', 'GET'])
def index():
    # update index here
    if request.method == 'POST':
        data_schema = request.get_json()
        indexName = request.args.get('indexName', default=None, type=str)
        print( "Index Name parameter: ", indexName )
        i = buildIndex(indexName, data_schema)
        print(i)
        createAtlasSearchIndex( i )
        db.config.delete_many({})
        db.config.insert(data_schema)
        return 'ok'

def createAtlasSearchIndex( index ):
    url = "https://cloud.mongodb.com/api/atlas/v1.0/groups/5e8f8268d896f55ac04969a1/clusters/SA-SHARED-DEMO/fts/indexes?pretty=true"

    # payload = "{  \"collectionName\": \"calls\",   \"database\": \"rochaDB\",  \"mappings\": {  \"dynamic\": false, \"fields\": { \"sentence\": {\"type\":\"string\"}  }}, \"name\": \"charlieIndex02\", \"synonyms\": [ { \"name\": \"mySynonyms\", \"source\": { \"collection\": \"rocha_synonyms\" }, \"analyzer\": \"lucene.standard\"  } ]  }"
    # payload = {
    #     "collectionName": "calls",
    #     "database": "rochaDB",
    #     "mappings": {  "dynamic": False,
    #     "fields": { "sentence": {"type":"string"}  }},
    #     "name": "charlieIndex03",
    #     "synonyms": [ { "name": "mySynonyms",
    #                     "source": { "collection": "rocha_synonyms" },
    #                     "analyzer": "lucene.standard"  } ]
    # }
    test = [
		{'addToSearchIndex': True, 'dataType': 'string', 'fieldIdentifier': 'versionId'},
		{'addToSearchIndex': True, 'dataType': 'string', 'fieldIdentifier': 'uniqueAggregatorId'},
		{'addToSearchIndex': True, 'dataType': 'number', 'fieldIdentifier': 'uniquePartnerId'}
	]

    jsonPayload = json.dumps( index )
    print( "JSON index spec: ", jsonPayload )

    headers = {
        'Content-Type': 'application/json'
    }
    pub_key = "xgcaookk"
    priv_key = "7500db82-2e47-4eeb-a4dc-139866851c04"

    # response = requests.request("POST", url, headers=headers, data=payload)
    response = requests.post(url, data=jsonPayload, headers=headers, auth=HTTPDigestAuth(username=pub_key, password=priv_key))
    print(response.text.encode('utf8'))

    #
    # # get data dictionary
    # if request.method == 'GET':
    #     # industry = request.args.get('industry_name', default=None, type=str)
    #     get_schemas_set(sample_size=100)
    #
    #     return 'ok'


def main():
    url = "https://cloud.mongodb.com/api/atlas/v1.0/groups/5e8f8268d896f55ac04969a1/clusters/SA-SHARED-DEMO/fts/indexes?pretty=true"
    indexName = "charlieIndex04"

    # payload = "{  \"collectionName\": \"calls\",   \"database\": \"rochaDB\",  \"mappings\": {  \"dynamic\": false, \"fields\": { \"sentence\": {\"type\":\"string\"}  }}, \"name\": \"charlieIndex02\", \"synonyms\": [ { \"name\": \"mySynonyms\", \"source\": { \"collection\": \"rocha_synonyms\" }, \"analyzer\": \"lucene.standard\"  } ]  }"
    # payload = {
    #     "collectionName": "calls",
    #     "database": "rochaDB",
    #     "mappings": {  "dynamic": False,
    #     "fields": { "sentence": {"type":"string"}  }},
    #     "name": "charlieIndex03",
    #     "synonyms": [ { "name": "mySynonyms",
    #                     "source": { "collection": "rocha_synonyms" },
    #                     "analyzer": "lucene.standard"  } ]
    # }
    test = [
		{'addToSearchIndex': True, 'dataType': 'string', 'fieldIdentifier': 'versionId'},
		{'addToSearchIndex': True, 'dataType': 'string', 'fieldIdentifier': 'uniqueAggregatorId'},
		{'addToSearchIndex': True, 'dataType': 'number', 'fieldIdentifier': 'uniquePartnerId'}
	]

    payload = buildIndex( indexName, test )
    jsonPayload = json.dumps( payload )

    headers = {
        'Content-Type': 'application/json'
    }
    pub_key = "xgcaookk"
    priv_key = "7500db82-2e47-4eeb-a4dc-139866851c04"

    # response = requests.request("POST", url, headers=headers, data=payload)
    response = requests.post(url, data=jsonPayload, headers=headers, auth=HTTPDigestAuth(username=pub_key, password=priv_key))
    print(response.text.encode('utf8'))
