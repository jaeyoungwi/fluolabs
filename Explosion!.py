add_library('minim')

beamX = []    # before setup()
beamY = []
shipX = []
shipY = []
speed = 1

gunX = 0
leftPressed = False
rightPressed = False

def setup():
    global zapSound, crashSound
    size(800, 800, P3D)
    minim = Minim(this)                             
    zapSound = minim.loadSample("zap.mp3")   
    crashSound = minim.loadSample("crash.wav")  
           
def draw():
    global gunX
    background(0)
    noFill()
    stroke(255)

    # display info
    text("ships: " + str(len(shipX)), 50, 50)

    if (len(shipY) > 0):
        text("shipX[0]: " + str(shipX[0]), 50, 80)
    if (len(beamY) > 0):
        text("beamX[0]: " + str(beamX[0]), 50, 110)

    translate(width/2, height/2)
    rotateX(radians(45))

    # show space ships
    for i in range(len(shipX)):
        stroke(random(256), random(256), random(256))
        rect(shipX[i], shipY[i], 50, 50)

    #update space ships
    for i in range(len(shipX)):
        shipY[i] = shipY[i] - speed
        if (shipY[i]  < -1000):
            shipY[i] = 800

    # laser gun
    stroke(255)
    y = height/2
    triangle(gunX - 20, y, gunX, y - 60, gunX + 20, y)

    # update gun location
    if (leftPressed):
        gunX -= 2
    if (rightPressed):
        gunX += 2

    # display beams :at the end of draw()
    strokeWeight(3)
    stroke(255, 255, 0)
    for i in range(len(beamX)):
        line(beamX[i], beamY[i], beamX[i], beamY[i] - 15)
        beamY[i] = beamY[i] - 10
       
    # check hit
    loop_break = False
    for i in range(len(beamX)):  # for each beam
        for j in range(len(shipX)): # for each ship
            if (shipX[j] < beamX[i] and beamX[i] < shipX[j] + 50):
                if (beamY[i] - 15 < shipY[j] + 50):
                    print("hit:", beamX[i], shipX[j])
                    del shipX[j]
                    del shipY[j]
                    del beamX[i]
                    del beamY[i]
                    loop_break = True
                    break
        if loop_break: 
            crashSound.trigger()
            break
                
        
def mouseClicked():
    shipX.append(mouseX - width/2)
    shipY.append(mouseY - height/2)

def keyReleased():
    global leftPressed, rightPressed
    if (keyCode == LEFT):
        leftPressed = False
    elif (keyCode == RIGHT):
        rightPressed = False

def keyPressed():
    global leftPressed, rightPressed
    if (keyCode == LEFT):
        leftPressed = True
    elif (keyCode == RIGHT):
        rightPressed = True
    elif (keyCode == 32):
        beamX.append(gunX)
        beamY.append(height/2 - 50)
        zapSound.trigger()
