inc = .05
t = 0

def setup():
    size(600, 600)

    
def draw():
    global t
    background(0)
    stroke (255)
    
    # random dots
    beginShape()
    noFill()
    for x in range(width):
        vertex(x, random(height/2))
    endShape()
    
    #smooth dots
    beginShape() 
    frameStart = t
    for x in range(width):
        y = noise(t)
        y = map(y, 0, 1, height/2, height)
        vertex(x,y)
        t = t + inc
    t = frameStart - inc*5
    endShape()
