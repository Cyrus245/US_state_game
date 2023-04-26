from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def move(self, x, y, place):
        self.goto(x, y)
        self.write_name(place)

    def write_name(self, state_name):
        self.write(state_name, align="center", font=('Courier', 8, 'normal'))

    def game_over(self):
        self.write("Game Over", align="center", font=('Courier', 8, 'normal'))
