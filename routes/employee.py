from services import databaseAPI
import json
from flask import jsonify, request, Flask

def getEmployeeRoutes(app):
    @app.route('/employees', methods=['GET'])
    def getEmployees():
        return str(databaseAPI.getAllEmployees())

    @app.route('/employee/<identification>', methods=['GET'])
    def getSpecificEmployee(identification):
        return str(databaseAPI.getSpecificEmployee(identification))

    @app.route('/employees', methods=['POST'])
    def populateEmployees():
        databaseAPI.populateEmployees()
        return("Employee Table populated.")

    @app.route('/employee', methods=['POST'])
    def createEmployee():
        record = json.loads(request.data)

        databaseAPI.createEmployee(record)
        return(str("Employee " + record['first_name'] + " " + record['last_name'] + " has been successfully entered."))


    @app.route('/employee/<identification>', methods=['PUT'])
    def updateEmployee(identification):
        record = json.loads(request.data)
        databaseAPI.updateEmployee(identification, record)

        return("emp_id " + identification + " successfully updated.")

    @app.route('/employee/<identification>', methods=['DELETE'])
    def deleteEmployee(identification):
        databaseAPI.deleteEmployee(identification)
        return("emp_id " + identification + " successfully deleted.")

    @app.route('/employees', methods=['DELETE'])
    def deleteEmployees():
        databaseAPI.deleteEmployees()
        return("Employee Table wiped.")
