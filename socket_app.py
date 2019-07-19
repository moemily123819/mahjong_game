# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
from flask_socketio import SocketIO, join_room, emit



#################################################
# Flask Setup
#################################################
app = Flask(__name__)

socketio = SocketIO(app)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('socket_index.html')

@socketio.on('my event')
def test_message(message):
    emit('my response', {'data': 'got it!'})

if __name__ == '__main__':
    socketio.run(app)
#ROOMS = {} # dict to track active rooms


#@socketio.on('create')

#def on_create(data):

#    """Create a game lobby"""

#    gm = game.Info(

#        size=data['size'],

#        teams=data['teams'],

#        dictionary=data['dictionary'])

#    room = gm.game_id

#    ROOMS[room] = gm

#    join_room(room)

#    emit('join_room', {'room': room})



if __name__ == "__main__":
#    app.run()
   socketio.run(app, debug=True)
