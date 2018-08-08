star_x = []
star_y = []

comet_x = []
comet_y = []

num = 400

def setup():
    global x, y
    #size(800, 800)
    fullScreen()
    background(0)
    
    for i in range(num):
        star_x.append(random(width))
        star_y.append(random(height))
        comet_x.append(random(width))
        comet_y.append(random(height))
    
def draw():
    global x, y
    
    # red stars
    fill(map(mouseX, 0, width, 0, 256), 0, 0)
    
    for i in range(num):
        ellipse(star_x[i], star_y[i], 8, 8)
        star_x[i] += 1
        star_y[i] += 1
    
        # check boundary
        if (star_x[i] - 4 > width):
            star_x[i] = random(width)
        if (star_y[i] - 4> height):
            star_y[i] = random(height)
      

    # blue stars
    fill(0, 0, map(mouseX, 0, width, 0, 256))
    
    for i in range(num):
        ellipse(comet_x[i], comet_y[i], 8, 8)
        comet_x[i] -= 1
        comet_y[i] += 1
    
        # check boundary
        if (comet_x[i] + 4 < 0):
            comet_x[i] = random(width)
        if (comet_y[i] - 4> height):
            comet_y[i] = random(height)
