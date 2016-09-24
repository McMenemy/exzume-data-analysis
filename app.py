# dev default config: local port is http://127.0.0.1:5000/
# run $ export FLASK_DEBUG=1 to watch for changes locally

# dev externally visible server:
#   $ python app.py
#   run $ flask run --host=0.0.0.0
#   local port is http://0.0.0.0:5000/

import os
from flask import Flask, request, jsonify
import json
import simplejson
import pandas as pd
from pandas import DataFrame
from collections import OrderedDict
import scipy
from scipy.stats import pearsonr
# Parameters :
# x : 1D array
# y : 1D array the same length as x
# Returns :
# (Pearson’s correlation coefficient, : 2-tailed p-value)

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

print(os.environ['APP_SETTINGS'])

#change route name to '/correlateTwo'?
@app.route('/correlateTwo', methods=['POST','GET'])
def correlateTwo():
    # expects JSON in form { data: { f1: [val1, val2, ...], f2: [val1, val2, ...]} }
    data_dictionary = json.loads(request.data.decode('utf-8'))
    data = json.loads(data_dictionary['data'])

    df_data = pd.DataFrame(data)
    df_data_clean = df_data.dropna()
    print(df_data)
    print(df_data_clean)
    result = pearsonr(df_data_clean['f1'], df_data_clean['f2'])

    return json.dumps(result)

@app.route('/correlateMany', methods=['POST'])
def correlateMany():
    # expects JSON in form {data: [{f1: value, f2: value}, {f1: value, f2: value}, ....]}
    data_dictionary = json.loads(request.data.decode('utf-8'))
    data = json.loads(data_dictionary['data'])
    print(data)
    df = pd.DataFrame(data)
    df_corr = df.corr()
    print(df)
    print(df_corr)

    num_corr_rows = df_corr.shape[0]
    num_corr_cols = df_corr.shape[1]

    dict = OrderedDict()
    for row in df_corr.itertuples():
        thisRow = []
        for x in range(1, num_corr_cols + 1):
            thisRow.append(row[x])
        dict[row[0]] = thisRow
    return simplejson.dumps(dict, ignore_nan=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
