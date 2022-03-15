import flask
import os
import subprocess
from flask_cors import CORS, cross_origin
from flask import jsonify

app = flask.Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

@cross_origin()

@app.route('/api/domain/<domain>', methods=['GET'])
def show_domain(domain):
    test = {
        "domain": domain,
        "yes": "bien"
    }
    print("--------------------------------")
    print(os.popen('ls').read())
    print("--------------------------------")
    return jsonify(test)



@app.route('/api/email/<email>', methods=['GET'])
def find_by_mail(email):
        return "toto"  
    # command = f"cd ../test/ghunt ; py -m ghunt.py {email}" 
    # ret = subprocess.run(command, capture_output=True, shell=True)
 

app.run()