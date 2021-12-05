from turtle import Turtle, Screen
from random import randint,  choice
import colorgram as cg

color_list = cg.extract("image.jpg", 30)
rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in color_list][3:]

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.hideturtle()
tim.penup()
tim.speed(0)
tim.setheading(135)
tim.forward(200)
tim.setheading(0)

for i in range(0, 10):
    for j in range(0, 10):
        tim.penup()

        tim.forward(50)
        tim.pendown()
        tim.dot(20, choice(rgb_colors))


    tim.penup()
    if i % 2 == 0:
        tim.right(90)
        tim.forward(50)
        tim.right(90)
        tim.backward(50)
        tim.pendown()

    else:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.backward(50)
        tim.pendown()

screen.exitonclick()

