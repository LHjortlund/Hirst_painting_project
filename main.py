# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import random
import turtle as turtle_module
turtle_module.colormode(255)
tim = turtle_module.Turtle()

color_list = [(29, 92, 187), (75, 164, 240), (58, 14, 26), (16, 22, 74), (68, 12, 6), (16, 49, 142), (178, 61, 33), (47, 125, 225), (151, 23, 13), (229, 145, 84), (132, 69, 95), (139, 24, 37), (204, 226, 245), (227, 75, 45), (247, 234, 210), (249, 207, 91), (188, 85, 124), (186, 137, 161), (240, 225, 235), (238, 250, 248), (161, 184, 233), (17, 25, 18), (200, 128, 42), (241, 169, 153), (222, 170, 185), (129, 209, 247), (96, 65, 19), (84, 93, 89), (157, 167, 162), (179, 200, 196)]
#Draw 10 * 10 dots, each dot 20 size anf spaced apart 50
tim.speed("fast")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots +1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()