from flask import Flask, render_template
import os
from flask_socketio import SocketIO, emit
import json

app = Flask(__name__)
# app.config.from_object(Config)
socketio = SocketIO(app)

@app.route('/test')
def hello():
    return 'Noni'

@app.route('/')
def index():
    return render_template('index.html')



def yeilder():
    with open("/home/chand/techneith/projects/joel/socket-flask/static/log/job.log") as log_info:
            data = log_info.readlines()
            yield data

import time
@socketio.on('connect')
def test_connect():
    emit('after connect',  {'data':next(yeilder())})
            

if __name__ == '__main__':
    socketio.run(app)
