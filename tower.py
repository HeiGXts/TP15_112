from cmu_graphics import *

#image, damage, firerate, range, cost, area, radius
towerStat = [
    ['images\\tower1.png', 5, 2, 200, 30, False, 0],
    ['images\\tower1.png', 8, 6, 220, 50, False, 0],
    ['images\\tower1.png', 20, 1.5, 400, 50, False, 0],
    ['images\\tower1.png', 5, 2, 200, 30, True, 30],
    ['images\\tower1.png', 8, 6, 220, 50, False, 0],
    ['images\\tower1.png', 20, 1.5, 400, 50, False, 0],
    ['images\\tower1.png', 5, 2, 200, 30, False, 0],
    ['images\\tower1.png', 8, 6, 220, 50, False, 0],
    ['images\\tower1.png', 20, 1.5, 400, 50, False, 0],
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
        
    def attack(self, app):
        pass