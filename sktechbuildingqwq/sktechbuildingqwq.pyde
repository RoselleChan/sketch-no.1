# F6A795
# F67059

def setup():
    size(400, 400)
    
def draw():
    background(255)
    
    #sky
    beginning = color(246, 147, 89)#(5, 5, 99)
    ending = color(246, 48, 89)#(5, 201, 187)
    
    for i in range(401):
        stroke(lerpColor(beginning, ending, i/500.0))
        line(0, i, width, i)
        
    #skyscaper
    noStroke()
    fill(0)
    rect(100, 70, 120, 400)
    
    #windows
    noStroke()
    fill(255)    
    
    for x in range (110, 200, 40):       #(110, +40 makes one column), 40)
        rect(x, 80, 15, 15)
        for y in range(80, 470, 30):     
            #(x-coordinate of top left corner, how many squares added together, space between each square)
            rect(x, y, 15, 15)  
            
#ball moves, variable for x, y and y-speed and x-speed, do not use draw function, understand the math 
#make a chessboard
