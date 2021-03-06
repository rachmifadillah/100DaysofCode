# How to extract rgb values from images
# use colorgram library package
# import colorgram
# colors = colorgram.extract('hirst.jpg', 10)
# my_list = []

# for i in range(len(colors)):
#     red = colors[i].rgb.r
#     green = colors[i].rgb.g
#     blue = colors[i].rgb.b
#     my_list.append((red, green, blue))

import turtle
import random

colors_list = [(237, 40, 115), (142, 27, 70), (219, 162, 59), (238, 71, 36), (14, 144, 89), (182, 166, 43)]

# Create a hirst painting
turtle.colormode(255)
paw = turtle.Turtle()
paw.setheading(225)
paw.penup()
paw.forward(250)
paw.pendown()
paw.setheading(0)
paw.speed(0)


def draw(dot_size, space):
    for i in range(space):
        for _ in range(space):
            paw.dot(dot_size, random.choice(colors_list))
            paw.penup()
            paw.forward(50)
            paw.pendown()

        paw.setheading(90)
        paw.penup()
        paw.forward(50)
        paw.left(90)
        paw.forward(50 * space)
        paw.setheading(360)
        paw.pendown()


draw(20, 10)
paw.hideturtle()

screen = turtle.Screen()
screen.exitonclick()
