import turtle

#GLOBAL VARIABLES

#set up screen and pen (turtle).
#turtle.colormode(255)
WN = turtle.Screen()
WN.title ('Tatami')
WN.bgcolor('#aa995a')

def draw_rectangle(t, w, l):
    t.fillcolor('#96a20e')
    t.begin_fill()
    t.forward(l)
    t.left(90)
    t.forward(w)
    t.left(90)
    t.forward(l)
    t.left(90)
    t.forward(w)
    t.end_fill()
    t.left(90)


def tatami_gen():
    t = turtle.Turtle()
    t.width(7)
    draw_rectangle(t, 200, 100)
    WN.exitonclick()


tatami_gen()