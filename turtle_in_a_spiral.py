from turtle import *
shape('turtle')
speed(0)
def square(sidelenght=100):
    for i in range(4):
        forward(sidelenght)
        right(90)

def spiral():
    lenght = 5
    for i in range(75):
        square(lenght)
        right(5)
        lenght += 5

spiral()