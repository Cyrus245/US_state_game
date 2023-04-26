import turtle
from turtle import Screen
import pandas as pd
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.title('U.S State Game')

# adding a background to turtle
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv('50_states.csv')
all_state = data.state.to_list()

answerInput = screen.textinput(title='Guess the state', prompt="what's another state name").title()

is_game_on = True
player = Player()
scoreboard = Scoreboard()
guessed_list = []

while len(guessed_list) < 50:
    guesses_state = data[data.state == answerInput]
    guessed_x = guesses_state.iloc[0].x
    guessed_y = guesses_state.iloc[0].y
    player.move(guessed_x, guessed_y, answerInput)

    if answerInput in all_state:
        guessed_list.append(answerInput)
        scoreboard.score_up()
        answerInput = screen.textinput(title=f'{scoreboard.score}/50 States correct',
                                       prompt="what's another state name").title()

    if answerInput == "Exit":
        missing_states = []
        for state in all_state:
            if state not in guessed_list:
                missing_states.append(state)
        df = pd.DataFrame({
            "Missing State": missing_states

        })

        df.to_csv('learn.csv')
        break

# get coordinate by clicking on the screen
# def get_mouseClick_cor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouseClick_cor)
# turtle.mainloop()
