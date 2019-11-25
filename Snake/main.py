import sys
import time as time
import turtle as t
import os

sys.path.append("Snake")

t.setup(800, 900)
win = t.Screen()
win.title("Menü (EGER_2019_1_E_Katica)")
win.bgcolor("lightblue")
# win.tracer(0)
subMenu = "main"

pen = t.Turtle()


def games_menu():
    global subMenu
    subMenu = "games"
    print(subMenu)
    pen.clear()
    pen.pu()
    pen.setpos(0, 50)
    pen.write("Snake", align="center", font=("Arial", 40))
    time.sleep(0.5)

    pen.setpos(0, -30)
    pen.write("Pacman", align="center", font=("Arial", 40))
    time.sleep(0.5)

    pen.setpos(0, -110)
    pen.write("Pong", align="center", font=("Arial", 40))
    time.sleep(0.5)

    pen.setpos(0, -190)
    pen.write("Vissza", align="center", font=("Arial", 40))


def main_menu():
    global subMenu
    subMenu = "main"
    # print(subMenu)
    pen.clear()
    pen.pu()
    pen.setpos(0, 50)
    pen.write("1. Játékok", align="center", font=("Arial", 40))
    time.sleep(0.5)

    pen.setpos(0, -30)
    pen.write("2. Pontok", align="center", font=("Arial", 40))
    time.sleep(0.5)

    pen.setpos(0, -110)
    pen.write("3. Kilépés", align="center", font=("Arial", 40))


def clicked(x, y):
    print(x, y)
    global subMenu
    if -130 < x < 135:

        if 110 > y > 65 and subMenu == "main":
            print("Game menu clicked")
            games_menu()
            print(subMenu)

        if 25 > y > -20 and subMenu == "main":
            print("Score menu clicked")
            # Score

        if -60 > y > -100 and subMenu == "main":
            print("Exit clicked")
            # sys.exit()
            # exit

        if 110 > y > 65 and subMenu == "games":
            print("Snake clicked")
            # pen.clear()
            os.system("python snake.py")

        if 25 > y > -20 and subMenu == "games":
            print("Pacman clicked")
            # Score

        if -60 > y > -100 and subMenu == "games":
            print("Pong clicked")

        if -150 > y > -175 and subMenu == "games":
            print("Back to main menu")
            main_menu()
            # back to main menu


if __name__ == "__main__":
    win.onscreenclick(clicked)
    main_menu()

    t.mainloop()
