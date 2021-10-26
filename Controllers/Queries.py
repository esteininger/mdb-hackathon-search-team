from flask import Blueprint, render_template, make_response, redirect


mod = Blueprint('query_routes', __name__)

@app.route('/synonyms', methods=['GET'])
def synonyms():
    pass


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', default=None, type=str)
    path = request.args.get('path', default='plot', type=str)
    synonym_collection = request.args.get('industry', default='finance', type=str)

    agg_pipeline = [
        {
            '$search': {
                'index': 'default',
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
