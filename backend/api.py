import flask
import os
from flask_cors import CORS, cross_origin
from flask import jsonify
app = flask.Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@cross_origin()
@app.route('/api/domain/<domain>', methods=['GET'])
def show_user_profile(domain):
    print(domain)
    return jsonify(domain)

app.run()