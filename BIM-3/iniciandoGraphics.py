import graphics as gf
import random

janela = gf.GraphWin("Hello caralho", 1920, 1080)


Leon = gf.Image(gf.Point(500, 500), "./leon.gif")
Leon.draw(janela)

while True:
    if janela.getKey() == "Right":
        Leon.move(30, 0)
    elif janela.getKey() == "Left":
        Leon.move(-30, 0)
    elif janela.getKey() == "Up":
        Leon.move(0, -30)
    elif janela.getKey() == "Down":
        Leon.move(0, 30)