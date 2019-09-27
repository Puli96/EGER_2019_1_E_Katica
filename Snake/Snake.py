# import stuff
import turtle
import time
import random
import sys

# Játékfelület létrehozása
window = turtle.Screen()
window.title("Snake (EGER_2019_1_E_Katica)")
window.bgcolor("lightblue")
window.setup(width=800, height=800)
window.tracer(0)

delay = 0.1

# Snake fej
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "up"


# Snake test
body = []

# Sznakk
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("green")
food.penup()
food.goto(50, 100)


# A fej mozgatása
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
    head.direction = "up"


def go_down():
    head.direction = "down"


def go_left():
    head.direction = "left"


def go_right():
    head.direction = "right"


window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "Down")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "Left")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "Right")
window.onkeypress(go_right, "d")
# Main loop
while True:
    window.update()
    #
    if head.distance(food) < 20:
        food.goto(random.randint(-290, 290), random.randint(-290, 290))
        new_body = 
    move()
    time.sleep(delay)
window.mainloop()
