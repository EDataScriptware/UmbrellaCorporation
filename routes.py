import databaseAPI

def getRoutes(app):
    @app.route('/employees', methods=['GET'])
    def getEmployees():
        return str(databaseAPI.getAllEmployees())

    @app.route('/employee/<identification>', methods=['GET'])
    def getSpecificEmployee(identification):
        return str(databaseAPI.getSpecificEmployee(identification))

    @app.route('/employees', methods=['POST'])
    def populateEmployees():
        databaseAPI.populateEmployees()
        return("Database populated.")

    @app.route('/employee/<identification>', methods=['DELETE'])
    def deleteEmployee(identification):
        databaseAPI.deleteEmployee(identification)
        return("emp_id " + identification + " successfully deleted.")

    @app.route('/employees', methods=['DELETE'])
    def deleteEmployees():
        databaseAPI.deleteEmployees()
        return("Employee table wiped.")
