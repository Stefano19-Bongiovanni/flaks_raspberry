from flask import Flask, render_template, request, send_from_directory
from carControl import setSteer, setMoving, setGear
from sockets import initSocket, emitCarStatus
    
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


socketio = initSocket(app)
#static files
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)



@app.route('/')
def index():
    return render_template('index.html')




@app.route('/api/rotateSteer', methods=['POST'])
def rotateSteerApi():
    setSteer(request.json['angle'])
    return emitCarStatus()
    


    
    








    






if __name__ == '__main__':
    socketio.run(app, debug=True, port=8000)