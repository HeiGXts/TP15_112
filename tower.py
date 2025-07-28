from cmu_graphics import *

#image, damage, firerate (fire every x steps), range, shot, cost, area, radius
towerStat = [
    ['images\\tower1.png', 5, 30, 200, 30, 1, False, 0],
    ['images\\tower1.png', 8, 10, 220, 50, 1, False, 0],
    ['images\\tower1.png', 20, 40, 400, 50, 1, False, 0],
    ['images\\tower1.png', 5, 30, 200, 30, 1, True, 30],
    ['images\\tower1.png', 8, 10, 220, 50, 1, False, 0],
    ['images\\tower1.png', 20, 40, 400, 50, 1, False, 0],
    ['images\\tower1.png', 5, 30, 200, 30, 1, False, 0],
    ['images\\tower1.png', 8, 10, 220, 50, 1, False, 0],
    ['images\\tower1.png', 20, 40, 400, 50, 1, False, 0],
]

class Tower:
    def __init__(self, app, row, col, type):
        self.row = row
        self.col = col
        self.type = type
        self.stat = towerStat[type]

    def draw(self, app):
        drawImage(self.stat[0], self.col * app.tileSize + app.tileHalf, self.row * app.tileSize + app.tileHalf, 
                  width = app.tileSize, height = app.tileSize, align = 'center')
        
    def attack(self, app, target):
        pass