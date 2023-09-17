
import graphics as gf
import random

winW = 1000
winH = 1000

win = gf.GraphWin("Colisão", winW, winH)

key = ""

lineLeft = gf.Line(gf.Point(10, 10), gf.Point(10, winH-10))
lineRight = gf.Line(gf.Point(winW-10, 10), gf.Point(winW-10, winH-10))
lineTop = gf.Line(gf.Point(10, 10), gf.Point(winW-10, 10))
lineBottom = gf.Line(gf.Point(10, winH-10), gf.Point(winW-10, winH-10))
lineLeft.draw(win)
lineRight.draw(win)
lineTop.draw(win)
lineBottom.draw(win)

circlePosition = [winW/2, winH/2]

circleRadius = 30
circle = gf.Circle(gf.Point(circlePosition[0], circlePosition[1]), circleRadius)
circle.draw(win)

speedH = 20
speedV = 20

while key != "Escape":
    key = win.getKey()

    if key == "Escape":
        win.close()

    if key == "w" and circlePosition[1]-speedV-circleRadius >= 10:
        circle.move(0, -speedV)
        circlePosition[1] -= speedV

    if key == "a" and circlePosition[0]-speedH-circleRadius >= 10:
        circle.move(-speedH, 0)
        circlePosition[0] -= speedH

    if key == "s" and circlePosition[1]+speedV+circleRadius <= winH-10:
        circle.move(0, speedV)
        circlePosition[1] += speedV

    if key == "d" and circlePosition[0]+speedH+circleRadius <= winW-10:
        circle.move(speedH, 0)
        circlePosition[0] += speedH
