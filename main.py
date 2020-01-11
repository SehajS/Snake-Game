import turtle
import time
import random
import math

delay = 0.1
player_score = 0
high_score = 0

snake_body = []
win = turtle.Screen()
win.setup(width=800, height=800)
win.bgcolor("#030259")
win.tracer(delay=0)
win.title("Snake Game")

# Snake object
snake = turtle.Turtle()
snake.shape("square")
snake.speed(0)
snake.color("white")
snake.goto(0, 0)
snake.penup()
snake.direction = "stop"

# mice object
mice = turtle.Turtle()
mice.speed(0)
mice.shape("circle")
mice.color("red")
mice.shapesize(stretch_wid=0.7, stretch_len=0.7)
mice.penup()
mice.goto(100, 0)

# Pen
pen = turtle.Turtle()
pen.color("white")
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0, 360)
pen.write("Your Score: {}  High Score: {}".format(0, 0), align="center", font=("Comic Sans MS", 24, "bold italic"))
# movements of snake in all the directions


def movement():
    if(snake.direction == "up"):
        y = snake.ycor()
        y += 20
        snake.sety(y)
    if(snake.direction == "down"):
        y = snake.ycor()
        y -= 20
        snake.sety(y)
    if(snake.direction == "left"):
        x = snake.xcor()
        x -= 20
        snake.setx(x)
    if(snake.direction == "right"):
        x = snake.xcor()
        x += 20
        snake.setx(x)

# changing the direction of the snake


def snake_up():
    if snake.direction != "down":
        snake.direction = "up"


def snake_down():
    if snake.direction != "up":
        snake.direction = "down"


def snake_left():
    if snake.direction != "right":
        snake.direction = "left"


def snake_right():
    if snake.direction != "left":
        snake.direction = "right"


# key_press events
win.listen()
win.onkeypress(snake_up, "Up")
win.onkeypress(snake_down, "Down")
win.onkeypress(snake_right, "Right")
win.onkeypress(snake_left, "Left")

while True:
    win.update()

    time.sleep(delay)

    # boundary conditions
    # want snake to appear from the opposite edge of the screen
    if(snake.xcor() > 390):
        snake.setx(-390)
    if(snake.xcor() < -390):
        snake.setx(390)
    if(snake.ycor() > 390):
        snake.sety(-390)
    if(snake.ycor() < -390):
        snake.sety(390)

    # snake eating mice conditions:
    # pythagoras theorem is used for 2-D distance
    if(math.sqrt((snake.xcor() - mice.xcor())**2 + (snake.ycor() - mice.ycor())**2) < 20):
        player_score += 10
        xcord = random.randint(-380, 380)
        ycord = random.randint(-340, 340)
        mice.goto(xcord, ycord)

        new_part = turtle.Turtle()
        new_part.speed(0)
        new_part.shape("square")
        new_part.color("white")
        new_part.penup()
        snake_body.append(new_part)

        # increasing the size of the snake when it eats mice
        # x = snake_body[len(snake_body)-2].xcor()
        # y = snake_body[len(snake_body)-2].ycor()
        # new_part.goto(x,y)

        # startx = snake.xcor()
        # starty = snake.ycor()
        # snake_body[0].goto(startx, starty)

        # if(snake.direction == "right" or snake.direction == "left"):
        #     snake.shapesize(stretch_len=2)
        # if(snake.direction == "up" or snake.direction == "down"):
        #     snake.shapesize(stretch_wid=2)

        # increase the size of the snake when it eats the mice
        # above we added a new body part, now we want to make sure the body part also moves with the head
        i = len(snake_body)-1
        while(i > 0):
            xcord = snake_body[i-1].xcor()
            ycord = snake_body[i-1].ycor()
            snake_body[i].goto(xcord, ycord)
            i -= 1
        # for i = 0
        if(len(snake_body) > 0):
            xcord = snake.xcor()
            ycord = snake.ycor()
            snake_body[0].goto(xcord, ycord)

        if(player_score > high_score):
            high_score = player_score
        pen.clear()
        pen.write("Your Score: {}  High Score: {}".format(
            player_score, high_score), align="center", font=("Comic Sans MS", 24, "bold italic"))

    # increase the size of the snake when it eats the mice
    # above we added a new body part, now we want to make sure the body part also moves with the head
    i = len(snake_body)-1
    while(i > 0):
        xcord = snake_body[i-1].xcor()
        ycord = snake_body[i-1].ycor()
        snake_body[i].goto(xcord, ycord)
        i -= 1
    # for i = 0
    if(len(snake_body) > 0):
        xcord = snake.xcor()
        ycord = snake.ycor()
        snake_body[0].goto(xcord, ycord)

    movement()
    # snake_body collision with itself
    for body_part in snake_body:
        if(body_part.distance(snake) < 20):
            time.sleep(1)
            snake.goto(0, 0)
            snake.direction = "stop"

            for part in snake_body:
                part.goto(700, 700)
            snake_body.clear()

            player_score = 0
            pen.clear()
            pen.write("Your Score: {}  High Score: {}".format(
                player_score, high_score), align="center", font=("Comic Sans MS", 24, "bold italic"))