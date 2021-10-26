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
field_template  = { "type" : "string" }

def buildIndex( datadic, template=index_template ):
	# print( datadic )
	# print( datadic.keys() )
	indexdef = copy.deepcopy( template )
	for fieldDef in datadic:
		if fieldDef["addToSearchIndex"] == False: continue
		name = fieldDef["fieldIdentifier"]
		type = fieldDef["dataType"]
		print( name, "->", type )
		field = { name : copy( field_template ) }
		field[name]["type"] = type
		indexdef["mappings"]["fields"][name] = field[name]
	return indexdef

def main():
    print("Hello World!")
    test = [
		{'addToSearchIndex': False, 'dataType': 'string', 'fieldIdentifier': 'versionId'},
		{'addToSearchIndex': False, 'dataType': 'string', 'fieldIdentifier': 'uniqueAggregatorId'},
		{'addToSearchIndex': False, 'dataType': 'number', 'fieldIdentifier': 'uniquePartnerId'}
	]
    print( buildIndex( test )) 
	


if __name__ == "__main__":
    main()
