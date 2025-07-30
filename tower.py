from cmu_graphics import *

#image, damage, firerate (fire every x steps), range, cost, shots, AOE, radius
towerStat = [
    ['images\\tower1.png', 5, 30, 120, 35, 1, False, 0],
    ['images\\tower2.png', 8, 15, 150, 80, 1, False, 0],
    ['images\\tower3.png', 35, 100, 250, 80, 1, False, 0],
    ['images\\tower1.png', 5, 50, 110, 45, 1, True, 60],
    ['images\\tower1.png', 7, 60, 150, 90, 1, True, 120],
    ['images\\tower1.png', 5, 50, 400, 110, 3, True, 80],
    ['images\\tower1.png', 2, 15, 90, 40, 4, False, 0],
    ['images\\tower1.png', 3, 15, 100, 85, 10, False, 0],
    ['images\\tower1.png', 5, 30, 120, 85, 4, False, 0]
]

towerButtonImages = ['images\\tower1Button.png', 
                     'images\\tower2Button.png', 
                     'images\\tower3Button.png', 
                     'images\\tower1Button.png',
                     'images\\tower1Button.png',
                     'images\\tower1Button.png',
                     'images\\tower1Button.png',
                     'images\\tower1Button.png',
                     'images\\tower1Button.png']

explosionImages = ['images\explosion1.png', 'images\explosion2.png', 'images\explosion3.png', 'images\explosion4.png', 'images\explosion5.png']

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