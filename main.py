import turtle

pos = (0, 0)

def move_right():
    turtle.onkeypress(None, "Right")  # Désactive la touche Left
    t.setheading(0)
    t.fd(10)
    turtle.onkeypress(move_right, "Right")  # Réassocie la touche Left à la fonction

def move_up():
    turtle.onkeypress(None, "Up")  # Désactive la touche Left
    t.setheading(90)
    t.fd(10)
    turtle.onkeypress(move_up, "Up")  # Réassocie la touche Left à la fonction

def move_left():
    turtle.onkeypress(None, "Left")  # Désactive la touche Left
    t.setheading(180)
    t.fd(10)
    turtle.onkeypress(move_left, "Left")  # Réassocie la touche Left à la fonction

def move_down():
    turtle.onkeypress(None, "Down")  # Désactive la touche Left
    t.setheading(270)
    t.fd(10)
    turtle.onkeypress(move_down, "Down")  # Réassocie la touche Left à la fonction

screen = turtle.Screen()
t = turtle.Turtle()

#t.dot(10, "blue")

screen.onkeypress(move_right, "Right")
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_down, "Down")
screen.listen()

turtle.done()

