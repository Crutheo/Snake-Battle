import turtle
import random


class Snake:

    def __init__(self, color, pos_score, pos_snake):

        self.score = 0

        self.lapiz = turtle.Turtle()
        self.lapiz.speed(0)
        self.lapiz.penup()
        self.lapiz.setposition(pos_score,280)
        self.lapiz.color(color)
        self.text = "Score: %s" % self.score
        self.lapiz.write(self.text, False, align="Left", font=("Arial", 14, "normal"))
        self.lapiz.hideturtle()

        self.head = turtle.Turtle()
        self.head.speed(0)
        self.head.penup()
        self.head.shape("square")
        self.head.color(color)
        self.head.goto(pos_snake, 0)
        self.head.direction = "stop"

        self.segment = []

        self.dict = {"Color": color, "Score": self.score, "Direction": self.head.direction}


class Food:
    def __init__(self):
        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.penup()
        self.food.shape("square")
        self.food.color("white")

        self.food.setposition(0, 60)
        

def snake_body(segment, head):

    for i in range(len(segment) - 1, 0, -1):
        x = segment[i - 1].xcor()
        y = segment[i - 1].ycor()
        segment[i].goto(x, y)

    if len(segment) > 0:
        y = head.ycor()
        x = head.xcor()
        segment[0].goto(x, y)


def eat(food, head, segment, score, pen, text, color, dict):
    if head.distance(food) < 20:
        x_move = random.randint(-14, 14) * 20
        y_move = random.randint(-14, 13) * 20
        food.goto(x_move, y_move)

        dict["Score"] = dict["Score"] + 1
        score = score + 1
        text = "Score: %s" % dict["Score"]
        pen.clear()
        pen.write(text, False, align="Left", font=("Arial", 14, "normal"))

        body = turtle.Turtle()
        body.penup()
        body.speed(0)
        body.color("dark "+color)
        body.shape("square")
        segment.append(body)
