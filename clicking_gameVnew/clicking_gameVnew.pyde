"""
Create a 2-player clicking game.
1. Draw an ellipse at a random location on the screen.
2. Store the location info in a variable (PVector?)
3. Define a mousePressed() function. When the user clicks,
   assign a new location to the ball.
4. Create a score variable. When the user clicks (same function above,
   add +1 to the score.
5. Display the score using the text() function.
   https://processing.org/reference/text_.html
6. Now, when the user clicks, use the mouseX and mouseY variables, within the
   previously defined mousePressed() function, compare those values to the 
   location of the ellipse. 
   If the mouse location is within a certain range, then you add to the 
   score and change the ellipse location.
7. Split the board visually in the middle. One side will be for player 1, the
   other for player2. Each will have their own ball to click...
8. Add a second ball, with its own position variable, and its own score, and
   its own click detection in the already defined mousePressed() function.
9. If a player reaches a score of 10, they win. Code this.
"""
p1_pos = PVector(0, 0)
p2_pos = PVector(0, 0)
p1_score = 0
p2_score = 0
winner = None


def setup():
    global p1_pos
    global p2_pos

    size(800, 400)

    global p1_pos
    global p2_pos

    p1_pos.x = random(5, 400)  # (5, 200) states the range
    p1_pos.y = random(5, 400)
    p2_pos.x = random(795, 400)
    p2_pos.y = random(795, 400)

def draw():
    global p1_pos
    global p2_pos
    global p1_score
    global p2_score
    global winner

    background(255)
    textAlign(LEFT)

    # Player 1 board
    fill(5, 9, 89)
    rect(0, 0, 400, 400)
    # ball
    fill(196, 255, 235)
    ellipse(p1_pos.x, p1_pos.y, 50, 50)
    # score
    fill(196, 255, 235)
    textSize(25)
    text("Score: " + str(p1_score), 30, 50)

    # Player 2 board
    fill(196, 255, 235)
    rect(width / 2, 0, width, height)
    # ball
    fill(5, 9, 89)
    ellipse(p2_pos.x, p2_pos.y, 50, 50)
    # score
    fill(5, 9, 89)
    textSize(25)
    text("Score: " + str(p2_score), 400, 50)

def mousePressed():
    global p1_pos
    global p2_pos
    global score

    p1_pos.x = random(5, 400)  # (5, 200) states the range
    p1_pos.y = random(5, 400)

    p2_pos.x = random(795, 400)
    p2_pos.y = random(795, 400)
    score += 1
