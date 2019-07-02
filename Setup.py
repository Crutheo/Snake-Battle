import turtle


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

        self.parts = {"Pen": self.lapiz, "Head": self.head, "Text": self.text, "Segment": self.segment,
                      "InitialPos": pos_snake}


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
