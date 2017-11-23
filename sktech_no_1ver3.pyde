x = 100
speed = 5
def setup():
    size(400, 400)

def draw():
    global x
    global speed
    x += speed
    if x == 400:
        speed = -speed
        # or speed += -1
    elif x < 0:
        speed = 5 

    background(255)
    noStroke()
    fill(196, 147, 173)  # (red, blue, green)
    ellipse(x, 100, 40, 40)  # (x, y, width, height)
