# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template, request
import requests
app = Flask(__name__)

tasks = {
    'id': '1',
    'usname': 'xiao_yi',
    'message': 'ok',
    'done': True
       } 
 
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        return jsonify(tasks)
    else:
        return "It's not post requests!"
 
if __name__ == '__main__':
    app.run()
