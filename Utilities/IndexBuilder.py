###
import copy

index_template = {
    "collectionName": "data",   
    "database": "cinnamon",  
    "name": "<index-name>",
    "analyzer": "lucene.standard",
    "searchAnalyzer": "lucene.standard",
    "mappings": {
        "dynamic": False,
        "fields": {  }
    },
    "synonyms": [
        {
            "name": "synonyms",
            "source": {
                "collection": "synonyms"
            },
            "analyzer": "lucene.standard"
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
	print( "Index name set to: ", indexdef["name"] )
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
