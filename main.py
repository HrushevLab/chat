from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit


tF = "template/" #template folder
app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")



@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/chat")
def chat():
    return render_template('simplechat.html')


@socketio.on('connect')
def test_connect():
    print('connect successful')
    emit('my response', {'data': 'Connected'})


@socketio.on('disconnect', namespace='/chat')
def test_disconnect():
    print('Client disconnected')

@socketio.on('sendMessage')
def handle_my_custom_event(data):
    print('received args: ' + str(data))
    emit('my response', data, broadcast=True)


if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', debug=True, allow_unsafe_werkzeug=True)