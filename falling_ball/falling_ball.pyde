"""
Create a dodging game.
Ellipses will start at the top of the screen and 
fall downwards. 
The Player controls the movement of an ellipse 
at the bottom of the screen using the mouse.
The player must dodge the falling ball
Steps:
    1. Create an ellipse with its own 
    position variables. Draw it in the draw() function
    This will be the falling ball.
    2. Make this ball "fall" by giving it a y-speed.
    Update its location in the draw() function.
    Also give it an x-speed, but keep it at 0
    (unless you want to mess around a bit).
    3. When the ball hits the bottom of the screen,
    reset its position to the top of the window.
    You can assign the x-position to a random value.
    Maybe even assign the y-speed to a random value 
    as well. Also, possibly create a second falling 
    ball.
    4. Create the PLAYER ellipse with its own position
    variables. The position of the PLAYER will update
    every draw loop. In the draw loop, bind the 
    x-location variable to the mouseX variable.
    Keep this ball at the bottom of the screen. 
    Draw this ball in the draw() function.
    This will be the player.
    5. In the draw() function determine if the two
    ellipses are touching:
        a) Use pythagorean theorem to find out the 
        distance (hypotenuse) between the two origins.
        b) check to see if the distance is less than 
        the two ellipse radii. (Radiuses)
"""
ball_pos = PVector(200, 570)
def setup():
    size(400, 600)
    
def draw():
    ellipse(ball_pos.x, ball_pos.y, 50, 50)
    #colorthemegenerator
    https://coolors.co/edae49-d1495b-00798c-30638e-003d5b
    https://coolors.co/efefef-3454d1-34d1bf-070707-d1345b