import turtle
import random

#===========================================================

#generate a random hex color.
def gen_hex_color():
    color = ['#']
    for i in range(6):
        color.append(random.choice('0123456789ABCDEF'))
    return ''.join(color)

#helps the script exit gracefully.
def run():
    global RUNNING
    RUNNING = False

#change fill color. next time fill color is toggled, the new color will be used.
def new_fill():
    global CURRENT_FILL, MEMORY, SWITCH
    SWITCH = False
    CURRENT_FILL = gen_hex_color()
    MEMORY = CURRENT_FILL

#toggle fill color of square: current fill vs. no fill (bgcolor).
def toggle_fill(x=None, y=None):
    global CURRENT_FILL, MEMORY, BGCOLOR, SWITCH
    SWITCH = True
    if x != None:
        if CURRENT_FILL == BGCOLOR:
            CURRENT_FILL = MEMORY
        else:
            CURRENT_FILL = BGCOLOR

#draw a square and allow the fill color to be toggled or changed to a new random color.
def draw_square(n):
    t = turtle.Turtle()
    t.pen(pensize=2, resizemode='user', stretchfactor=(n, n), outline=2, fillcolor=BGCOLOR)
    t.shape('square')
    #center
    start_coord = -n / 2
    t.setpos(start_coord, start_coord)
    while RUNNING:
        global WN
        WN.onkey(new_fill, "space")
        WN.onkey(run, 'q')
        WN.listen()
        t.onclick(toggle_fill)
        global SWITCH
        if SWITCH == True:
            t.fillcolor(CURRENT_FILL)
    WN.exitonclick()

#===========================================================

#GLOBAL VARIABLES

BGCOLOR = '#aa995a'
MEMORY = gen_hex_color()
CURRENT_FILL = BGCOLOR
SWITCH = False
RUNNING = True

#set up screen
WN = turtle.Screen()
WN.title ('Square Grid Playground')
WN.bgcolor(BGCOLOR)


#===========================================================

draw_square(10)


