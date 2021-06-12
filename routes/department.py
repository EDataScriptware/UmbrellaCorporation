from services import databaseAPI
from business.jsonTransformer import selectQueryToJSON
import json
from flask import jsonify, request, Flask

def getDepartmentRoutes(app):
    @app.route('/departments', methods=['GET'])
    def getDepartments():
        jsonObject = selectQueryToJSON(databaseAPI.getAllDepartment())
        return jsonObject

    @app.route('/department/<identification>', methods=['GET'])
    def getSpecificDepartment(identification):
        jsonObject = selectQueryToJSON(databaseAPI.getSpecificDepartment(identification))
        return jsonObject
        
    @app.route('/departments', methods=['POST'])
    def populateDepartments():
        databaseAPI.populateDepartments()
        return("Department Table populated.")

    @app.route('/department', methods=['POST'])
    def createDepartment():
        record = json.loads(request.data)

        databaseAPI.createDepartment(record)
        return(str("Department " + str(record['dept_name']) + " has been successfully entered."))


    @app.route('/department/<identification>', methods=['DELETE'])
    def deleteDepartment(identification):
        databaseAPI.deleteDepartment(identification)
        return("dept_id " + identification + " successfully deleted.")

    @app.route('/departments', methods=['DELETE'])
    def deleteDepartments():
        databaseAPI.deleteDepartments()
        return("Department Table wiped.")

    @app.route('/department/<identification>', methods=['PUT'])
    def updateDepartment(identification):
        record = json.loads(request.data)
        databaseAPI.updateDepartment(identification, record)

        return(str("Department " + str(record['dept_name']) + " has been successfully updated."))
