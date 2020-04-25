# 用來接收消息用的flask api
from flask import Flask, jsonify

app = Flask(__name__)

Services = None

# get /store
@app.route('/push/<message>')
def get_store(message):
    rs = Services.push(message)
    return rs

# get /store
@app.route('/')
def home():
    return "ready"

# if __name__ == "__main__":
#     app.config['JSON_AS_ASCII'] = False
#     app.run(port=5000, debug=True, host="192.168.0.96")