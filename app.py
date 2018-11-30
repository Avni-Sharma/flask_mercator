from flask import Flask
import os
import subprocess as sp
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Dockerized'
@app.route('/commands', methods=['GET'])
def command_in_action():
    # print(sp.check_output(["mercator", "."]))
    # return "yes"
    return sp.check_output(["mercator", "/home/avsharma/test/jsl/"])
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5002)
