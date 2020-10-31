import turtle
from CONFIGS import *
from plan import *

screen = turtle.Screen()
turtle.title("Python des neiges")
turtle.hideturtle()
turtle.speed(0)
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()


matrice = lire_matrice(fichier_plan)
# print("Matrice = " + str(matrice))

pas = calculer_pas(matrice)
# print("pas = " + str(pas))

# matrice_coord = matrice_coordonnees(matrice, pas)
# print("Matrice des coordonnées = " + str(matrice_coord))
# print("ZONE_PLAN_MAXI = " + str(ZONE_PLAN_MAXI))
# print("ZONE_PLAN_MINI = " + str(ZONE_PLAN_MINI))

# coord = coordonnees((0, 5), pas)
# print("coord = " + str(coord))
# tracer_case((0, 0), COULEUR_MUR, pas)
# tracer_case((0, 1), COULEUR_MUR, pas)
# tracer_case((0, 2), COULEUR_MUR, pas)


afficher_plan(t, matrice, pas)

pos = POSITION_DEPART
c = coordonnees(pos, pas)
# print(c)
t.setpos(c[0] + (pas / 2), c[1] + (pas / 2))
# print(turtle.pos())
t.dot(pas, COULEUR_PERSONNAGE)
# dot = turtle.Turtle(shape="square", visible=True)
# turtle.dot(pas, COULEUR_PERSONNAGE)
# dot.shapesize(0.5, 0.5)
# dot.color("red")
# dot.penup()

directions = {
    "Right": 0,
    "Up": 90,
    "Left": 180,
    "Down": 270
}


def can_move(matrice, position, dir):
    if dir == "Right":
        newpos = (position[0], position[1] + 1)
    if dir == "Up":
        newpos = (position[0] - 1, position[1])
    if dir == "Left":
        newpos = (position[0], position[1] - 1)
    if dir == "Down":
        newpos = (position[0] + 1, position[1])
    return newpos, matrice[newpos[0]][newpos[1]]


def move(matrice, position, dir, delegate):
    newpos, item = can_move(matrice, position, dir)
    # print("new pos = " + str(newpos))
    # print("item = " + str(item))
    if item == 0:
        turtle.onkeypress(None, dir)  # Désactive la touche Left
        t.dot(pas, COULEUR_CASES)
        t.setheading(directions[dir])
        t.fd(pas)
        # dot.setpos(t.pos())
        t.dot(pas, COULEUR_PERSONNAGE)
        turtle.onkeypress(delegate, dir)  # Réassocie la touche Left à la fonction
        return newpos
    else:
        return pos


def move_right():
    global pos
    pos = move(matrice, pos, "Right", move_right)



def move_up():
    global pos
    pos = move(matrice, pos, "Up", move_up)


def move_left():
    global pos
    pos = move(matrice, pos, "Left", move_left)


def move_down():
    global pos
    pos = move(matrice, pos, "Down", move_down)


screen.onkeypress(move_right, "Right")
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_down, "Down")
screen.listen()

turtle.done()
