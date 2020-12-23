#Creating a simple circle with Python turtle
import turtle

#Settings for turtle
screen = turtle.Screen()
screen.bgcolor("blue")
screen.title("Drawing Circles")

my_turtle = turtle.Turtle()
my_turtle.pensize(5)
my_turtle.begin_fill()
my_turtle.circle(100)
my_turtle.end_fill()
