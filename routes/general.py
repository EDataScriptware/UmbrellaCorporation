def getRoutes(app):
    @app.route('/', methods=['GET'])
    def getRoot():
        return "Your connection is stable!"