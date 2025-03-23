from turtle import Turtle, Screen
import random

screen_with = 500
screen_height = 400
race_on = True

colors = ["red", "green", "blue", "black", "purple", "orange"]
turtles = []


screen = Screen()
screen.setup(screen_with,screen_height)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
print(user_bet)

for i in range (5):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[i])
    turtle.goto(x=(screen_with/2)*(-1), y=-100+i*50)
    turtles.append(turtle)

while race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_on = False
            winner_color = turtle.pencolor()
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

if winner_color == user_bet:
    print(f"YOU WON.{winner_color} turtle wins!!")
else:
    print(f"LOSER. Turtle {winner_color} won ")
screen.exitonclick()
