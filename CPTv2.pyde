# shooting game about a treasure lost in space
# https://www.youtube.com/user/shiffman
# link used for treasure chest is too long (Pep 8)
# however it is required so please ignore it. Thank you!!

# variables
score = 0
playerSize = 40
playerPos = PVector(180, 0)

missilePos = PVector(200, 200)
missileSpeed = PVector(10, 0)

mobPos = PVector(950, 200)
mobSize = 50
mobSpeed = PVector(-5, 0)

playerHP = 10
chestHP = 3
url = "http://clipartix.com/wp-content/uploads/2016/07/Treasure-chest-clipart-clipart.gif"
webImg = loadImage(url, "gif")


def setup():
    size(1000, 600)


def draw():
    # globals
    global score
    global playerSize
    global playerPos
    global missilePos
    global missileSpeed
    global mobPos
    global mobSize
    global mobSpeed
    global playerHP
    global chestHP
    global url
    global webImg

    # background
    background(255)
    beginning = color(1, 5, 32)
    ending = color(45, 135, 255)

    for i in range(801):
        stroke(lerpColor(beginning, ending, i/600.0))
        line(0, i, width, i)

    # title & score
    textSize(25)
    fill(255)
    text("Pew Pew!!!", 465, 50)
    text("score:", 845, 50)
    text(score, 930, 50)

    # health points
    text("Player's HP:     / 10", 760, 90)
    text("Chest's HP:    / 3", 760, 130)
    text(playerHP, 903, 90)
    text(chestHP, 903, 130)

    # stars
    strokeWeight(2)
    stroke(255)
    point(500, 400)
    point(300, 200)
    point(100, 300)
    point(600, 100)
    point(700, 250)
    point(430, 230)
    point(150, 60)
    point(360, 470)
    point(50, 140)
    point(230, 350)
    point(750, 430)
    point(150, 450)
    point(365, 320)
    point(600, 300)
    point(650, 550)

    # treasure chests, use "Using For Loops to Make Multiple Objects"
    # image(webImg, 20, 300)
    # webImg.resize(100, 50)
    for y in range(20, 700, 100):
        image(webImg, 20, y)
        webImg.resize(100, 50)

    # player
    playerPos.y = mouseY
    stroke(255, 112, 91)
    strokeWeight(5)
    noFill()
    ellipse(playerPos.x, playerPos.y, playerSize, playerSize)

    # missiles
    stroke(255, 81, 54)
    rect(missilePos.x, missilePos.y, 50, 20)
    missilePos.add(missileSpeed)
    if missilePos.x > width:
        missilePos.x = 200
        missilePos.y = mouseY - 10

    # mobs
    stroke(146, 255, 48)
    ellipse(mobPos.x, mobPos.y, mobSize, mobSize)
    mobPos.add(mobSpeed)
    if mobPos.x == 0:
        mobPos.x = 950
        mobPos.y = random(100, 500)

    # missle detection for mobs if hit
    distance = PVector.sub(missilePos, mobPos)
    if distance.mag() <= mobSize:
        mobPos.x = 950
        mobPos.y = random(100, 500)

    # collision detection for when player gets hit by mob
    dis = PVector.sub(playerPos, mobPos)
    if dis.mag() <= playerSize:
        playerHP -= 1
    if playerHP <= 0:
        textSize(40)
        fill(255)
        text("GAME OVER~ :C", 350, 300)

# Game-help
def keyPressed():
    framerate = PVector(60, 0)
    if keyPressed and (key == "h") == True:
        frameRate(framerate.x)
        fill(0)
        textSize(15)
        help = """
             Game Help:
             1. The player is the red ball (your bullets are depicted as red rectangles) and enemies are green balls
             2. You have automatic bullets, move your mouse up or down to direct the missiles
             3. Objective: Use these missiles to defeat the missiles and protect the treasure chest
             4. There are 3 stages in total, defeat the mob wave and a mini boss to continue
             5. If you or the treasure chest gets hit, HP goes down. If HP hits 0 you lose.
             6. After 3 stages you reach the spaceship and the game is cleared.
             """
        text(help, 75, 350)
