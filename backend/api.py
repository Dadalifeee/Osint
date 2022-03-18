from cProfile import run
from re import sub
from tabnanny import check
from unittest import result
import flask
import subprocess
from flask_cors import CORS, cross_origin
from flask import jsonify
import json
import re
import os
import vt
 
import httpx

from holehe.modules.social_media.snapchat import snapchat




app = flask.Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@cross_origin()

@app.route('/api/domain/<domain>', methods=['GET'])
def show_domain(domain):
    check = re.search('^(http(s)?://)?[a-zA-Z0-9]+.((fr)|(com))$', domain)
    if check:
        command = "cd ./domain ; python3 theHarvester.py -d " + domain + " -l 50 -b all -f " + domain.split('.')[0]
        subprocess.run(command, capture_output=True, shell=True)
        f = open('./domain/'+ domain.split('.')[0] + '.json')
        data = json.load(f)
        return jsonify(data)
    else:
        return False

@app.route('/api/pseudo/<pseudo>', methods=['GET'])
def show_pseudo(pseudo):
    check = re.search('^[a-zA-Z0-9]\w{1,15}$', pseudo)
    if check:
        command = f"cd sher && python3 sherlock.py {pseudo}"
        ret = subprocess.run(command, capture_output=True, shell=True)
        return jsonify(ret.stdout.decode())
    else:
        return False
    
@app.route('/api/email/<email>', methods=['GET'])
def find_by_mail(email):
    check = re.search('^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$', email)
    if check:
        command = f"cd email && python3 ghunt.py email {email}"
        os.popen(command).read()
        result_file = f"./email/result_{email.split('@')[0]}.json"
        f = open(result_file, encoding='utf-8')
        return json.dumps(f.read(), ensure_ascii=False).encode('utf8')   
    else:
        return False


@app.route('/api/vt/<url>', methods=['GET'])
def virus_total(url):
    check = re.search('^(http(s)?://)?[a-zA-Z0-9]+.((fr)|(com))$', url)
    if check:
        client_vt = vt.Client("e6716487ed3dab6fd9dc6ff6ad3508c5fd56ca69fbb2b4e1972dceed4e70d4a4")
        analysis = client_vt.scan_url(url,  wait_for_completion=False)
        result = client_vt.get_object(f'/analyses/{analysis.id}')
        return jsonify(result.to_dict())
    else:
        return False

@app.route('/api/mail/<mail>', methods=['GET'])
async def mail_holehe(mail):
    check = re.search('^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$', mail)
    if check:
        command = f"cd holehe && holehe {mail}"
        ret = subprocess.run(command, capture_output=True, shell=True)
        return jsonify(ret.stdout.decode())
    else:
        return False;


app.run()
