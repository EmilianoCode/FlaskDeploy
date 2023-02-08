from flask import Flask, render_template, redirect
from flask_socketio import SocketIO, emit, join_room
import eventlet

eventlet.monkey_patch()

app = Flask(__name__)
socketio = SocketIO(app)
app.debug = True

@app.route("/", methods=["GET", "POST"])
def hello():

    @socketio.event()
    def saludo(msg):
        print(msg)
        emit("msg", msg, broadcast = True)

    return render_template("index.html")

if __name__ == '__main__':
	socketio.run(app, host="0.0.0.0", port=5000)