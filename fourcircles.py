t2 = 0
t3 = 0
t4 = 0
def setup():
    size(600,600)

def draw():
    
    background(0)
    global t2, t3, t4
    #circle 1
    x = random(width)
    ellipse(height * 1/5 , x, 40, 40)
    
    # circle 2
    x = noise(t2)
    x = map( x, 0, 1, 0, width)
    print(x)
    ellipse(height * 2/5, x, 40, 40)
    t2 = t2 + 1
    
    #circle 3
    
    x = noise(t3)
    x = map( x, 0, 1, 0, width)
    print(x)
    ellipse(height * 3/5, x,  40, 40)
    t3 = t3 + .05
    
    #circle 4
    
    x = noise(t4)
    x = map( x, 0, 1, 0, width)
    print(x)
    ellipse(height * 4/5, x, 40, 40)
    t4 = t4 + .01
