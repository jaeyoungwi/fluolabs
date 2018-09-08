rectX = []
rectY = []
x = 0
y = 250
w = 600
h = 600
speed = 1

def setup():
    size(800, 800, P3D)

def draw():
    global y
    background(0)
    noFill()
    stroke(255)
    
    
    text("N:" + str(len(rectX)), width/2, 50)
    
    translate(width/2, height/2)
    rotateX(radians(45))
    
    
    for i in range(len(rectX)):
        rect(rectX[i]-width/2, rectY[i]-height/2, 50, 50)
    
    
    for i in range(len(rectX)):
        rectY[i] = rectY[i] - speed
        
def mouseClicked():
    rectX.append(mouseX)
    rectY.append(mouseY)
