def check_collission(dict, parts):

    #    Chequea si se choca contra el muro
    if parts["Head"].xcor() > 280 or parts["Head"].ycor() > 280 or parts["Head"].xcor() < -280 or \
            parts["Head"].ycor() < -280:
        parts["Head"].goto(parts["InitialPos"], 0)
        parts["Head"].direction = "stop"
        dict["Score"] = 0
        dict["Score"] = 0
        parts["Text"] = "Score: %s" % dict["Score"]
        parts["Pen"].clear()
        parts["Pen"].write(parts["Text"], False, align="Left", font=("Arial", 14, "normal"))

        for snake_body in parts["Segment"]:
            snake_body.goto(-1000, -1000)

        parts["Segment"].clear()

    #   Chequea si se choca consigo mismo
    for body in parts["Segment"]:
        if body.distance(parts["Head"]) < 20:
            parts["Head"].goto(parts["InitialPos"], 0)
            parts["Head"].direction = "stop"
            dict["Score"] = 0
            parts["Text"] = "Score: %s" % dict["Score"]
            parts["Pen"].clear()
            parts["Pen"].write(parts["Text"], False, align="Left", font=("Arial", 14, "normal"))

            for body in parts["Segment"]:
                body.goto(-1000, -1000)

            parts["Segment"].clear()


def check_snake_collision(dict, parts, enemyParts):
    for body in enemyParts["Segment"]:
        if body.distance(parts["Head"]) < 20:
            parts["Head"].goto(parts["InitialPos"], 0)
            parts["Head"].direction = "stop"

            dict["Score"] = 0
            parts["Text"] = "Score: %s" % dict["Score"]
            parts["Pen"].clear()
            parts["Pen"].write(parts["Text"], False, align="Left", font=("Arial", 14, "normal"))

            for body in parts["Segment"]:
                body.goto(-1000, -1000)

            parts["Segment"].clear()
