# UMBRELLA CORPORATION
from flask import Flask, request, jsonify, make_response

from flask_cors import CORS

from routes.general import getRoutes
from routes.employee import getEmployeeRoutes
from routes.department import getDepartmentRoutes

# Uses Flask
app = Flask(__name__)

# Sets up the routes
getRoutes(app)
getEmployeeRoutes(app)
getDepartmentRoutes(app)

if __name__ == "__main__":
    app.run(debug=True)