# JackM400
# jack.millar400@gmail.com
# Python Pong test
from random import *
import turtle

isRunning = True
gameWindow = turtle.Screen()
gameWindow.title("Pong - JackM400")
gameWindow.setup(width=900, height=700)
gameWindow.bgcolor("black")

# pong
pong = turtle.Turtle()
pong.speed(0)
pong.shape("circle")
pong.color("white")
pong.penup()
pong.goto(0, 0)
pong.dx = 4
pong.dy = 4

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


def moveLeftBarUp():
    leftbarposition_y = leftBar.ycor()
    leftbarposition_y += 20
    leftBar.sety(leftbarposition_y)


def moveLeftBarDown():
    leftbarposition_y = leftBar.ycor()
    leftbarposition_y -= 20
    leftBar.sety(leftbarposition_y)


def moveRightBarUp():
    rightbarposition_y = rightBar.ycor()
    rightbarposition_y += 20
    rightBar.sety(rightbarposition_y)


def moveRightBarDown():
    rightbarposition_y = rightBar.ycor()
    rightbarposition_y -= 20
    rightBar.sety(rightbarposition_y)


# score
scoreP1 = 0
scoreP2 = 0

# get input
gameWindow.listen()
# Left player controls
gameWindow.onkeypress(moveLeftBarUp, "w")
gameWindow.onkeypress(moveLeftBarDown, "s")
# Right player controls
gameWindow.onkeypress(moveRightBarUp, "Up")
gameWindow.onkeypress(moveRightBarDown, "Down")

# Terminal - Score
scoreBoard = turtle.Turtle()
scoreBoard.hideturtle()
scoreBoard.goto(0, 300)
scoreBoard.color("white")
scoreBoard.speed(0)
scoreBoard.penup()
scoreBoard.write("Player 1: 0    Player 2: 0", align="center", font=("Arial", 26, "normal"))

# main function/loop
while isRunning:
    gameWindow.update()
    # update ball x position
    pong.setx(pong.xcor() + pong.dx)
    # update ball y position
    pong.sety(pong.ycor() + pong.dy)

    # constrain elements to screen
    # ball constraints
    if pong.ycor() > 338:
        pong.sety(338)
        pong.dy *= -1
    if pong.ycor() < -338:
        pong.sety(-338)
        pong.dy *= -1
    if pong.xcor() > 438:
        scoreBoard.clear()
        scoreP1 += 1
        scoreBoard.write("Player 1: " + scoreP1 + " Player 2: " + scoreP2, align="center", font=("Arial", 26, "normal"))
        pong.setx(438)
        pong.dx *= -1
    if pong.xcor() < -438:
        scoreBoard.clear()
        scoreP2 += 1
        pong.setx(-438)
        pong.dx *= -1

    # bar constraints
    # option 1 : bounce
    # left bar
    if leftBar.ycor() > 290:
        leftBar.sety(290)
    if leftBar.ycor() < -290:
        leftBar.sety(-290)

    # option 2 :emerge
    if rightBar.ycor() > 430:
        rightBar.sety(-410)
    if rightBar.ycor() < -430:
        rightBar.sety(410)

    # collisions
    if (pong.xcor() > 375 and pong.xcor() < 385) and (pong.ycor() < rightBar.ycor() + 35 and rightBar.ycor() - 35):
        pong.setx(375)
        pong.dx *= -1
    if (pong.xcor() < -375 and pong.xcor() > -385) and (pong.ycor() < leftBar.ycor() + 35 and leftBar.ycor() - 35):
        pong.setx(-375)
        pong.dx *= -1
