from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

speed = 0.07

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()


screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

is_on = True
scoree = Scoreboard()
while is_on:
    screen.update()
    time.sleep(speed)
    snake.move()

    # Detect food collision.
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        speed -= 0.001
        scoree.increase_score()

    # Detect Wall collision
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        scoree.reset()
        snake.reset()

    # Detext self collision
    for seg in snake.segments[1:]:
        if snake.segments[0].distance(seg) < 10:
            scoree.reset()
            snake.reset()
screen.exitonclick()
