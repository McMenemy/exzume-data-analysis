# dev default config: local port is http://127.0.0.1:5000/
# run $ export FLASK_DEBUG=1 to watch for changes locally

# dev externally visible server:
#   $ python app.py
#   run $ flask run --host=0.0.0.0
#   local port is http://0.0.0.0:5000/

import os
from flask import Flask, request, jsonify
import json
from pandas import DataFrame

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

print(os.environ['APP_SETTINGS'])

@app.route('/', methods=['POST','GET'])
def correlate():
    if request.method == 'POST':
        data_dict = json.loads(request.data.decode('utf-8'))
        return request.data
        # return jsonify(json.loads(request.data.decode('utf-8')))
    elif request.method == 'GET':
        return jsonify(alan='alan')

if __name__ == '__main__':
    app.run(host='0.0.0.0')


# import sys
# import pandas as pd
# # from pd import DataFrame
#
# print('Python version ' + sys.version)
# print('Pandas version ' + pd.__version__)
#
