from flask import Flask
import os
from flask_socketio import SocketIO, emit

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'WELLHEREISTHEPASSWORDFORSECURINGMYAPPLICATION'

app = Flask(__name__)
# app.config.from_object(Config)
socketio = SocketIO(app)

@app.route('/')
def hello():
    return 'Noni'

@socketio.on('connect')
def test_connect():
    emit('after connect',  {'data':'Lets dance'})

if __name__ == '__main__':
    socketio.run(app)
