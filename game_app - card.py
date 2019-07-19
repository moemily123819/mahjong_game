# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

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
flowers.append('images/flowerb_1.PNG')
flowers.append('images/flowera_2.PNG')
flowers.append('images/flowerb_2.PNG')
flowers.append('images/flowera_3.PNG')
flowers.append('images/flowerb_3.PNG')
flowers.append('images/flowera_4.PNG')
flowers.append('images/flowerb_4.PNG')




 
# create route that renders index.html template
@app.route("/")
def home():
    list=[]
    image = "static/"+winds[0]
    list.append(image)
    list.append(image)
    list.append(image)
    image = "static/"+winds[6]
    list.append(image)
    list.append(image)
    image = "static/"+circles[0]
    list.append(image)
    image = "static/"+circles[1]
    list.append(image)
    image = "static/"+circles[2]
    list.append(image)
    image = "static/"+circles[4]
    list.append(image)
    list.append(image)
    list.append(image)
    image = "static/"+circles[6]
    list.append(image)
    image = "static/"+circles[7]
    list.append(image)
    image = "static/"+circles[8]
    list.append(image)
    
    return render_template("game.html", list= list)







if __name__ == "__main__":
    app.run()
