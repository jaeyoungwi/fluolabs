def setup():
    size(600,600)
    frameRate(5)

def draw():


    #random dots
    stroke(255)
    background(0)
    
    for x in range(width):
        y = random (height/2)
        point(x,y)
    
    t = 0
    for x in range(width):
        y = noise(t)
        y = map(y, 0, 1, height/2, height)
        print(y)
        point(x,y)
        t = t + .01
        
