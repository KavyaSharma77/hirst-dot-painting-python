import colorgram
# colors =colorgram.extract('image.jpg',10)
# rgb_color = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_color.append((r,g,b))
#
# print(rgb_color)

color_list = [(241, 242, 237), (230, 241, 233), (244, 228, 233), (234, 238, 246), (238, 222, 65), (38, 102, 149), (160, 62, 44), (178, 46, 66), (157, 166, 55), (204, 151, 94)]
from turtle import Turtle, Screen,colormode
import random
my_turtle = Turtle()
my_turtle.speed('fastest')
my_turtle.penup()
my_turtle.hideturtle()
colormode(255)

def draw_dots():
    for _ in range(10):

        # my_turtle.pendown()
        color = random.choice(color_list)
        my_turtle.dot(20, color)
        # my_turtle.penup()
        my_turtle.forward(50)
        # my_turtle.pendown()

positions = [(-200,-200), (-200, -160), (-200, -120), (-200, -80), (-200, -40), (-200, 0),(-200, 40),(-200, 80), (-200,120), (-200,160) ]
for x, y in positions:
    # my_turtle.penup()
    my_turtle.goto(x,y)
    # my_turtle.pendown()
    draw_dots()
my_screen = Screen()
my_screen.exitonclick()
