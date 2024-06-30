#!/usr/bin/env python3

from flask import Flask, request, current_app

app = Flask(__name__)

@app.route('/')
def index():
    host = request.headers.get('Host')
    appname = current_app.baracks
    return f'''
                <h1>The host for this page is {host}</h1>
                <h2>The name of this application is {appname}</h2>
            '''

if __name__ == '__main__':
    app.run(port=5555, debug=True)
