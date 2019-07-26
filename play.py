# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import mahjong
from mahjong import Type, Dragon, Wind, Round, Tile, Player
import numpy
import random


#################################################
# Flask Setup
#################################################
#app = Flask(__name__,
#            static_url_path='',
#           static_folder='static')
app = Flask(__name__)

bamboo =[]
bamboo.append('static/images/stick_1.PNG')
bamboo.append('static/images/stick_2.PNG')
bamboo.append('static/images/stick_3.PNG')
bamboo.append('static/images/stick_4.PNG')
bamboo.append('static/images/stick_5.PNG')
bamboo.append('static/images/stick_6.PNG')
bamboo.append('static/images/stick_7.PNG')
bamboo.append('static/images/stick_8.PNG')
bamboo.append('static/images/stick_9.PNG')

character =[]
character.append('static/images/man_1.PNG')
character.append('static/images/man_2.PNG')
character.append('static/images/man_3.PNG')
character.append('static/images/man_4.PNG')
character.append('static/images/man_5.PNG')
character.append('static/images/man_6.PNG')
character.append('static/images/man_7.PNG')
character.append('static/images/man_8.PNG')
character.append('static/images/man_9.PNG')

dot =[]
dot.append('static/images/circle_1.PNG')
dot.append('static/images/circle_2.PNG')
dot.append('static/images/circle_3.PNG')
dot.append('static/images/circle_4.PNG')
dot.append('static/images/circle_5.PNG')
dot.append('static/images/circle_6.PNG')
dot.append('static/images/circle_7.PNG')
dot.append('static/images/circle_8.PNG')
dot.append('static/images/circle_9.PNG')


wind = []
wind.append('static/images/east.PNG')
wind.append('static/images/south.PNG')
wind.append('static/images/west.PNG')
wind.append('static/images/north.PNG')
dragon = []
dragon.append('static/images/center.PNG')
dragon.append('static/images/fortune.PNG')
dragon.append('static/images/paa.PNG')

flower = []
season = []
flower.append('static/images/flowera_1.PNG')
flower.append('static/images/flowera_2.PNG')
flower.append('static/images/flowera_3.PNG')
flower.append('static/images/flowera_4.PNG')
season.append('static/images/flowerb_1.PNG')
season.append('static/images/flowerb_2.PNG')
season.append('static/images/flowerb_3.PNG')
season.append('static/images/flowerb_4.PNG')

tile_category = ["bamboo", "dot", "character", "wind", "dragon","flower", "season"]
current_round = Round()


 
# create route that renders index.html template
@app.route("/")
def home():
    
    info =[]
    revealed_list = []
    list = []
    first = 'first'
    loop = True
    
#    while (loop==True):
        

  
    info.append('East')  # 0 - round - wind:east, south, west, north
    info.append('East')  # 1 - seat
    info.append('East')  # 2 - who is the dealer
    image = " "
    info.append(image)   # 3 - just discarded by 
    info.append('South') # 4 by whom 
    info.append(first)   # 5 - first round?
    roll = random.randrange(3, 19)
    info.append(roll)   # 6 - first round?
    current_round = Round()
    start = current_round.crack(roll)
    current_round.deal()
    current_round.deal_flowers()
    current_round.print_player_hands()
    t = 0
    r = 0
    t_id = 'tile'
    r_id = 'revealed'
    list=[]
    print('from play.py')
    if (info[1] == 'East'):
       for tile in current_round.east.hand:
        real_value = tile.value - 1 
        print('real_value : ', real_value)
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
    
        
    print('list :', list)        
    print('revealed_list :', revealed_list)        
    print('info :', info)        
        
    return render_template("play.html", list= list, revealed_list = revealed_list, info=info)


@app.route("/discard/<discard_tile>")
def discard(discard_tile):
    
    print('discard tile:', discard_tile)
    discard(self, seat, discard_tile)
    
    return redirect("/", code=302)
'''    
@app.route("/crack/<roll>")
def crack(roll):
    roll_nbr = int(roll)
    start = current_round.crack(roll_nbr)
    current_round.deal()
    current_round.deal_flowers()
    current_round.print_player_hands()
    
    return jsonify(current_round.east.hand)
'''

if __name__ == "__main__":
    app.run()
