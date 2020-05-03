# 用來接收消息用的flask api
import time

from flask import Flask, jsonify, request, g

app = Flask(__name__)

Services = None

# GET 取得參數方式有三種：
# 1. request.args.get(‘name’)
# 2. request.values.get(‘name’)
# 3. def index_id(id)
# get /store
# http: // www.example.com / myapplication / page.html?x = y
# request get method
# path             /page.html
# script_root      /myapplication
# base_url         http://www.example.com/myapplication/page.html
# url              http://www.example.com/myapplication/page.html?x=y
# url_root         http://www.example.com/myapplication/
@app.route('/push/<message>', methods=["GET"])
def get_store(message):
    g.request_started = time.time()
    rs = Services.push(message, request)
    return rs

# get /store
@app.route('/', methods=["GET"])
def home():
    return "<h1>ready</h1>"

@app.before_request
def before_request():
    # 開始時間
    g.start = time.time()

@app.after_request
def after_request(response):
    # 結束時間
    query_time = time.time() - g.start
    Services.update_query_time(query_time)
    return response

# POST 取得參數方式有兩種：
# 1. request.form.get(‘username’)
# 2. request.values.get(‘username’)


# if __name__ == "__main__":
#     app.config['JSON_AS_ASCII'] = False
#     app.config["DEBUG"] = True
#     app.run(port=5000, debug=True, host="192.168.0.96")