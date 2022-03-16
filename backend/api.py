from cProfile import run
from re import sub
from tabnanny import check
from unittest import result
import flask
import subprocess
from flask_cors import CORS, cross_origin
from flask import jsonify
import json

import os
import vt
 

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

@app.route('/api/pseudo/<pseudo>', methods=['GET'])
def show_pseudo(pseudo):
    print("--------------------------------")
    print(pseudo)
    command = f"cd sher && py -m sherlock.py {pseudo}"
    ret = subprocess.run(command, capture_output=True, shell=True)
    print(ret.stdout.decode())
    print("--------------------------------")
    
    return jsonify(ret.stdout.decode())
    
@app.route('/api/email/<email>', methods=['GET'])
def find_by_mail(email):
    command = f"cd email && python3 ghunt.py email {email}"
    print("--------------------------------")
    print(command)
    result = os.popen(command).read()
    print("-----\"---------------------------")
    result_file = f"./email/result_{email.split('@')[0]}.json"
    f = open(result_file, encoding='utf-8')
    return json.dumps(f.read(), ensure_ascii=False).encode('utf8')

@app.route('/api/vt/<url>', methods=['GET'])
def virus_total(url):
    client_vt = vt.Client("e6716487ed3dab6fd9dc6ff6ad3508c5fd56ca69fbb2b4e1972dceed4e70d4a4")
    analysis = client_vt.scan_url(url,  wait_for_completion=False)
    print("--------------------------------")
    result = client_vt.get_object(f'/analyses/{analysis.id}')
    print(str(result.to_dict()))
    print("--------------------------------")
    return jsonify(result.to_dict())

app.run()
