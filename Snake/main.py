import time as time
import turtle as t

t.setup(800, 900)
win = t.Screen()
win.title("Menü (EGER_2019_1_E_Katica)")
win.bgcolor("lightblue")
#win.tracer(0)

pen = t.Turtle()

pen.pu()
pen.setpos(0, 50)
pen.write("1. Játékok", align="center", font=("Arial", 40))
# -130, 110
# -130, 65
# 145, 110
# 145, 65
time.sleep(0.5)

pen.setpos(0, -30)
pen.write("2. Pontok", align="center", font=("Arial", 40))
time.sleep(0.5)

pen.setpos(0, -110)
pen.write("3. Kilépés", align="center", font=("Arial", 40))


def clicked(x, y):
    print(x, y)
    if -130 < x < 135:
        if 110 > y > 65:
            print("Yep")
            pen.clear()
            exec(open("snake.py").read())


win.onscreenclick(clicked)

t.mainloop()
