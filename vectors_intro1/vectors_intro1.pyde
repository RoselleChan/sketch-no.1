# Vectors!!!!
# 1. Create variables for a ball that moves 
# You need a x-position, x-position
# also a x-speed and y-speed variable
# no need for a draw loop for now.

position = PVector(50, 50)
speed = PVector(5, 10)

def setup():
    frameRate(40)
    size(600, 600)
    background(255)
    beginning = color(246, 147, 89)#(5, 5, 99)
    ending = color(246, 48, 89)#(5, 201, 187)
    
    for i in range(601):
        stroke(lerpColor(beginning, ending, i/100.0))
        line(0, i, width, i)

    
def draw():
    global position
    global speed
    
    position.add(speed)

    background(255)
    ellipse(position.x, position.y, 30, 30)
    if position.x >= width:
        speed.x += -1
    if position.x <= 0:
        speed.x += 1
    if position.y >= height:
        speed.y += -1
    if position.y <= 0:
        speed.y += 1
