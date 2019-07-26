# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import numpy

#################################################
# Flask Setup
#################################################
#app = Flask(__name__,
#            static_url_path='',
#           static_folder='static')
app = Flask(__name__)

sticks =[]
sticks.append('images/stick_1.PNG')
sticks.append('images/stick_2.PNG')
sticks.append('images/stick_3.PNG')
sticks.append('images/stick_4.PNG')
sticks.append('images/stick_5.PNG')
sticks.append('images/stick_6.PNG')
sticks.append('images/stick_7.PNG')
sticks.append('images/stick_8.PNG')
sticks.append('images/stick_9.PNG')

mans =[]
mans.append('images/man_1.PNG')
mans.append('images/man_2.PNG')
mans.append('images/man_3.PNG')
mans.append('images/man_4.PNG')
mans.append('images/man_5.PNG')
mans.append('images/man_6.PNG')
mans.append('images/man_7.PNG')
mans.append('images/man_8.PNG')
mans.append('images/man_9.PNG')

circles =[]
circles.append('images/circle_1.PNG')
circles.append('images/circle_2.PNG')
circles.append('images/circle_3.PNG')
circles.append('images/circle_4.PNG')
circles.append('images/circle_5.PNG')
circles.append('images/circle_6.PNG')
circles.append('images/circle_7.PNG')
circles.append('images/circle_8.PNG')
circles.append('images/circle_9.PNG')


winds = []
winds.append('images/east.PNG')
winds.append('images/south.PNG')
winds.append('images/west.PNG')
winds.append('images/north.PNG')
winds.append('images/center.PNG')
winds.append('images/fortune.PNG')
winds.append('images/paa.PNG')

flowers = []
flowers.append('images/flowera_1.PNG')
flowers.append('images/flowera_2.PNG')
flowers.append('images/flowera_3.PNG')
flowers.append('images/flowera_4.PNG')
flowers.append('images/flowerb_1.PNG')
flowers.append('images/flowerb_2.PNG')
flowers.append('images/flowerb_3.PNG')
flowers.append('images/flowerb_4.PNG')




 
# create route that renders index.html template
@app.route("/")
def home():
    i=0
    id = 'drag0'+str(i)
    list=[]
    image = "static/"+winds[0]
    list.append([id, image])
    i+=1
    id = 'drag0'+str(i)
    list.append([id, image])
    i+=1
    id = 'drag0'+str(i)
    list.append([id, image])
    image = "static/"+winds[6]
    i+=1
    id = 'drag0'+str(i)
    list.append([id, image])
    i+=1
    id = 'drag0'+str(i)
    list.append([id, image])
    image = "static/"+circles[0]
    i+=1
    id = 'drag0'+str(i)
    list.append([id, image])
    image = "static/"+circles[1]
    i+=1
    id = 'drag0'+str(i)
    list.append([id, image])
    image = "static/"+circles[2]
    i+=1
    id = 'drag0'+str(i)
    list.append([id, image])
    image = "static/"+circles[4]
    i+=1
    id = 'drag0'+str(i)
    list.append([id, image])
    i+=1
    id = 'drag'+str(i)
    list.append([id, image])

  
    i=0
    id = 'revealed0'+str(i)
    revealed_list=[]
    image = "static/"+winds[4]
    revealed_list.append([id, image])
    i+=1
    id = 'revealed0'+str(i)
    revealed_list.append([id, image])
    i+=1
    id = 'revealed0'+str(i)
    revealed_list.append([id, image])
    
    info =[]
    info.append('East')
    info.append('South')
    info.append('North')
    image = "static/"+winds[6]
    info.append(image)
    info.append('first')

    return render_template("game.html", list= list, revealed_list = revealed_list, info=info)


@app.route("/discard/<discard_tile>")
def discard(discard_tile):
    
    print('discard tile:', discard_tile)
    discard(self, seat, discard_tile)
    
    return redirect("/", code=302)
    
@app.route("/crack/<roll>")
def crack(roll):
    
    start = crack(roll)
    return redirect("/", code=302)
    
    
    



if __name__ == "__main__":
    app.run()
