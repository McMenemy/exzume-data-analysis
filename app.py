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
    if request.method == 'POST':
        step1 = request.data
        print(step1)
        step2 = request.data.decode('utf-8')
        print(step2)
        # step25 = step2.replace('\\"',"\"")
        # print(step25)
        # step3 = json.dumps(step25)
        # print(step3)
        step4 = json.loads(step2)
        print(step4)
        print('done')
        data_dictionary = json.loads(step2)
        print(data_dictionary['data'])
        d = json.loads(data_dictionary['data'])
        print(d)
        print(d[0])
        df = pd.DataFrame(d)
        print(df)
        print(df.corr())
        print(df.describe())
        print(df.corr().to_json)
        print(df.corr().iloc[0]['f2'])
        return json.dumps(df.corr().iloc[0]['f2'])
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
