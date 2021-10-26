###
import copy

index_template = {
    "name": "<index-name>",
    "analyzer": "Standard",
    "searchAnalyzer": "Standard",
    "mappings": {
        "dynamic": False,
        "fields": {  }
    },
    "synonyms": [
        {
            "name": "default_synonyms",
            "source": {
                "collection": "synonym_collection"
            },
            "analyzer": "Standard"
        }
    ]
}
""" 
[ {'addToSearchIndex': False,
   'dataType': 'STRING',
   'fieldIdentifier': 'versionId'} ]
 """

def staticMapping( datadic, target ):
	for fieldDef in datadic:
		if fieldDef["addToSearchIndex"] == False: continue
		name = fieldDef["fieldIdentifier"]
		type = fieldDef["dataType"]
		print( name, "->", type )
		field = { name : { "type" : type } }
		field[name]["type"] = type
		print( field )
		target[name] = field[name]

def buildIndex( indexName, datadic, template=index_template ):
	# print( datadic )
	# print( datadic.keys() )
	indexdef = copy.deepcopy( template )
	indexdef["name"] = indexName
	staticMapping( datadic, indexdef["mappings"]["fields"] )
	return indexdef

def main():
    print("Hello World!")
    test = [
		{'addToSearchIndex': True, 'dataType': 'string', 'fieldIdentifier': 'versionId'},
		{'addToSearchIndex': True, 'dataType': 'string', 'fieldIdentifier': 'uniqueAggregatorId'},
		{'addToSearchIndex': True, 'dataType': 'number', 'fieldIdentifier': 'uniquePartnerId'}
	]
    print( buildIndex( "MyIndex", test )) 
	


if __name__ == "__main__":
    main()
