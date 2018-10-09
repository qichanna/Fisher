"""
    Created by Lucky on 2018/10/9 15:48
"""
from flask import Flask, make_response

__author__ = "lucky"

app = Flask(__name__)
app.config.from_object('config')


@app.route('/hello')
def hello():
    headers = {
        'content-type': 'application/json',
        'location': 'http://www.bing.com'
    }
    # response = make_response('<html></html>', 301)
    # response.headers = headers
    return '<html></html>', 301, headers


# app.add_url_rule("/hello", view_func=hello)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)
