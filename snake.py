from turtle import Turtle, Screen

screen = Screen()

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.entire_snake = []
        self.create_snake()
        self.head = self.entire_snake[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_tim = Turtle(shape="square")
        new_tim.color("white")
        new_tim.penup()
        new_tim.goto(position)
        self.entire_snake.append(new_tim)

    def reset(self):
        for seg in self.entire_snake:
            seg.goto(1000, 1000)
        self.entire_snake.clear()
        self.create_snake()
        self.head = self.entire_snake[0]

    def extend(self):
        self.add_segment(self.entire_snake[-1].position())

    def move(self):
        for tim_number in range(len(self.entire_snake) - 1, 0, -1):
            new_x = self.entire_snake[tim_number - 1].xcor()
            new_y = self.entire_snake[tim_number - 1].ycor()
            self.entire_snake[tim_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)