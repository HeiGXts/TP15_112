from cmu_graphics import *

#image, damage, firerate (fire every x steps), range, cost, shots, AOE, radius
towerStat = [
    ['images/tower1.png', 5, 30, 120, 35, 1, False, 0],
    ['images/tower2.png', 6, 15, 140, 80, 1, False, 0],
    ['images/tower3.png', 40, 120, 250, 80, 1, False, 0],
    ['images/tower4.png', 4, 50, 110, 45, 1, True, 60],
    ['images/tower5.png', 6, 60, 140, 90, 1, True, 120],
    ['images/tower6.png', 5, 50, 200, 110, 2, True, 80],
    ['images/tower7.png', 1, 15, 90, 40, 4, False, 0],
    ['images/tower8.png', 2, 20, 100, 100, 10, False, 0],
    ['images/tower9.png', 4, 30, 120, 90, 4, False, 0]
]

towerButtonImages = ['images/tower1Button.png', 
                     'images/tower2Button.png', 
                     'images/tower3Button.png', 
                     'images/tower4Button.png',
                     'images/tower5Button.png',
                     'images/tower6Button.png',
                     'images/tower7Button.png',
                     'images/tower8Button.png',
                     'images/tower9Button.png']

#Icon Art Inspiration from:
#https://jimhatama.itch.io/world-wars-weapons-pack

explosionImages = ['images\explosion1.png', 'images\explosion2.png', 'images\explosion3.png', 'images\explosion4.png', 'images\explosion5.png']

towerPrice = [0, 0, 80, 50, 120, 200, 50, 120, 200]

class Tower:
    def __init__(self, app, row, col, type):
        self.row = row
        self.col = col
        self.type = type
        self.stat = towerStat[type]

    def draw(self, app):
        drawImage(self.stat[0], self.col * app.tileSize + app.tileHalf, self.row * app.tileSize + app.tileHalf, 
                  width = app.tileSize, height = app.tileSize, align = 'center')