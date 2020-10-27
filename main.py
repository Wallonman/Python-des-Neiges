import turtle

matrice = []

def lire_matrice(fichier):
    f = open(fichier, "r")
    for x in f:
        matrice.append(list(int(a) for a in x.split()))
    print(matrice)


lire_matrice("C:\Src\Python\Project1\matrice.txt")

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
    #print(directions[dir])
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
t = turtle.Turtle()

screen.onkeypress(move_right, "Right")
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_down, "Down")
screen.listen()

turtle.done()

