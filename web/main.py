import sys
import os

__dir__ = os.path.dirname(os.path.abspath(__file__))
sys.path.append(__dir__)
sys.path.append(os.path.abspath(os.path.join(__dir__, '../')))

from flask import Flask, request

import tools.infer.predict_system as predict_sys
import tools.infer.utility as utility

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"

@app.route("/analyse", methods=['POST'])
def analyse():
  # print(request.get_json())
  return "<p>Hello, World!</p>"


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)