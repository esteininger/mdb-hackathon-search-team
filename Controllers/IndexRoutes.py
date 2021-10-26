from flask import request, Blueprint, render_template, make_response, redirect
from Models.introspect import get_schemas_set
from Utilities.IndexBuilder import buildIndex

mod = Blueprint('index_routes', __name__)

@mod.route('/index-creation', methods=['POST', 'GET'])
def index_creation():
    # update index
    if request.method == 'POST':
        data_schema = request.get_json()
        indexName = request.args.get('industry', default=None, type=str)
        i = buildIndex(indexName, data_schema)
        print(i)
        return 'ok'

    #
    # # get data dictionary
    # if request.method == 'GET':
    #     # industry = request.args.get('industry_name', default=None, type=str)
    #     get_schemas_set(sample_size=100)
    #
    #     return 'ok'
