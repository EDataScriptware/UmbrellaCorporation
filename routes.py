import databaseAPI

def getRoutes(app):
    @app.route('/employees', methods=['GET'])
    def getEmployees():
        return str(databaseAPI.getAllEmployees())

    @app.route('/employee/<identification>', methods=['GET'])
    def getSpecificEmployee(identification):
        return str(databaseAPI.getSpecificEmployee(identification))


