from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello Ioet.. :)!!'


if __name__ == '__main__':
    DEBUG = os.environ['DEBUG']
    if DEBUG == 'True':
        app.run(debug=True, host='0.0.0.0',  port=5050)
    else:
        app.run(debug=False, host='0.0.0.0', port=5000)
