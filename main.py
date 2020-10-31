import turtle
from CONFIGS import *

screen = turtle.Screen()
turtle.title("Python des neiges")
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()


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


def matrice_coordonnees(matrice, pas):
    m = []
    for l in range(len(matrice)):
        i = []
        for c in range(len(matrice[0])):
            i.append(coordonnees((l, c), pas))
        m.append(i)
    return m


matrice_coord = matrice_coordonnees(matrice, pas)

print("Matrice des coordonnées = " + str(matrice_coord))
print("ZONE_PLAN_MAXI = " + str(ZONE_PLAN_MAXI))
print("ZONE_PLAN_MINI = " + str(ZONE_PLAN_MINI))

# coord = coordonnees((0, 5), pas)
# print("coord = " + str(coord))


def tracer_carre(dimension):
    t.begin_fill()
    for _ in range(4):
        t.forward(dimension)
        t.left(90)
    t.end_fill()


def tracer_case(case, couleur, p):
    t.color(couleur)
    coord = coordonnees(case, pas) # matrice_coord[case[0]][case[1]]
    # print(coord)
    t.goto(coord)
    tracer_carre(p)


# tracer_case((0, 0), COULEUR_MUR, pas)
# tracer_case((0, 1), COULEUR_MUR, pas)
# tracer_case((0, 2), COULEUR_MUR, pas)


def afficher_plan(matrice):
    for l in range(len(matrice)):
        # print(l)
        for c in range(len(matrice[l])):
            # print(c)
            # print(matrice[l][c])
            if matrice[l][c] > 0 :
                # print(coordonnees((l, c), pas))
                tracer_case((l, c), COULEURS[matrice[l][c]], pas)



afficher_plan(matrice)

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
