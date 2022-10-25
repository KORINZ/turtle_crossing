from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)  # facing the north
        self.goto(STARTING_POSITION)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def game_over(self):
        if self.ycor() == FINISH_LINE_Y:
            print("Win")
