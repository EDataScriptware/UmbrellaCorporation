import databaseAPI

def getRoutes(app):
    @app.route('/getAllEmployees', methods=['GET'])
    def getEmployees():
        return str(databaseAPI.getAllEmployees())

    @app.route('/getSpecificEmployee/<identification>', methods=['GET'])
    def getSpecificEmployee(identification):
        return str(databaseAPI.getSpecificEmployee(identification))


