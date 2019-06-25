def move(head):
    if head.direction == "up":
        y = head.ycor()
        if y > 280:
            y = 280
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        if y < -280:
            y = -280
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        if x < -280:
            x = -280
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        if x > 280:
            x = 280
        head.setx(x + 20)

