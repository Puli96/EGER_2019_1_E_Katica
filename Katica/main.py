import sys
import time as time
import turtle as t
import os

sys.path.append("Katica")


win = t.Screen()
win.setup(800, 900)
win.title("Menü (EGER_2019_1_E_Katica)")
win.bgcolor("lightblue")
# win.tracer(0)
subMenu = "main"

dir_path = os.path.dirname(os.path.realpath(__file__))

pen = t.Turtle()


# Main menü elemeinek kiírása
def main_menu():
    global subMenu
    subMenu = "main"
    print(subMenu)
    pen.clear()
    pen.pu()
    pen.setpos(0, 50)
    pen.write("Játékok", align="center", font=("Arial", 40))
    time.sleep(0.5)

    pen.setpos(0, -30)
    pen.write("Pontok", align="center", font=("Arial", 40))
    time.sleep(0.5)

    pen.setpos(0, -110)
    pen.write("Kilépés", align="center", font=("Arial", 40))


def sub_menu():
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


def games_menu():
    global subMenu
    subMenu = "games"
    print(subMenu)
    sub_menu()


def score_menu():
    global subMenu
    subMenu = "score"
    print(subMenu)
    sub_menu()


def clicked(x, y):
    print("Clicked at \nx: {x}, y: {y}".format(x=x, y=y))
    global subMenu
    if -130 < x < 135:

        if 110 > y > 65 and subMenu == "main":
            print("Game menu clicked")
            games_menu()
            # print(subMenu)
            return

        if 25 > y > -20 and subMenu == "main":
            print("Score menu clicked")
            score_menu()
            return

        if -60 > y > -100 and subMenu == "main":
            print("Exit clicked")
            sys.exit()
            # exit

        if 110 > y > 65 and subMenu == "games":
            print("Snake clicked")
            os.system("python {path}/games/snake.py".format(path=dir_path))
            return

        if 25 > y > -20 and subMenu == "games":
            print("Pacman clicked")
            # os.system("python {path}/games/pacman.py".format(path=dir_path))
            return

        if -60 > y > -100 and subMenu == "games":
            print("Pong clicked")
            # os.system("python {path}/games/pong.py".format(path=dir_path))
            return

        if -150 > y > -175 and subMenu == "games":
            print("Back to main menu")
            main_menu()

        # TODO:
        if 110 > y > 65 and subMenu == "score":
            print("Snake score clicked")

        if 25 > y > -20 and subMenu == "score":
            print("Pacman score clicked")

        if -60 > y > -100 and subMenu == "score":
            print("Pong score clicked")

        if -150 > y > -175 and subMenu == "score":
            print("Back to main menu from score")
            main_menu()


if __name__ == "__main__":
    win.onscreenclick(clicked)
    main_menu()

    t.mainloop()
