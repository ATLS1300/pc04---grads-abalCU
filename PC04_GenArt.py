# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 23:48:16 2021

@author: amaiyouf
"""
# Attempt to draw a group of colored stars of different colors in two shapes of rays and stars in different places on a black background

import turtle, random
panel = turtle.Screen() 
w = 600
h = 600 
panel.setup(width=w, height=h)
turtle.Screen().bgcolor((0,0,0))


generativeCircle = turtle.Turtle()  # first turtlle
generativeStar = turtle.Turtle() # second turtlle

rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
smalNumOfStars = 2
largNumOfStars = 10
smalStarRadus = 3
bigStarRadus = 10
numberOfStars = random.randint(smalNumOfStars, largNumOfStars)

size = 20
sides = 2 
angle = 360/3
increment = 30 
generativeStar.width(1)


''''need a question
radiusOfStars = random.randint(smalStarRadus, bigStarRadus)
R = random.randint(1, 256)
G = random.randint(1, 256)
B = random.randint(1, 256)
starColor = random.choice(turtle.color((R,G,B)))
'''



for i in range(numberOfStars):
    generativeCircle.color(random.choice(rainbow))    
    generativeCircle.width(i)
    generativeCircle.circle(random.randint(smalStarRadus, bigStarRadus))
    generativeCircle.penup()
    generativeCircle.goto(random.randint(-200, 200), random.randint(-200, 200))
    generativeCircle.pendown()


for i in range(numberOfStars):
    generativeStar.down()
    generativeStar.color(random.choice(rainbow)) 
    for i in range(4):
        for i in range(sides):
            generativeStar.forward(size)
            generativeStar.right(angle)
        generativeStar.right(increment) 
    generativeStar.up()    
    generativeStar.goto(random.randint(-200, 200), random.randint(-200, 200))


for color in rainbow: # for testing purpose 
    print(color)
    
turtle.done()