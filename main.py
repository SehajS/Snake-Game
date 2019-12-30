import turtle 
import time
import random
import math

delay = 0.1 
player_score = 0
high_score = 0

win = turtle.Screen()
win.setup(width = 800, height = 800)
win.bgcolor("black")
win.tracer(delay = 0)
win.title("Snake Game")

# Snake object
snake = turtle.Turtle()
snake.shape("square")
snake.speed(0)
snake.color("white")
snake.goto(0,0)
snake.penup()
snake.direction = "stop"

# mice object
mice = turtle.Turtle()
mice.speed(0)
mice.shape("circle")
mice.color("red")
mice.penup()
mice.goto(100, 0)

# Pen
pen = turtle.Turtle()
pen.color("white")
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0,360)
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
    movement()
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
    if(math.sqrt((snake.xcor() - mice.xcor())**2 + (snake.ycor() - mice.ycor())**2) < 5):
        player_score += 10
        xcord = random.randint(-390,390)
        ycord = random.randint(-390, 390)
        mice.goto(xcord, ycord)
    

    if(player_score > high_score):
        high_score = player_score
        pen.clear()
    pen.write("Your Score: {}  High Score: {}".format(player_score, high_score),align="center", font=("Comic Sans MS", 24, "bold italic"))


    
