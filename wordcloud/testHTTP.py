from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from flask import Flask,request
# 配置路由
app=Flask(__name__)

@app.route('/')
def hello_wordl():
    return "Hello, world"
# jquerry get 请求
@app.route('/worldCloud')
def worldCloud():
    # 获取参数
    itemid = request.args.get('itemid')
    return itemid

# 直接返回id
@app.route('/worldCloud/<id>')
def world(id):
    return id

if __name__=="__main__":
    app.run()