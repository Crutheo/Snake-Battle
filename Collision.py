def check_collission(head, segment, pos, score, pen, text,dict):

    #    Chequea si se choca contra el muro
    if head.xcor() > 280 or head.ycor() > 280 or head.xcor() < -280 or head.ycor() < -280:
        head.goto(pos, 0)
        head.direction = "stop"
        dict["Score"] = 0
        score = score - score
        text = "Score: %s" % score
        pen.clear()
        pen.write(text, False, align="Left", font=("Arial", 14, "normal"))

        for red_snake_body in segment:
            red_snake_body.goto(-1000, -1000)

        segment.clear()

    #   Chequea si se choca consigo mismo
    for body in segment:
        if body.distance(head) < 20:
            head.goto(pos, 0)
            head.direction = "stop"
            dict["Score"] = 0
            score = 0
            text = "Score: %s" % score
            pen.clear()
            pen.write(text, False, align="Left", font=("Arial", 14, "normal"))

            for body in segment:
                body.goto(-1000, -1000)

            segment.clear()


def check_snake_collision(head, segment, opponent_segment, pos, score, pen, text):
    for body in opponent_segment:
        if body.distance(head) < 20:
            head.goto(pos, 0)
            head.direction = "stop"

            score = 0
            text = "Score: %s" % score
            pen.clear()
            pen.write(text, False, align="Left", font=("Arial", 14, "normal"))

            for body in segment:
                body.goto(-1000, -1000)

            segment.clear()

