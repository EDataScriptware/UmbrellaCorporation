from services import databaseAPI

def getDepartmentRoutes(app):
    @app.route('/departments', methods=['GET'])
    def getDepartments():
        return str(databaseAPI.getAllDepartment())

    @app.route('/department/<identification>', methods=['GET'])
    def getSpecificDepartment(identification):
        return str(databaseAPI.getSpecificDepartment(identification))

    @app.route('/departments', methods=['POST'])
    def populateDepartments():
        databaseAPI.populateDepartments()
        return("Department Table populated.")

    @app.route('/department/<identification>', methods=['DELETE'])
    def deleteDepartment(identification):
        databaseAPI.deleteDepartment(identification)
        return("dept_id " + identification + " successfully deleted.")

    @app.route('/departments', methods=['DELETE'])
    def deleteDepartments():
        databaseAPI.deleteDepartments()
        return("Department Table wiped.")

