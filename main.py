import random
import turtle
from turtle import Turtle, Screen
from  color import color_list

list = color_list
turtle.colormode(255)
tim = Turtle()
screen = Screen()
tim.penup()
tim.speed(0)
tim.ht()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100


for dots in range(1, number_of_dots + 1):
    tim.dot(20,random.choice(list))
    tim.forward(50)

    if dots % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen.exitonclick()