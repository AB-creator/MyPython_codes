# Simple pong game in Python 3
#This is just a simple pong game I learnt last month..... 
#It helps in relaxing a bit while coding for a lot time(recommended to play with your pals:)))  )

import turtle

wn = turtle.Screen()
wn.title("Pong Game by Anushree")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
 
# Score
score_a = 0
score_b = 0

# bounce




# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("pink")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

 # Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1  #  every time the ball moves it moves by two pixels , dx and dy are the change in places of the ball

# Pen 
pen = turtle.Turtle()    # its pen = module.Class()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions  to mske paddle go up, down, right , left
def paddle_a_up():
    y = paddle_a.ycor()  # paddle_a is name of obj and .ycor() function returns y coordiate of object
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()  # paddle_a is name of obj and .ycor() function returns y coordiate of object
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()  # paddle_b is name of obj and .ycor() function returns y coordiate of object
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()  # paddle_b is name of obj and .ycor() function returns y coordiate of object
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen()      # listen to keyboard module
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"o")
wn.onkeypress(paddle_b_down, "k")

#Main game loop
while True:
    wn.update()


    #  Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:                # top border
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:               # lower border
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1           
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1        
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    
    
    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1


     


    


    
