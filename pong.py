import turtle
import winsound

wn=turtle.Screen()
wn.title(" Pong by deptrainhilop ")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# paddle A
paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.color("white")
paddle_A.shapesize(stretch_wid=5, stretch_len=1)
paddle_A.penup()
paddle_A.goto(-350,0)

# paddle B
paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("white")
paddle_B.shapesize(stretch_wid=5, stretch_len=1)
paddle_B.penup()
paddle_B.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.07
ball.dy=-0.07

# Score

score_A=0
score_B=0

#pen 
pen=turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("THANG A: 0 -- 0 : THANG B ", align="center", font=( "courier", 24, "bold"))

#function-move-paddle
def paddle_A_up():
    y=paddle_A.ycor()
    y+=20
    paddle_A.sety(y)
def paddle_A_down():
    y=paddle_A.ycor()
    y-=20
    paddle_A.sety(y)

def paddle_B_up():
    y=paddle_B.ycor()
    y+=20
    paddle_B.sety(y)
def paddle_B_down():
    y=paddle_B.ycor()
    y-=20
    paddle_B.sety(y)


def play():
    winsound.PlaySound("XTC.wav", winsound.SND_ASYNC)

#keybooard binding
wn.listen()
wn.onkeypress(play,"p")

wn.onkeypress(paddle_A_up, "w")
wn.onkeypress(paddle_A_down, "s")
wn.onkeypress(paddle_B_up, "Up")
wn.onkeypress(paddle_B_down, "Down")



#main game loop
while True:
    
    wn.update()

    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
  

    # border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *=-1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *=-1

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *=-1
        score_A+=1
        pen.clear()
        pen.write("THANG A: {} -- {} : THANG B ".format(score_A, score_B), align="center", font=( "courier", 24, "bold"))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *=-1
        score_B+=1
        pen.clear()
        pen.write("THANG A: {} -- {} : THANG B ".format(score_A, score_B), align="center", font=( "courier", 24, "bold"))


    # paddle and ball collisions
    if(ball.xcor()> 340 and ball.xcor()<350) and ( ball.ycor() < paddle_B.ycor()+ 50 and ball.ycor() > paddle_B.ycor() -50 ):
        ball.setx(340)
        ball.dx*=-1

    if(ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_A.ycor()+ 50 and ball.ycor() > paddle_A.ycor() -50 ):
        ball.setx(-340)
        ball.dx*=-1

    
    

