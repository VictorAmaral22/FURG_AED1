class Orc:
    def __init__(self, name, posX, posY):
        self.name = name
        self.position = [posX, posY]
        self.atk = 200
        self.hp = 100

orc1 = Orc("Ashnazg", 0, 1)