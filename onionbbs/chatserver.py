from flask import Flask
from flask import Response
from flask import Request
from flask import abort
from flask import g


class Chat:
    def __init__(self):
        self.messages = []
        app = Flask(__name__)
        self.app = app
        chat = Chat()

        @app.before_request
        def before_req():
            g.chat = chat

        @app.route('/ping')
        def hello():
            return Response('pong!')

        @app.route('/getchat/<offset>')
        def show_chat(offset):
            if len(self.messages) == 0:
                return self.get()
            try:
                return self.get()[offset]
            except IndexError:
                return abort(500)

        @app.route('/send', methods=['POST'])
        def add_message():
            self.messages.append(Request.data)
            return Response("success")
    def send(self, msg):
        self.messages.append(msg)
    def get(self):
        return '\n'.join(self.messages)
