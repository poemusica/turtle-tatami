import turtle
import random

#===========================================================

#generate a random hex color.
def gen_hex_color():
    color = ['#']
    for i in range(6):
        color.append(random.choice('0123456789ABCDEF'))
    return ''.join(color)

def make_square(n):
    s = turtle.Turtle()
    #s.ht()
    #s.speed(0)
    s.pen(pencolor="black", pensize=2, shown=True, pendown=False, speed=4)
    s.begin_poly()
    m = n * 50
    for x in range(2):
        s.forward(m)
        s.left(90)
        s.forward(m)
        s.left(90)
    s.end_poly()
    p = s.get_poly()
    turtle.register_shape('mysquare', p)


def new_fill():
    global CURRENT_FILL, MEMORY, SWITCH
    SWITCH = False
    CURRENT_FILL = gen_hex_color()
    MEMORY = CURRENT_FILL

def toggle_fill(x=None, y=None):
    global CURRENT_FILL, MEMORY, BGCOLOR, SWITCH
    SWITCH = True
    if x != None:
        if CURRENT_FILL == BGCOLOR:
            CURRENT_FILL = MEMORY
        else:
            CURRENT_FILL = BGCOLOR

def draw_grid(n):
    #make_square(n)
    t = turtle.Turtle()
    t.pen(pensize=2, resizemode='user', stretchfactor=(5,5), outline=2, fillcolor=BGCOLOR)
    t.shape('square')
    t.shapesize(10, 10)
    #center grid
    start_coord = -n / 2
    t.setpos(start_coord, start_coord)
    while True:
        global WN
        WN.onkey(new_fill, "space")
        WN.listen()
        t.onclick(toggle_fill)
        global SWITCH
        if SWITCH == True:
            t.fillcolor(CURRENT_FILL)

#===========================================================

#GLOBAL VARIABLES

#fav colors
BGCOLOR = '#aa995a'
MEMORY = gen_hex_color()
CURRENT_FILL = BGCOLOR
SWITCH = False

#set up screen
WN = turtle.Screen()
WN.title ('Square Grid Playground')
WN.bgcolor(BGCOLOR)


#===========================================================

draw_grid(5)


