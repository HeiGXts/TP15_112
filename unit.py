from cmu_graphics import *
from map import *

#left, right, up, down, dead
enemyImage = [
    ['images\enemyUnitL1.png', 'images\enemyUnitR1.png', 'images\enemyUnitU1.png', 'images\enemyUnitD1.png', 'images\enemyUnit1Dead.png'],
    []
]

#image, damage, hp, speed(pixel per 10 steps), worth, size
enemyStat = [
    [enemyImage[0], 1, 30, 8, 10, 0.5],
    [],
    []
]

class Enemy:
    def __init__(self, app, map, start, type):
        self.map = map
        self.y, self.x = start
        self.direction = self.map[self.y][self.x]
        self.y = self.y * app.tileSize + app.tileHalf - (app.tileHalf * self.direction[0])
        self.x = self.x * app.tileSize + app.tileHalf - (app.tileHalf * self.direction[1])
        self.stat = enemyStat[type]
        self.hp = self.stat[2]
        self.dead = False
        self.size = int(app.tileSize * self.stat[5])
        self.type = type
        self.count = 0
        self.rotateAngle = 0
        self.rotateSign = 2

    def onStep(self, app):
        if(not self.dead):
            self.count = (self.count + 1) % 10
            if(self.type == 0):
                if(self.count % 2 == 0):
                    self.rotateAngle += self.rotateSign
                    if(abs(self.rotateAngle) == 10):
                        self.rotateSign *= -1
            if(self.count == 9):
                dy, dx = self.direction
                dy = dy * self.stat[3]
                dx = dx * self.stat[3]
                self.y += dy
                self.x += dx
                ySign, xSign = self.direction
                self.direction = self.map[max(self.y - ySign * app.tileHalf, 0) // app.tileSize][max(self.x - xSign * app.tileHalf, 0) // app.tileSize]

    def takeDamage(self, app, dmg):
        self.hp -= dmg
        if(self.hp <= 0):
            self.dead = True

    def draw(self, app):
        img = ''
        if(self.dead):
            img = self.stat[0][4]
        elif(self.direction == (1, 0)):
            img = self.stat[0][3]
        elif(self.direction == (-1, 0)):
            img = self.stat[0][2]
        elif(self.direction == (0, 1)):
            img = self.stat[0][1]
        else:
            img = self.stat[0][0]
        drawImage(img, self.x, self.y, width = self.size, height = self.size, rotateAngle = self.rotateAngle, align = 'center')

    def attack(self):
        return self.stat[1]