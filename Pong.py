# JackM400
# jack.millar400@gmail.com
# Python Pong test

import turtle

isRunning = True
gameWindow = turtle.Screen()
gameWindow.title("Pong - JackM400")
gameWindow.setup(width=900, height=700)
gameWindow.bgcolor("black")

# pong
pong = turtle.Turtle()
pong.speed(0)
pong.shape("square")
pong.color("white")
pong.penup()
pong.goto(0, 0)

# left bar
leftBar = turtle.Turtle()
leftBar.speed(0)
leftBar.shape("square")
leftBar.shapesize(stretch_wid=7, stretch_len=1)
leftBar.color("white")
leftBar.penup()
leftBar.goto(-390, 200)

# right bar
rightBar = turtle.Turtle()
rightBar.speed(0)
rightBar.shape("square")
rightBar.shapesize(stretch_wid=7, stretch_len=1)
rightBar.color("white")
rightBar.penup()
rightBar.goto(390, -200)

# main function/loop
while isRunning:
    gameWindow.update()
