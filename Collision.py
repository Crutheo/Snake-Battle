import random
import turtle

def check_collission(dict, parts, food, enemyParts):

    #    Chequea si se choca contra el muro
    if parts["Head"].xcor() > 280 or parts["Head"].ycor() > 280 or parts["Head"].xcor() < -280 or \
            parts["Head"].ycor() < -280:
        clear(dict,parts)

    #   Chequea si se choca consigo mismo
    for body in parts["Segment"]:
        if body.distance(parts["Head"]) < 20:
            clear(dict,parts)

    #   Chequea si se choca con otra serpiente
    for body in enemyParts["Segment"]:
        if body.distance(parts["Head"]) < 20:
            clear(dict,parts)

    # Chequear si se choca con la comida
    if parts["Head"].distance(food) < 20:
        x_move = random.randint(-14, 14) * 20
        y_move = random.randint(-14, 13) * 20
        food.goto(x_move, y_move)

        dict["Score"] = dict["Score"] + 1
        parts["Text"] = "Score: %s" % dict["Score"]
        parts["Pen"].clear()
        parts["Pen"].write(parts["Text"], False, align="Left", font=("Arial", 14, "normal"))

        body = turtle.Turtle()
        body.penup()
        body.speed(0)
        body.color("dark "+dict["Color"])
        body.shape("square")
        parts["Segment"].append(body)


def clear(dict, parts):
    parts["Head"].goto(parts["InitialPos"], 0)
    parts["Head"].direction = "stop"

    dict["Score"] = 0
    parts["Text"] = "Score: %s" % dict["Score"]
    parts["Pen"].clear()
    parts["Pen"].write(parts["Text"], False, align="Left", font=("Arial", 14, "normal"))

    for body in parts["Segment"]:
        body.goto(-1000, -1000)

    parts["Segment"].clear()
