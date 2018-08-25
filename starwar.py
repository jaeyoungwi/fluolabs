x = 0
y = 0
w = 600 
h = 600
speed = 1

def setup(): 
    size (800, 800, P3D)
    
def draw():
    global y, speed
    background(0)
    speed = map(mouseX, 0, width, 0, 3)
    
    noFill()
    stroke(255)
    pushMatrix()
    translate(width/2, height/2)
    rotateX(PI/4)

    
    
    rect(-w/2, y , w, h)
    y = y - speed
    popMatrix()
   
    text("y:" + str(y), width/2, height - 50)
    
    if (y < -2000):
        y = 500
    
    
    
    
    
    
    
    
    
    
    
    
    
