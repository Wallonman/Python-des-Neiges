import turtle
from CONFIGS import *


def lire_matrice(fichier):
    m = []
    f = open(fichier, "r")
    for x in f:
        m.append(list(int(a) for a in x.split()))
    return m


matrice = lire_matrice(fichier_plan)
print("Matrice = " + str(matrice))


def calculer_pas(matrice):
    width = abs(ZONE_PLAN_MINI[0]) + abs(ZONE_PLAN_MAXI[0])
    height = abs(ZONE_PLAN_MINI[1]) + abs(ZONE_PLAN_MAXI[1])
    resX = width / len(matrice[0])
    resY = height / len(matrice)
    # print(width, resX, height, resY)
    return resX if resX < resY else resY


pas = calculer_pas(matrice)
print("pas = " + str(pas))


def coordonnees(case, pas):
    x = case[1] * pas + ZONE_PLAN_MINI[0]
    y = ZONE_PLAN_MAXI[1] - (case[0] * pas) - pas
    coord = (x, y)
    return coord

coord = coordonnees((0, 5), pas)
print("ZONE_PLAN_MAXI = " + str(ZONE_PLAN_MAXI))
print("ZONE_PLAN_MINI = " + str(ZONE_PLAN_MINI))

print("coord = " + str(coord))

pos = (0, 0)
dot = turtle.Turtle(shape="circle", visible=True)
dot.shapesize(0.5, 0.5)
dot.color("red")
dot.penup()


def move(dir, delegate):
    directions = {
        "Right": 0,
        "Up": 90,
        "Left": 180,
        "Down": 270
    }
    turtle.onkeypress(None, dir)  # Désactive la touche Left
    # print(directions[dir])
    t.setheading(directions[dir])
    t.fd(10)
    dot.setpos(t.pos())
    turtle.onkeypress(delegate, dir)  # Réassocie la touche Left à la fonction


def move_right():
    move("Right", move_right)


def move_up():
    move("Up", move_up)


def move_left():
    move("Left", move_left)


def move_down():
    move("Down", move_down)


screen = turtle.Screen()
turtle.title("Python des neiges")
t = turtle.Turtle()
t.penup()

screen.onkeypress(move_right, "Right")
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_down, "Down")
screen.listen()

turtle.done()
