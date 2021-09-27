from turtle import Screen
from snake import Snake
from Food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Play Snake Game")
screen.tracer(0)

game_is_on = True
all_turtle = []
number_of_turtles = 3
turtle_start_position = 0

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # TODO: Detect Collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_score()

    # TODO: Detect Collision with wall.
    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290:
        # game_is_on = False
        scoreboard.reset_score()
        snake.reset()

    # TODO: Detect Collision with tail.
    for turtle in snake.all_turtle[1:]:
        if snake.head.distance(turtle) < 10:
            # game_is_on = False
            scoreboard.reset_score()
            snake.reset()

screen.exitonclick()
