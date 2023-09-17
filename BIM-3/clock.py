import graphics as gf
import random

winW = 1000
winH = 1000
win = gf.GraphWin("Colisão", winW, winH)

key = ""

circleRadius = 500
circle = gf.Circle(gf.Point(winW/2, winH/2), circleRadius)
circle.draw(win)

for number in [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
    text = gf.Text(gf.Point(30, 30), str(number))
    text.draw(win)
    text.setSize(15ss)

while key != "Escape":
    key = win.getKey()
    print("hello")