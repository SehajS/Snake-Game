import turtle 
import time

delay = 0.1 

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
    if(snake.xcor() > 390):
        snake.setx(-390)
    if(snake.xcor() < -390):
        snake.setx(390)
    if(snake.ycor() > 390):
        snake.sety(-390)
    if(snake.ycor() < -390):
        snake.sety(390)
    
