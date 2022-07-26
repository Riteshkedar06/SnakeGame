import time
from turtle import Turtle, Screen

import scoreboard
from snake import Snake
import food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = food.Food()
score = scoreboard.Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.5)
    snake.move()
    # collection of food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()
    # collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < - 280:
        score.reset()
        snake.reset()

    # self Collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            screen.reset()
screen.exitonclick()
