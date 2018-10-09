"""
    Created by Lucky on 2018/10/9 15:48
"""
from flask import Flask

__author__ = "lucky"

app = Flask(__name__)


@app.route('/hello')
def hello():
    return "Hello, Lucky"


# app.add_url_rule("/hello", view_func=hello)

app.run(host='0.0.0.0', debug=True,port='')
