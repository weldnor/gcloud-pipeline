import os

from flask import Flask

VERSION = '1.0'

app = Flask(__name__)


@app.get('/')
def hello():
    return f'hi! version: {VERSION}'


if __name__ == '__main__':
    port = int(os.environ.get("PORT"))
    app.run(host='0.0.0.0', port=port)
