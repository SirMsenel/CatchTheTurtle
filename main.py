import turtle
import random

screen = turtle.Screen()
screen.bgcolor("Light yellow")
screen.title("Cath The Turtle")

game_over = False
FONT = ('Comic Sans' , 30 , 'normal')
FONT1 =('Comic Sans' , 100 , 'normal')
SİZE = 10
turtle_list = []
score = 0
countdwn_turtle = turtle.Turtle()
countdwn_turtle1 = turtle.Turtle()
s_c = turtle.Turtle()

def setscoreturtle():
    s_c.hideturtle()
    s_c.color("black")
    s_c.penup()
    th = screen.window_height() / 2
    y = th * 0.9
    s_c.setposition(0,y)
    s_c.write(arg="Score: 0 ", move=False , align="center" , font= FONT)

def maketurtles(x, y):
    turtle_mod = turtle.Turtle()
    def hand_cl(x,y):
        global score
        score += 1
        s_c.clear()
        s_c.write(arg="Score: {} ".format(score), move=False, align="center", font=FONT)

    turtle_mod.onclick(hand_cl)
    turtle_mod.shape("turtle")
    turtle_mod.color("green")
    turtle_mod.shapesize(3)
    turtle_mod.penup()
    turtle_mod.goto( x * SİZE, y * SİZE)
    turtle_list.append(turtle_mod)

x_kor = [-20,-10,0,10,20]
y_kor = [20,10,0,-10,-20]

def setupturtles():
    for x in x_kor:
        for y in y_kor:
            maketurtles(x,y)

def hideturt ():
    for turtle_mod in turtle_list :
        turtle_mod.hideturtle()

def showturtrand():
    if not game_over:
         hideturt()
         random.choice(turtle_list).showturtle()
         screen.ontimer(showturtrand,600)

def countdwn(time):
    global game_over
    countdwn_turtle.hideturtle()
    countdwn_turtle.color("Dark red")
    countdwn_turtle.penup()
    th = screen.window_height() / 2
    y = th * 0.8
    countdwn_turtle.setposition(0, y)
    countdwn_turtle.clear()
    countdwn_turtle1.color("red")
    countdwn_turtle1.penup()
    countdwn_turtle1.hideturtle()

    if time > 0 :
        countdwn_turtle.clear()
        countdwn_turtle.write(arg="Time: {} ".format(time), move=False, align="center", font=FONT)
        screen.ontimer(lambda:countdwn(time - 1 ), 1000)
    else:
        game_over = True
        countdwn_turtle.clear()
        countdwn_turtle1.clear()
        hideturt()
        countdwn_turtle1.write(arg="Game Over!", move=False, align="center", font=FONT1)




def starttogame():
    turtle.tracer(0)

    setscoreturtle()
    setupturtles()
    showturtrand()
    hideturt()
    countdwn(10)

    turtle.tracer(1)

starttogame()
turtle.mainloop()