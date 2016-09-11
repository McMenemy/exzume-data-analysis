# dev default config: local port is http://127.0.0.1:5000/
# run $ export FLASK_DEBUG=1 to watch for changes locally

# dev externally visible server:
#   $ python app.py
#   run $ flask run --host=0.0.0.0
#   local port is http://0.0.0.0:5000/

import os
from flask import Flask

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

print(os.environ['APP_SETTINGS'])

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/<name>')
def hello_name(name):
        return "Hello {}!".format(name)

if __name__ == '__main__':
            app.run()

# from flask import Flask, request
# app = Flask(__name__)
# 
# import sys
# import pandas as pd
# # from pd import DataFrame
# 
# print('Python version ' + sys.version)
# print('Pandas version ' + pd.__version__)
# 
# @app.route('/', methods=["POST"])
# 
# def correlate():
#     if request.headers['Content-Type'] == 'application/json':
#         print request.data
#     # return request.data
