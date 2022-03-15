import flask
import os
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



app.run()