from CONFIGS import *


def lire_matrice(fichier):
    m = []
    f = open(fichier, "r")
    for x in f:
        m.append(list(int(a) for a in x.split()))
    return m


def calculer_pas(matrice):
    width = abs(ZONE_PLAN_MINI[0]) + abs(ZONE_PLAN_MAXI[0])
    height = abs(ZONE_PLAN_MINI[1]) + abs(ZONE_PLAN_MAXI[1])
    resX = width / len(matrice[0])
    resY = height / len(matrice)
    # print(width, resX, height, resY)
    return resX if resX < resY else resY


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


def tracer_carre(t, dimension):
    t.begin_fill()
    for _ in range(4):
        t.forward(dimension)
        t.left(90)
    t.end_fill()


def tracer_case(t, case, couleur, pas):
    t.color(couleur)
    coord = coordonnees(case, pas) # matrice_coord[case[0]][case[1]]
    # print(coord)
    t.goto(coord)
    tracer_carre(t, pas)


def afficher_plan(t, matrice, pas):
    for l in range(len(matrice)):
        # print(l)
        for c in range(len(matrice[l])):
            # print(c)
            # print(matrice[l][c])
            if matrice[l][c] > 0 :
                # print(coordonnees((l, c), pas))
                tracer_case(t, (l, c), COULEURS[matrice[l][c]], pas)



