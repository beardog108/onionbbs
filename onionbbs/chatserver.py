from flask import Flask
from flask import Response

app = Flask(__name__)


@app.route('/ping')
def hello():
    return Response('pong!')
