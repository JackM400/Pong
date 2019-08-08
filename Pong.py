# JackM400
# jack.millar400@gmail.com
# Python Pong test

import turtle

isRunning = True
gameWindow = turtle.Screen()
gameWindow.title("Pong - JackM400")
gameWindow.setup(width=900, height=700)
gameWindow.bgcolor("black")

leftBar = turtle.Turtle()
leftBar.speed(0)
leftBar.shape("square")
leftBar.color("white")
leftBar.penup()
leftBar.goto(-390, 0)

# main function/loop
while isRunning:
    gameWindow.update()
