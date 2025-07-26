from cmu_graphics import *
from map import *

#image, deadImage, damage, hp, speed, worth, size
enemyStat = [
    ['', '', 1, 80, 1, 10, 0.5],
    [],
    []
]

class Enemy:
    def __init__(self, app, map, start, type):
        self.map = map
        self.y, self.x = start
        self.y = self.y * app.tileSize + app.tileHalf
        self.x = self.x * app.tileSize + app.tileHalf
        self.stat = enemyStat[type]
        self.hp = self.stat[3]
        self.dead = False
        self.size = int(app.tileSize * self.stat[6])

    def onStep(self, app):
        if(not self.dead):
            dy, dx = self.map[(self.y - app.tileHalf) // app.tileSize][(self.x - app.tileHalf) // app.tileSize]
            dy = dy * self.stat[4]
            dx = dx * self.stat[4]
            self.y += dy
            self.x += dx

    def takeDamage(self, app, dmg):
        self.hp -= dmg
        if(self.hp <= 0):
            self.dead = True

    def draw(self, app):
        img = self.stat[0]
        if(self.dead):
            img = self.stat[1]
        drawImage(img, self.x, self.y, width = self.size, height = self.size, align = 'center')