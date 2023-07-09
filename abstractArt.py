import turtle
import random

shelly = turtle.Turtle()

colors = ['red','blue','yellow','orange','purple','pink','green']


def square(size):
    for n in range(4):
        shelly.forward(size)
        shelly.right(90)



for i in range(100):
    shelly.forward(random.randint(0,360))
    shelly.begin_fill()
    shelly.color(random.choice(colors))
    size = random.randint(10,50)
    square(size)
    shelly.end_fill()
    shelly.forward(random.randint(20,100))
    shelly.left(random.randint(0,360))
    shelly.begin_fill()
    shelly.color(random.choice(colors))
    shelly.circle(random.randint(5,30))
    shelly.end_fill()


shelly.hideturtle()
turtle.done()