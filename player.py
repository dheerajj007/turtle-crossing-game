from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.go_to_start()

    def move_up(self):
        self.forward(10)

    def move_left(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)
        self.setheading(90)

    def move_right(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)
        self.setheading(90)
    
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish(self):
        if self.ycor() > 280:
            return True
        else:
            return False
