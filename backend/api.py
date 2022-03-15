import flask
import subprocess
from flask_cors import CORS, cross_origin
from flask import jsonify
import json
 

app = flask.Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@cross_origin()

@app.route('/api/domain/<domain>', methods=['GET'])
def show_domain(domain):
    print("--------------------------------")
    command = "cd ./domain ; python3 theHarvester.py -d " + domain + " -l 50 -b all -f " + domain.split('.')[0]
    ret = subprocess.run(command, capture_output=True, shell=True)
    print(ret.stdout.decode())
    print("--------------------------------")

    f = open('./domain/'+ domain.split('.')[0] + '.json')
    data = json.load(f)

    return jsonify(data)

app.run()