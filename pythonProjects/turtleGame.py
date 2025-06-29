from turtle import Turtle, Screen
import random # Import random for random movement

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y_positions = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

is_race_on = False
if user_bet: # Start the race only if a bet was made
    is_race_on = True

winning_color = ""

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230: # Check if a turtle crossed the finish line (e.g., x=230)
            is_race_on = False
            winning_color = turtle.pencolor() # Get the color of the winning turtle
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break # Exit the for loop once a winner is found

        random_distance = random.randint(0, 10) # Move forward randomly between 0 and 10 pixels
        turtle.forward(random_distance)

screen.exitonclick()