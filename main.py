import pygame as pg, math

# outputs color on rainbow depending on progression
def rainbow_color(value):
    step = (value*1536 // 255) % 6
    pos = value*1536 % 255
    if step == 0:
        return (255, pos, 0)
    if step == 1:
        return (255-pos, 255, 0)
    if step == 2:
        return (0, 255, pos)
    if step == 3:
        return (0, 255-pos, 255)
    if step == 4:
        return (pos, 0, 255)
    if step == 5:
        return (255, 0, 255-pos)
# sets up pygame windows
pg.init()
screen = pg.display.set_mode((801,801))

# creates option variables
number_points = 500
times = 2

# main loop
run = True
change = True
while run:
    # handles quitting window and button inputs
    event_list = pg.event.get()
    for event in event_list:
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            change = True
            if event.key == pg.K_ESCAPE:
                run = False
            if event.key == pg.K_RIGHT:
                number_points += 1
            if event.key == pg.K_LEFT:
                if number_points != 0:
                    number_points -= 1
            if event.key == pg.K_UP:
                times += 1
            if event.key == pg.K_DOWN:
                if times != 0:
                    times -= 1
    # runs script if a change in the options happened
    if change:
        #creates a list for stroring all the points
        point_list = []
        # clears display
        screen.fill((255,255,255))
        # creates the points on a circle
        for i in range(number_points):
            angle = (math.pi*2 / number_points) * i
            x = 401 + round(math.cos(angle) * 300)
            y = 401 + round(math.sin(angle) * 300)
            point_list.append((x,y))
        # executes for every point
        for i in range(number_points):
            # calculates how far und the circle the point is
            multiply = 0
            if i != 0:
                multiply = i/number_points
            # gets rainbow color depending on how far the point is
            color = rainbow_color(multiply)
            # draws line 
            pg.draw.aaline(screen,color,point_list[i], point_list[(i*times) % number_points],1)  
        # sets caption to the selected options
        pg.display.set_caption(f'points [LEFT, RIGHT] : {number_points}         times [UP, DOWN] : {times}')
        # updates screen
        pg.display.flip()

        change = False