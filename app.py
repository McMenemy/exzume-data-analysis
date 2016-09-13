# dev default config: local port is http://127.0.0.1:5000/
# run $ export FLASK_DEBUG=1 to watch for changes locally

# dev externally visible server:
#   $ python app.py
#   run $ flask run --host=0.0.0.0
#   local port is http://0.0.0.0:5000/

import os
from flask import Flask, request, jsonify
import json
import pandas as pd
from pandas import DataFrame

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

print(os.environ['APP_SETTINGS'])

@app.route('/', methods=['POST','GET'])
def correlate():
    # expects JSON in form {data: [{f1: value, f2: value}, {f1: value, f2: value}, ....]}
    data_dictionary = json.loads(request.data.decode('utf-8'))
    data = json.loads(data_dictionary['data'])
    df = pd.DataFrame(data)
    return json.dumps(df.corr().iloc[0]['f2'])

if __name__ == '__main__':
    app.run(host='0.0.0.0')

