import sys
import time as time
import turtle as t

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
    #

    pen.setpos(0, -110)
    pen.write("Mittomén", align="center", font=("Arial", 40))
    time.sleep(0.5)

    pen.setpos(0, -190)
    pen.write("Vissza", align="center", font=("Arial", 40))


def main_menu():
    global subMenu
    subMenu = "main"
    #print(subMenu)
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
    if -130 < x < 135 and subMenu == "main":

        if 110 > y > 65 and subMenu == "main":
            print("Yep")
            games_menu()
            print(subMenu)

        if 25 > y > -20 and subMenu == "main":
            print("YepYep")
            # Score

        if -60 > y > -100 and subMenu == "main":
            print("YepYepYep")
            #sys.exit()
            # exit

        if 110 > y > 65 and subMenu == "games":
            print("Snake")
            # pen.clear() #ez kell
            # os.system("snake.py") #nem jó
            # exec(open("snake.py").read()) #nem jó
            # call(["pytgon", "snake.py"]) #nem jó
            # Popen("python snake.py") #nem jó

        if 25 > y > -20 and subMenu == "games":
            print("Pacman")
            # Score

        if -60 > y > -100 and subMenu == "games":
            print("Mittomén")

        if -150 > y > -175 and subMenu == "games":
            print("Main menu")
            main_menu()
            # back to main menu


if __name__ == "__main__":
    win.onscreenclick(clicked)
    main_menu()

    t.mainloop()