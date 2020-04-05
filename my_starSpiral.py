from turtle import *
speed(0)
def star(sidelenght=100):
    for i in range(4):
        forward(sidelenght)
        right(144)

def starSpiral():
    length = 5
    for i in range(60):
        star(length)
        right(5)
        length += 5
        rt(5)

starSpiral()