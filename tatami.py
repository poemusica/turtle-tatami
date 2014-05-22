import turtle
import random

#===========================================================

#GLOBAL VARIABLES

#fav colors
BGCOLOR = '#aa995a'
GREEN = '#96a20e'

#set up screen and pen (turtle).
#turtle.colormode(255)
WN = turtle.Screen()
WN.title ('Tatami')
WN.bgcolor(BGCOLOR)

#===========================================================

#generate a random hex color.
def gen_hex_color():
    color = ['#']
    for i in range(6):
        color.append(random.choice('0123456789ABCDEF'))
    return ''.join(color)

#draw rectangle.
def draw_rectangle(t, w, l, fill=None):
    t.down()
    if fill:
        t.begin_fill()
    for x in range(2):
        t.forward(w)
        t.left(90)
        t.forward(l)
        t.left(90)
    t.end_fill()


def draw_room(rm_w, rm_l):
    room = turtle.Turtle()
    room.pen(pencolor="black", pensize=7, shown=False, pendown=False, speed=4)
    #center room
    room.setpos( (-rm_w / 2), (-rm_l / 2) )
    draw_rectangle(room, rm_w, rm_l)


def size_of_tiles(w, l):
    tile_short = w/200
    tile_long = tile_short * 2


def tatami_gen(w, l):
    draw_room(w, l)
    size_of_tiles(w, l)

    WN.exitonclick()

#===========================================================

tatami_gen(600, 600)