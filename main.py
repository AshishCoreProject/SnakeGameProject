from turtle import Screen
import time  # import time module
from snake import Snake
from food import Food
from scoreboard import Scoreboard
scoreboard = Scoreboard()
food = Food()
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

screen.tracer(0)
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

Game_is_on = True
while Game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # we just need move the snake Head Rest of his body move towards to it.
    # segment[0].left(90)

    # detect collision with food
    # 20 is the distance between the snake head and food if it less than 20 we will refresh the location of food

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # collision with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        Game_is_on = False
        scoreboard.game_over()

    # detect collision with snake tail
    # if the head collides with  any segment in the tail
    for body in snake.segment[1:]:
        if snake.head.distance(body) < 1:
            Game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
