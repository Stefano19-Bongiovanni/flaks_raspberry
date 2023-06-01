

from flask_socketio import SocketIO
from carControl import getCarStatus, setSteer, setGear, setMoving
from flask import request
socketio = SocketIO()

sessions = []

def initSocket(app):
    socketio.init_app(app, cors_allowed_origins="*")
    return socketio



@socketio.on('connect')
def handle_connect():
    return False



@socketio.on('connect', namespace='/ws/carStatus')
def carStatus():
    sessions.append(request.sid)
    print('Client connected carStatus, sid: ', request.sid)
    emitCarStatus()

@socketio.on('disconnect', namespace='/ws/carStatus')
def carStatus():
    sessions.remove(request.sid)
    setMoving(False)
    print('Client disconnected carStatus', request.sid)
    return True

def emitCarStatus():
    carStatus = getCarStatus()
    socketio.emit('carStatus', carStatus, namespace='/ws/carStatus')
    return carStatus

@socketio.on('changeSteer', namespace='/ws/carStatus')
def changeSteer(data):
    success = setSteer(data['angle'])
    if (not success):
        return False
    emitCarStatus()
    return True

@socketio.on('changeGear', namespace='/ws/carStatus')
def changeGear(data):
    success = setGear(data['gear'])
    if (not success):
        return False
    emitCarStatus()
    return True

@socketio.on('changeMoving', namespace='/ws/carStatus')
def changeMoving(data):
    success = setMoving(data['moving'])
    if (not success):
        return False
    emitCarStatus()
    return True