from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.all_turtle = []
        self.create_snake()
        self.head = self.all_turtle[0]

    def create_snake(self):
        for turtle_position in STARTING_POSITIONS:
            self.add_turtle(turtle_position)

    def add_turtle(self, turtle_position):
        turtle = Turtle()
        turtle.color("white")
        turtle.shape("square")
        turtle.penup()
        turtle.goto(turtle_position)
        self.all_turtle.append(turtle)

    def reset(self):
        for turtle in self.all_turtle:
            turtle.goto(1000, 1000)
            turtle.color("black")
        self.all_turtle.clear()
        self.create_snake()
        self.head = self.all_turtle[0]

    def extend(self):
        self.add_turtle(self.all_turtle[-1].position())

    def move(self):
        for turtle_num in range(len(self.all_turtle) - 1, 0, -1):
            new_x = self.all_turtle[turtle_num - 1].xcor()
            new_y = self.all_turtle[turtle_num - 1].ycor()
            self.all_turtle[turtle_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
