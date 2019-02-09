diameter = 80
mouth = 45 # open mouth
mSpeed = -3
angle = 0
xSpeed = 1
ySpeed = 1

def setup(): 
    global px, py
    size(800, 600)
    px = width/2
    py = height/2

def draw():
    global mouth, mSpeed, py, px, ySpeed
    background(0)

    fill(255, 255, 0)
    textSize(24)
    text("px=" + str(mouth), width/2, height/4)
    text("mSpeed=" + str(mSpeed), width/2, height/4 + 20)
    text("angle=" + str(angle), width/2, height/4 + 40)

    translate(px, py)
    rotate(radians(angle))
    arc(0, 0, diameter, diameter, radians(mouth), radians(360 - mouth))
    
    #mouth animation
    mouth += mSpeed
    if (mouth <= 0 or mouth >= 45):
        mSpeed *= -1
    
    # uptade pacman's position
    if (angle == 0 or angle == 180):
        px += xSpeed
    else:
        py += ySpeed
    
    # check boundry 
    if (px + 40 > width):
        px = width - 40
    if (px - 40 < 0):
        px = 40
    
    
            

def keyPressed():
    global angle, xSpeed, ySpeed
    if (keyCode == RIGHT):
        angle = 0
        xSpeed = 1
    elif (keyCode == DOWN):
        angle = 90
        ySpeed = 1
        
    elif (keyCode == LEFT):
        angle = 180
        xSpeed = -1
    elif (keyCode == UP):
        angle = 270 
        ySpeed = -1
        
