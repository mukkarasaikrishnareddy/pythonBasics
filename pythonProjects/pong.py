from turtle import Screen, Turtle
import time


sc = Screen()
sc.title("Pong")
sc.bgcolor("white")
sc.setup(width=1000, height=600)
sc.tracer(0)  


lef_paddle = Turtle()
lef_paddle.shape("square")
lef_paddle.color("black")
lef_paddle.shapesize(stretch_wid=6, stretch_len=2)
lef_paddle.penup()
lef_paddle.goto(-400, 0)

right_paddle = Turtle()
right_paddle.shape("square")
right_paddle.color("brown")
right_paddle.shapesize(stretch_wid=6, stretch_len=2)
right_paddle.penup()
right_paddle.goto(400, 0)


ball = Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 5  
ball.dy = -5 

left_player_score = 0
right_player_score = 0
score_board = Turtle()
score_board.color("green")
score_board.penup()
score_board.hideturtle() 
score_board.goto(0, 260)
score_board.write(f"Left Player: {left_player_score}   Right Player: {right_player_score}", align="center", font=("Courier", 24, "normal"))


def paddle_left_up():
    y = lef_paddle.ycor()
    if y < 240: 
        y += 20
        lef_paddle.sety(y)

def paddle_left_down():
    y = lef_paddle.ycor()
    if y > -240:
        y -= 20
        lef_paddle.sety(y)

def paddle_right_up():
    y = right_paddle.ycor()
    if y < 240: 
        y += 20
        right_paddle.sety(y)

def paddle_right_down():
    y = right_paddle.ycor()
    if y > -240: 
        y -= 20
        right_paddle.sety(y)


sc.listen()
sc.onkeypress(paddle_left_up, "w")
sc.onkeypress(paddle_left_down, "s")
sc.onkeypress(paddle_right_up, "Up")    
sc.onkeypress(paddle_right_down, "Down") 


while True:
    sc.update() 

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    
    if ball.xcor() > 490: 
        ball.goto(0, 0)
        ball.dx *= -1
        left_player_score += 1
        score_board.clear()
        score_board.write(f"Left Player: {left_player_score}   Right Player: {right_player_score}", align="center", font=("Courier", 24, "normal"))
    elif ball.xcor() < -490: 
        ball.goto(0, 0)
        ball.dx *= -1
        right_player_score += 1
        score_board.clear()
        score_board.write(f"Left Player: {left_player_score}   Right Player: {right_player_score}", align="center", font=("Courier", 24, "normal"))

    
    if (ball.xcor() > 380 and ball.xcor() < 390) and (ball.ycor() < right_paddle.ycor() + 60 and ball.ycor() > right_paddle.ycor() - 60):
        ball.setx(380)
        ball.dx *= -1

    
    if (ball.xcor() < -380 and ball.xcor() > -390) and (ball.ycor() < lef_paddle.ycor() + 60 and ball.ycor() > lef_paddle.ycor() - 60):
        ball.setx(-380)
        ball.dx *= -1

    time.sleep(0.01) 