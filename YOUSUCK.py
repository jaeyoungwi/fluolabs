x = 50
xSpeed = 1
col = 255
strike = 0
recWidth = 150

def setup():
    #size(800, 800)
    fullScreen()
    
def draw():
    background(0)
    global x, strike
    fill(col, 0, 0)
    rect(x, height/2, 150, 75)  
    x = x + xSpeed
    
    # display xSpeed
    
    fill(255)
    text ("xSpeed:" +str(xSpeed), width/2, 32)
    text ("x:" +str(x), width/2, 50)
    text("strike: " + str(strike), width/2, 64)

    if(strike == 3):
        textSize(60)
        text("YOU SUCK TAYLOR!", width/2 - 225, height/2)
        noLoop()

    #check boundary
    if ( x > width ):
        x = -1 * recWidth
        strike += 1
        
    if (x < -1 * recWidth):
        x = width
        strike += 1



     
    
def mouseClicked():
    global xSpeed, col
    print (mouseX, mouseY)
    
    col = random(100, 255)

            
    
    if ( (x < mouseX) and (mouseX < x + recWidth)):
        if(( height/2 < mouseY) and (mouseY < height/2 + 75)):
            xSpeed = xSpeed * - 1

    if(xSpeed > 0):
        xSpeed += 1
    else:
        xSpeed -= 1
    
    
