import turtle
import time
import Movement as mov
import Setup as setup
import Collision as col


# Red movement
def red_go_up():
    if red.head.direction != "down":
        red.head.direction = "up"
        red.dict["Direction"] = red.head.direction
        print(red.dict)
def red_go_down():
    if red.head.direction != "up":
        red.head.direction = "down"
        red.dict["Direction"] = red.head.direction
        print(red.dict)
def red_go_left():
    if red.head.direction != "right":
        red.head.direction = "left"
        red.dict["Direction"] = red.head.direction
        print(red.dict)
def red_go_right():
    if red.head.direction != "left":
        red.head.direction = "right"
        red.dict["Direction"] = red.head.direction
        print(red.dict)

# Blue movement
def blue_go_up():
    if blue.head.direction != "down":
        blue.head.direction = "up"
def blue_go_down():
    if blue.head.direction != "up":
        blue.head.direction = "down"
def blue_go_left():
    if blue.head.direction != "right":
        blue.head.direction = "left"
def blue_go_right():
    if blue.head.direction != "left":
        blue.head.direction = "right"


# Screen and border setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Snake")
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off screen updates

border = turtle.Turtle()
border.penup()
border.goto(-310, -310)
border.color("white")
border.pendown()
for side in range(4):
    border.fd(620)
    border.lt(90)
border.hideturtle()

# Snake setup, ("color", coord_score, coord_snake)
red = setup.Snake("red", -290, -160)
blue = setup.Snake("blue", 210, 160)

# Setup food
food = setup.Food()

# Read Inputs
screen.listen()

# Red Inputs
screen.onkeypress(red_go_left, "a")
screen.onkeypress(red_go_right, "d")
screen.onkeypress(red_go_up, "w")
screen.onkeypress(red_go_down, "s")

# Blue Inputs
screen.onkeypress(blue_go_left, "Left")
screen.onkeypress(blue_go_right, "Right")
screen.onkeypress(blue_go_up, "Up")
screen.onkeypress(blue_go_down, "Down")

# Screen Refresh
delay = 0.1
while True:
    screen.update()
    time.sleep(delay)

    setup.eat(food.food, red.dict, red.parts)
    setup.eat(food.food, blue.dict, blue.parts)

    col.check_collission(red.dict, red.parts)
    col.check_collission(blue.dict, blue.parts)
    col.check_snake_collision(red.dict, red.parts, blue.parts)
    col.check_snake_collision(blue.dict, blue.parts, red.parts)

    setup.snake_body(red.segment, red.head)
    setup.snake_body(blue.segment, blue.head)

    mov.move(red.head)
    mov.move(blue.head)
