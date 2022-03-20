#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 15:59:38 2022

@author: Linda
"""

## Turtle library

import turtle

scrn = turtle.Screen()
scrn.bgcolor("aliceblue")

linda = turtle.Turtle()
linda.color("deepskyblue1")
linda.pensize(2)

# turtle face east at the beginning
# turtle move forward
linda.forward(150)

# turn left at 90 degree
linda.left(90)
linda.forward(100)
linda.left(90)
linda.forward(150)
linda.left(90)
linda.forward(100)

# use for loop to repeat 10 times
tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(5)

dist1 = 50
for _ in range(10):
    tess.forward(dist1)
    tess.right(120)
    dist1 = dist1 + 15

elan = turtle.Turtle()
elan.color("olivedrab1")
elan.pensize(2)
elan.up()

dist2 = 5
for _ in range(10):
    elan.stamp()   # leave an impression on the canvas
    elan.forward(dist2)
    elan.right(24)
    dist2 = dist2 + 2

# use stamp to leave impression
erin = turtle.Turtle()
erin.color("aqua")
erin.shape("turtle")
erin.penup()                     # this is new
for size in range(10):
    erin.forward(50)          # move tess along
    erin.stamp()
    erin.forward(-50)              # and turn her
    erin.right(36)

scrn.exitonclick()


linda.salary = 5000
print(linda.salary)
