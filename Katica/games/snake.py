# import stuff
import random
import time
import turtle as t

# Játékfelület létrehozása.
win = t.Screen()
win.setup(800, 900)
win.title("Katica (EGER_2019_1_E_Katica)")
win.bgcolor("lightblue")
win.tracer(0)

# Lépések között eltelt idő.
delay = 0.1

# Katica feje
head = t.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Katica teste
body = []

# Snakk
food = t.Turtle()
food.speed(0)
food.shape("square")
food.turtlesize = 10
food.color("green")
food.penup()
food.goto(0, 100)

# Pont
score = 0
high_score = 0
pen = t.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(350, 410)
pen.write("Pont: 0 Legmagasabb pont: 0", align="right",
          font=("Arial", 24, "normal"))

#
liner = t.Turtle()
liner.speed(0)
liner.shape("square")
liner.color("blue")
liner.penup()
liner.shapesize(0.1, 500)
liner.goto(0, 410)


def coord_gen():
    return random.randint(-1, 1) * 20 * 4


def spawn_food():  # Snakk áthelyezése és teszhossz növelése.
    global delay
    delay -= .0001
    print("Delay: {d}".format(d=delay))
    food.goto(coord_gen(), coord_gen())
    new_body = t.Turtle()
    new_body.speed(0)
    new_body.shape("square")
    new_body.color("gray")
    new_body.penup()
    body.append(new_body)


# A fej mozgatása.
def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)

    if head.direction == "down":
        head.sety(head.ycor() - 20)

    if head.direction == "left":
        head.setx(head.xcor() - 20)

    if head.direction == "right":
        head.setx(head.xcor() + 20)


# Input kezelés
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def update_score(s, hs):
    pen.clear()
    pen.write("Pont: {} Legmagasabb pont: {}".format(s, hs), align="right",
              font=("Arial", 24, "normal"))


def game_over():
    global score
    global delay
    print("Dead! score: {score}".format(score=score))
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"
    for body_part in body:
        body_part.goto(1000, 1000)
    body.clear()
    food.goto(0, 100)
    score = 0
    update_score(score, high_score)
    delay = 0.1
    print("Delay: {d}".format(d=delay))


win.listen()
win.onkeypress(go_up, "Up")
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "Down")
win.onkeypress(go_down, "s")
win.onkeypress(go_left, "Left")
win.onkeypress(go_left, "a")
win.onkeypress(go_right, "Right")
win.onkeypress(go_right, "d")

print("Start. Delay: {d}".format(d=delay))

# Main loop
while True:
    win.update()

    if head.xcor() > 370 or head.xcor() < -380 or head.ycor() > 390 or head.ycor() < -420:
        game_over()

    if head.distance(food) < 20:
        spawn_food()
        score += 1
        update_score(score, high_score)

        if score > high_score:
            high_score = score
            update_score(score, high_score)

    for i in range(len(body) - 1, 0, -1):
        body[i].goto(body[i - 1].xcor(), body[i - 1].ycor())

    if len(body) > 0:
        body[0].goto(head.xcor(), head.ycor())

    move()

    for body_part in body:
        if body_part.distance(head) < 20:
            game_over()

    time.sleep(delay)
