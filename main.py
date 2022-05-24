from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
print(bet)

colors = ["red", "green", "yellow", "blue", "purple"]
team = []

x = -235
y = -100

for index in range(5):
    tim = Turtle(shape="turtle")
    tim.color(colors[index])
    tim.penup()
    tim.goto(x, y)
    y += 50
    team.append(tim)

if bet:
    is_race_on = True

while is_race_on:
    for turtle in team:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == bet:
                print(f"You win, {bet} has came first")
            else:
                print(f"You lose, {turtle.pencolor()} has came first")

        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)



screen.exitonclick()