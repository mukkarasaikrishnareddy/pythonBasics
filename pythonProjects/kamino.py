from turtle import Turtle, Screen

kamino = Turtle()
screen = Screen()

def move_forwards():
    kamino.forward(10)

def move_backwards():
    kamino.backward(10)

def turn_left():
    new_heading = kamino.heading() + 10
    kamino.setheading(new_heading)

def turn_right():
    new_heading = kamino.heading() - 10  # Corrected: Call heading() method
    kamino.setheading(new_heading)

def clear_screen():
    kamino.clear()
    kamino.penup()  # Lift pen before going home to avoid drawing a line
    kamino.home()
    kamino.pendown() # Put pen down after going home

screen.listen()
screen.onkey(move_forwards, "w")  # Corrected: Use onkey for key presses
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_screen, "c") # Added 'c' key to clear and reset

screen.exitonclick()