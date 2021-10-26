from flask import request, Blueprint, render_template, make_response, redirect, jsonify
from Models.ingest import ingest
from Models.introspect import get_schemas_set 
from config import db

mod = Blueprint('query_routes', __name__)

@mod.route('/ingest', methods=['GET'])
def ingestTest():
    print("Testing")
    return "Passed"

@mod.route('/ingest', methods=['POST'])
def ingestPost():
    # This is ideally how we'd do this where the user can specify the custom data source url but for now we are hardcoding via dropdown
    # Grab the custom URL for the data source
    # datasource = request.args.get('datasource', default=None, type=str)

    # For now, we are just going to have a drop down for industry, e.g. banking
    industry = request.args.get('industry', default=None, type=str)
    print('Industry: ', industry)

    # Set the data source accordingly
    if industry == "banking":
        # This is Aaron's generated data with nested structures and such
        # but he only cares about the first 2 levels of depth and not beyond that
        datasource = "https://cinnamon-hackathon-gnbzi-etihf.mongodbstitch.com/bankingRewards_sampleData.json"
    elif industry == "healthcare":
        datasource = "https://data.cityofnewyork.us/api/views/825b-niea/rows.json"
    elif industry == "education":
        datasource = "https://data.cityofnewyork.us/api/views/f6s7-vytj/rows.csv?accessType=DOWNLOAD"
    else:
        # Default to education
        datasource = "https://cinnamon-hackathon-gnbzi-etihf.mongodbstitch.com/test.json"

    ingest.load(datasource)

    # After loading data, now we need to do the data inspection
    return jsonify(get_schemas_set(db.data, 10))

@mod.route('/synonyms', methods=['GET'])
def synonyms():
    return "true"

@mod.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', default=None, type=str)
    path = request.args.get('path', default='plot', type=str)
    synonym_collection = request.args.get('industry', default='finance', type=str)

    agg_pipeline = [
        {
            '$search': {
                'index': 'synonyms',
                'text': {
                    'query': query,
                    'path': path,
                    "synonyms": synonym_collection
                },
                'highlight': { "path": path }
            }
        }
    ]
    docs = list(collection.aggregate(agg_pipeline))
    json_result = json_util.dumps({'docs': docs}, json_options=json_util.RELAXED_JSON_OPTIONS)
    return jsonify(json_result)
