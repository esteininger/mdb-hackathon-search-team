from flask import request, Blueprint, render_template, make_response, redirect
from Models.ingest import ingest

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
    # Each of our demos need to have it's own namespace to prevent collision
    # namespace = request.args.get('namespace', default=None, type=str)

    # For now, we are just going to have a drop down for industry, e.g. banking
    industry = request.args.get('industry', default=None, type=str)
    print('Industry: ', industry)

    # Since we are only doing a drop down for industry so we'll default the namespace to industry
    namespace = industry

    # Set the data source accordingly
    if industry == "banking":
        datasource = "https://data.cityofnewyork.us/api/views/825b-niea/rows.json"
    elif industry == "healthcare":
        datasource = "https://data.cityofnewyork.us/api/views/825b-niea/rows.json"
    elif industry == "ecommerce":
        datasource = "https://data.cityofnewyork.us/api/views/825b-niea/rows.json"
    else:
        # Default to banking if all else fails
        namespace = "banking"
        datasource = "https://data.cityofnewyork.us/api/views/825b-niea/rows.json"

    ingest.test(datasource, namespace)
    return "true"

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
