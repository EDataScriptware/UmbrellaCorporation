# UMBRELLA CORPORATION
from flask import Flask, request, jsonify, make_response

from flask_cors import CORS

from routes import getRoutes

# Uses Flask
app = Flask(__name__)

# Sets up the routes
getRoutes(app)

if __name__ == "__main__":
    app.run()