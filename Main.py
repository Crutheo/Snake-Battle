import turtle
import time
import Movement as mov
import Setup as setup
import Collision as col

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


red = setup.Snake("red", -290, -160)
blue = setup.Snake("blue", 210, 160)

# Setup food

food = setup.Food()

# # Blue food
#
# blue_food = turtle.Turtle()
# blue_food.speed(0)
# blue_food.penup()
# blue_food.shape("square")
# blue_food.color("blue")
#
# blue_food.setposition(-1500, -1500)
#
# # Red food
#
# red_food = turtle.Turtle()
# red_food.speed(0)
# red_food.penup()
# red_food.shape("square")
# red_food.color("red")
#
# red_food.setposition(1500, 1500)


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


screen.listen()

# Red listen

screen.onkeypress(red_go_left, "a")
screen.onkeypress(red_go_right, "d")
screen.onkeypress(red_go_up, "w")
screen.onkeypress(red_go_down, "s")

# Blue listen

screen.onkeypress(blue_go_left, "Left")
screen.onkeypress(blue_go_right, "Right")
screen.onkeypress(blue_go_up, "Up")
screen.onkeypress(blue_go_down, "Down")


delay = 0.1

while True:

    # Screen update/refresh rate

    screen.update()
    time.sleep(delay)

    setup.eat(food.food, red.head, red.segment, red.score, red.lapiz, red.text, 'red',red.dict)
    setup.eat(food.food, blue.head, blue.segment, blue.score, blue.lapiz, blue.text, "blue",blue.dict)

    col.check_collission(red.head, red.segment, -160, red.score, red.lapiz, red.text, red.dict)
    col.check_collission(blue.head, blue.segment, 160, blue.score, blue.lapiz, blue.text, blue.dict)

    setup.snake_body(red.segment, red.head)
    setup.snake_body(blue.segment, blue.head)

    # Collision between snakes bodies

    col.check_snake_collision(red.head, red.segment, blue.segment, -160, red.score, red.lapiz, red.text)
    col.check_snake_collision(blue.head, blue.segment, red.segment, 160, blue.score, blue.lapiz, blue.text)

    # Movement red and blue loop

    mov.move(red.head)
    mov.move(blue.head)

