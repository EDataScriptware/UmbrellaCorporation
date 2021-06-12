import json
from flask import jsonify

def selectQueryToJSON(sqlObject):
    list_of_dicts = {'result': [dict(record.items()) for record in sqlObject]}
    dictObject = {'total_model': len(list_of_dicts['result'])}
    
    dictObject.update(list_of_dicts)
    
    return jsonify(dictObject)
