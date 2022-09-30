import turtle
import math

obj=turtle.Turtle()

def lovecurve(t):
    x = 16 * (math.sin(t) ** 3)
    y = 13 * math.cos(t)  - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
    return x,y 


screen=turtle.Screen()

screen.title("Valentine's Day Special Love Art")
screen.bgcolor("black") 
obj.pensize(2)
obj.pencolor("red") 
obj.speed(5) 

import time

time.sleep(3)

factor = 10

obj.penup()

for i in range(0,400):
    x, y = lovecurve(i) 
    obj.goto(x * factor , y * factor)
    obj.pendown()

obj.penup()
obj.forward(-180)
obj.pendown()

obj.setheading(42)

obj.pensize(10)

obj.forward(500)

obj.setheading(-90)

obj.forward(30)

obj.setheading(90)

obj.forward(30)

obj.setheading(180)

obj.forward(30)

obj.hideturtle()

turtle.done()