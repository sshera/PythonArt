from turtle import *

shape("turtle")
speed(0)


def tree(size, levels, angle):
    if levels == 0:
        return

    forward(size)
    right(angle)

    tree(size * 0.8, levels - 1, angle)

    left(angle * 2)

    tree(size * 0.8, levels - 1, angle)

    right(angle)
    back(size)


left(90)
tree(70, 15, 30)

""" forward(100)
left(45)
forward(100)
right(90)
forward(100)
back(200) """

mainloop()
