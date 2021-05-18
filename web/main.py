import sys
import os
import json

__dir__ = os.path.dirname(os.path.abspath(__file__))
sys.path.append(__dir__)
sys.path.append(os.path.abspath(os.path.join(__dir__, '../')))

from flask import Flask, request, Response

import tools.infer.predict_system as predict_sys
import tools.infer.utility as utility

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"

@app.route("/analyse", methods=['POST'])
def analyse():
  args = utility.parse_args()
  # 获取图片base64参数
  requestBody = request.json
  args.base64Img = requestBody['base64Img']
  result = predict_sys.analyse_image_web(args)
  return Response(json.dumps(result),  mimetype='application/json')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)