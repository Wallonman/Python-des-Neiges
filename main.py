import turtle
from CONFIGS import *
from plan import *

screen = turtle.Screen()
turtle.title("Python des neiges")
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()


matrice = lire_matrice(fichier_plan)
print("Matrice = " + str(matrice))


pas = calculer_pas(matrice)
print("pas = " + str(pas))


# matrice_coord = matrice_coordonnees(matrice, pas)
# print("Matrice des coordonnées = " + str(matrice_coord))
print("ZONE_PLAN_MAXI = " + str(ZONE_PLAN_MAXI))
print("ZONE_PLAN_MINI = " + str(ZONE_PLAN_MINI))

# coord = coordonnees((0, 5), pas)
# print("coord = " + str(coord))
# tracer_case((0, 0), COULEUR_MUR, pas)
# tracer_case((0, 1), COULEUR_MUR, pas)
# tracer_case((0, 2), COULEUR_MUR, pas)


afficher_plan(t, matrice, pas)

pos = (0, 0)
dot = turtle.Turtle(shape="square", visible=True)
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


screen.onkeypress(move_right, "Right")
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_down, "Down")
screen.listen()

turtle.done()
