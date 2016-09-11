# dev default config: local port is http://127.0.0.1:5000/
# run $ export FLASK_DEBUG=1 to watch for changes locally

# dev externally visible server:
#   run $ flask run --host=0.0.0.0
#   local port is http://0.0.0.0:5000/

from flask import Flask, request
app = Flask(__name__)

import sys
import pandas as pd
# from pd import DataFrame

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)

@app.route('/', methods=["POST"])
def correlate():
    print request.data
    return request.data
