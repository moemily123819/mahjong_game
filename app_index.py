from flask import Flask, render_template
from flask_socketio import SocketIO
import mahjong
from mahjong import Type, Dragon, Wind, Round, Tile, Player
import numpy
import random



app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

#user_count=0

#@socketio.on('connect')
#def test_connect():
#    global user_count
#    user_count = user_count + 1
#    print(user_count)

user_count = 0

round_array = ['East', 'South', 'West', 'North']
round_ind = 0

dealer_array = ['East', 'South', 'West', 'North']
dealer_ind = 0

seat = ['Not Now', 'East', 'South', 'West', 'North', 'Not Now']
sid = []

bamboo =[]
bamboo.append('stick_1.PNG')
bamboo.append('stick_2.PNG')
bamboo.append('stick_3.PNG')
bamboo.append('stick_4.PNG')
bamboo.append('stick_5.PNG')
bamboo.append('stick_6.PNG')
bamboo.append('stick_7.PNG')
bamboo.append('stick_8.PNG')
bamboo.append('stick_9.PNG')

character =[]
character.append('man_1.PNG')
character.append('man_2.PNG')
character.append('man_3.PNG')
character.append('man_4.PNG')
character.append('man_5.PNG')
character.append('man_6.PNG')
character.append('man_7.PNG')
character.append('man_8.PNG')
character.append('man_9.PNG')

dot =[]
dot.append('circle_1.PNG')
dot.append('circle_2.PNG')
dot.append('circle_3.PNG')
dot.append('circle_4.PNG')
dot.append('circle_5.PNG')
dot.append('circle_6.PNG')
dot.append('circle_7.PNG')
dot.append('circle_8.PNG')
dot.append('circle_9.PNG')


wind = []
wind.append('east.PNG')
wind.append('south.PNG')
wind.append('west.PNG')
wind.append('north.PNG')
dragon = []
dragon.append('center.PNG')
dragon.append('fortune.PNG')
dragon.append('paa.PNG')


flower = []
season = []
flower.append('flowera_1.PNG')
flower.append('flowera_2.PNG')
flower.append('flowera_3.PNG')
flower.append('flowera_4.PNG')
season.append('flowerb_1.PNG')
season.append('flowerb_2.PNG')
season.append('flowerb_3.PNG')
season.append('flowerb_4.PNG')

tile_category = ["bamboo", "dot", "character", "wind", "dragon","flower", "season"]
current_round = Round()


a_game=False


@app.route('/')
def sessions():
    global user_count
    global seat
    global game_on
    user_count = user_count + 1
    if (user_count > 4):
        print('user exceed limit')
        status = 'N'
        
    else:    
        status = 'Y'
        if (user_count == 4):
            a_game = True
    print('user_count', user_count)
    if (user_count <=4):
        nbr_user = 4 - user_count 

        
    login_status={'nbr_user' : nbr_user,
                  'user_count' : user_count,
                  'seat' : seat[user_count]}    

        
    return render_template('index.html', status=login_status)



def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

    


@socketio.on('user_id')
def handle_user(json, methods=['GET', 'POST']):
    global sid
    sid.append(json['socket_id'])
    socket_id=json['socket_id']
    print('sid', sid)
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)


@socketio.on('game_on')
def game_on(json, methods=['GET', 'POST']):
    global a_game
    global round_ind
    global dealer_ind
    global round_array
    global dealer_array
 
    game_on = json['game_on']
    if (game_on == 'Y'):
        if (a_game == False):
            a_game = True
 
            round_wind = round_array[round_ind]
            dealer = dealer_array[dealer_ind]

            game_info = {'round' : round_wind,
                         'dealer' : dealer_array[dealer_ind]}
            socketio.emit('to_dealer', game_info, room =sid[dealer_ind],  callback=messageReceived)
            

def formatTiles(current_round):
    j = 0
    list=[]
    revealed_list=[]
    
    retrieveTiles(current_round.east.hand, j, list, revealed_list)
    j=j+1
    retrieveTiles(current_round.south.hand, j, list, revealed_list)
    j=j+1
    retrieveTiles(current_round.west.hand, j, list, revealed_list)
    j=j+1
    retrieveTiles(current_round.north.hand, j, list, revealed_list)
    print('tiles were sent!')


def retrieveTiles(current_hand, j, list, revealed_list):
    list=[]
    revealed_list=[]
    t = 0
    t_id = 'tile'
    r_id = 'revealed'
    for tile in current_hand:
        real_value = tile.value - 1 
        if tile.type==4:
           print(Type(tile.type), Dragon(tile.value))
           tile_id = t_id+str(t)  
           list.append([tile_id, dragon[real_value]])
           t = t+1             
        elif tile.type==3:
           print(Type(tile.type), Wind(tile.value))
           tile_id = t_id+str(t)  
           list.append([tile_id, wind[real_value]])
           t = t+1             
        else:
           print(Type(tile.type), tile.value)
           if tile.type==0:
               tile_id = t_id+str(t)  
               list.append([tile_id, bamboo[real_value]])
               t = t+1             
           elif tile.type==1:
               tile_id = t_id+str(t)  
               list.append([tile_id, dot[real_value]])
               t = t+1             
           elif tile.type==2:
               tile_id = t_id+str(t)  
               list.append([tile_id, character[real_value]])
               t = t+1             
           elif tile.type==5:
               tile_id = r_id+str(r)  
               revealed_list.append([tile_id, season[real_value]])
               r = r+1             
           elif tile.type==6:
               tile_id = r_id+str(t)  
               revealed_list.append([tile_id, flower[real_value]])
               r = r+1             
    print('list : ', list)    
    print('revealed : ', revealed_list)    
    game_info = {'list' : list,
                 'revealed_list' : revealed_list}
    socketio.emit('to_player', game_info, room =sid[j],  callback=messageReceived)
            
        
@socketio.on('roll_the_dice')
def roll_the_dice(json, methods=['GET', 'POST']):
    roll = json["roll"]
    dealer = json["dealer"]
    round_wind = json["round"]
    print('roll_the_dice :', roll, dealer, round_wind)
    
    socketio.emit('game_info', json, callback=messageReceived)
       
    current_round = Round()
    start = current_round.crack(roll)
    current_round.deal()
    current_round.deal_flowers()
    formatTiles(current_round)
#    current_round.print_player_hands()
    
#    socketio.emit('to_dealer', game_info, room =sid[dealer_ind],  callback=messageReceived)
    



@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, debug=True)    