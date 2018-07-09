#!/usr/bin/env python
# coding:utf-8

from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    data = {
        "username": 'test',
        "password": '123456',
        "testuser":'yzw'
    }
    return jsonify(**data)
    
    

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=80)
