import turtle
import random

#===========================================================

#generate a random hex color.
def gen_hex_color():
    color = ['#']
    for i in range(6):
        color.append(random.choice('0123456789ABCDEF'))
    return ''.join(color)

#change fill color. next time fill color is toggled, the new color will be used.
def new_fill():
    global CURRENT_FILL, MEMORY
    CURRENT_FILL = gen_hex_color()
    MEMORY = CURRENT_FILL

#creates a callback function within the scope of t. 
def filler_maker(t):
    def filler(x, y):
        global CURRENT_FILL, MEMORY, BGCOLOR
        if CURRENT_FILL == BGCOLOR:
            CURRENT_FILL = MEMORY
        else:
            CURRENT_FILL = BGCOLOR
        t.fillcolor(CURRENT_FILL)
    return filler

#draw a square and allow the fill color to be toggled or changed to a new random color.
#note: side of square equals stretchfactor times 20. position of shape is calculated from its centerpoint.
def draw_square(sside, spos):
    stretch = sside / 20
    t = turtle.Turtle()
    t.pen(pensize=2, resizemode='user', stretchfactor=(stretch, stretch), outline=2, fillcolor=BGCOLOR,
        shown=True, pendown=False, speed=0)
    t.shape('square')
    t.setpos(spos['x'], spos['y'])
    t.onclick(filler_maker(t))

#draw a grid of squares
def draw_grid(m):
    square_side = 100
    grid_side = m * square_side
    start_coord = -(grid_side/2 - square_side/2)
    square_pos = {'x': start_coord, 'y':start_coord}
    max_y = start_coord + (square_side * (m - 1))

    WN.tracer(0)
    for i in range(m * m):
        draw_square(square_side, square_pos)
        if square_pos['y'] < max_y:
            square_pos['y'] = square_pos['y'] + square_side
        else:
            square_pos['y'] = start_coord
            square_pos['x'] = square_pos['x'] + square_side
    WN.tracer(1)

def get_user_input():
    while True:
        user_input = raw_input('This program creates an n x n grid. Enter a number to set n. \n')
        try:
            int(user_input)
        except ValueError:
            print "Please enter a whole number."
        else:
            return int(user_input)

def main():
    m = get_user_input()
    draw_grid(m)
    print "Click a square to toggle fill. \nTo switch the fill color press the spacebar."
    WN.onkey(new_fill, "space")
    WN.listen()
    turtle.mainloop()

#===========================================================

#GLOBAL VARIABLES

BGCOLOR = '#aa995a'

#state keepers
MEMORY = gen_hex_color()
CURRENT_FILL = BGCOLOR

#set up screen
WN = turtle.Screen()
WN.title ('Square Grid Playground')
WN.bgcolor(BGCOLOR)

#===========================================================

#let's do this!
main()

