import collections
import json
import pprint as pp
from config import db
import datetime

def get_sample_data(collection, sample_size):
    pipeline = [{"$sample": {"size": sample_size}}]
    cursor = collection.aggregate(pipeline)
    data_sample = []
    for doc in cursor:
        data_sample.append(doc)
    return data_sample


def get_top_level_schemas(data):
    schemas = []
    for doc in data:
        for key in doc:
            value = doc[key]
            if value:
                schema = {}
                value_type = get_data_type(doc[key])
                label = key
                schema['fieldIdentifier'] = label
                schema['dataType'] = value_type
                schema['addToSearchIndex'] = False
                if schema['dataType'] != "UNSUPPORTED":
                    schemas.append(schema)
    return schemas


def get_second_level_schemas(data):
    schemas = []
    for doc in data:
        for key0 in doc:
            value0 = doc[key0]
            # print(value0, type(value0), type(value0) is dict)
            if value0:
                if isinstance(value0, dict):
                    subdoc = value0
                    for key1 in subdoc:
                        value1 = subdoc[key1]
                        schema = {}
                        value_type = get_data_type(value1)
                        label = key0 + "." + key1
                        schema['fieldIdentifier'] = label
                        schema['dataType'] = value_type
                        schema['addToSearchIndex'] = False
                        if schema['dataType'] != "UNSUPPORTED":
                            schemas.append(schema)
                if isinstance(value0, list):
                    for element in value0:
                        if not isinstance(element, dict):
                            schema = {}
                            value_type = get_data_type(value1)
                            label = key0 + "." + key1
                            schema['fieldIdentifier'] = label
                            schema['dataType'] = value_type
                            schema['addToSearchIndex'] = False
                            schema['isArray'] = True
                            if schema['dataType'] != "UNSUPPORTED":
                                schemas.append(schema)
                        else:
                            for key1 in subdoc:
                                value1 = subdoc[key1]
                                schema = {}
                                value_type = get_data_type(value1)
                                label = key0 + "." + key1
                                schema['fieldIdentifier'] = label
                                schema['dataType'] = value_type
                                schema['addToSearchIndex'] = False
                                if schema['dataType'] != "UNSUPPORTED":
                                    schemas.append(schema)
    return schemas


def uniquify(schemas):
    return list(map(dict, set(tuple(sorted(d.items())) for d in schemas)))


def get_data_type(value):
    if isinstance(value, str):
        simplified_type = "string"
    elif isinstance(value, int):
        simplified_type = "number"
    elif isinstance(value, float):
        simplified_type = "number"
    elif isinstance(value, datetime.date):
        simplified_type = "date"
    else:
        simplified_type = "UNSUPPORTED"
    return simplified_type

def get_schemas_set(schemas):
    sample_data = get_sample_data(db.bankingRewards_sampleData, 10)
    schemas_top_level = get_top_level_schemas(sample_data)
    schemas_second_level = get_second_level_schemas(sample_data)
    schemas = schemas_top_level + schemas_second_level
    unique_schemas = uniquify(schemas)
    return unique_schemas


# print("getting data sample")
# sample_data = get_sample_data(db.bankingRewards_sampleData, 10)
#
# print("inspecting schema top level")
# schemas_top_level = get_top_level_schemas(sample_data)
#
# print("inspecting schema second level")
# schemas_second_level = get_second_level_schemas(sample_data)
#
# schemas = schemas_top_level + schemas_second_level
#
# print("Making unique")
# unique_schemas = uniquify(schemas)
# pp.pprint(unique_schemas)