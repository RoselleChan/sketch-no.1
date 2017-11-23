#beautiful scenery
cloud = 170
speed = 1
def setup():
    size(700, 700)

def draw():
    background(151, 165, 232)
    noStroke()
    
    #sun
    fill(241, 240, 62)  # (red, blue, green)
    ellipse(200, 90, 40, 40)  # (x, y, width, height)
    
    #mountain no.1
    fill(4, 36, 1)
    ellipse(200, 350, 400, 500)
    
    #cloud
    global cloud
    global speed
    cloud += speed
    if cloud == 700:
        speed = -speed
    elif cloud < 0:
        speed = 1
    fill(255)
    ellipse(cloud, 30, 70, 30) #(bigger # to the right, )
    
    #lake
    fill(100, 230, 189)
    lerpColor(230, 189, 1)
    rect(200, 350, 900, 500)

    #gradient how to??
    #https://processing.org/examples/lineargradient.html
    #http://eskipaper.com/images/beautiful-scenery-1.jpg

