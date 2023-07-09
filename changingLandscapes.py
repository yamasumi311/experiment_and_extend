import turtle
import random

shelly = turtle.Turtle()

colors = ['red','green','yellow','orange','purple','pink']

def house(x, y, wallColor, roofColor):
    shelly.penup()
    shelly.goto(x,y)
    shelly.setheading(0) #set turtle to point to the right
    shelly.pendown()
    shelly.begin_fill()
    shelly.color(wallColor)
    for i in range(4):
        shelly.right(90)
        shelly.forward(30)
    shelly.end_fill()
    shelly.backward(35) #go back and get ready for roof
    shelly.begin_fill()
    shelly.color(roofColor)
    shelly.left(60)
    shelly.forward(40)
    shelly.right(120)
    shelly.forward(40)
    shelly.right(120)
    shelly.forward(40)
    shelly.end_fill()

turtle.bgcolor('blue')

for n in range(10):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    wallColor = random.choice(colors)
    roofColor = random.choice(colors)
    house(x, y, wallColor, roofColor)
