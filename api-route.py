from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import subprocess
from datetime import datetime

app = Flask(__name__)
api = Api(app)

class project(Resource):
    def get(self, env):

        pod= subprocess.check_output("hostname", shell=True)
        pod=(str(pod)[2:-3])

        return jsonify({"Date":str(datetime.now()), "Environment":env, "Pod":pod})
api.add_resource(project, '/<env>')



# driver function
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)