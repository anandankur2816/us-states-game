import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US-States-Name-Game")
image = "blank_states_img.gif"
print(image)
screen.addshape(image)
# turtle.hideturtle()
turtle.shape(image)
guessed = []
data = pd.read_csv("50_states.csv")

while len(guessed) < 50:
    user_guess = screen.textinput(f"Guess the {len(guessed)+1}/50 State", "What's the another state's name?").title()
    for name in data.state:
        if name == user_guess:
            t = turtle.Turtle()
            t.hideturtle()
            # print(name)
            state_data = data[data.state == user_guess]
            t.penup()
            t.goto(int(state_data.x), int(state_data.y))
            t.write(user_guess)


screen.exitonclick()
