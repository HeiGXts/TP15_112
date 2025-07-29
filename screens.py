from cmu_graphics import *
from button import Button
from map import *
from tower import *
from unit import *
import copy
import random
import drawMap


class homePage:
    def __init__(self, app):
        self.startButton = Button(app.width // 2, app.height * 0.6, 200, 80, 'images\startButton.png', lambda: self.toLevel())
        self.settingButton = Button(app.width // 2, app.height * 0.72, 150, 60, 'images\startButton.png', lambda: self.toSetting())
        self.quitButton = Button(app.width // 2, app.height * 0.82, 150, 60, 'images\quitButton.png', lambda: app.quit())
        self.buttons = [self.startButton, self.settingButton, self.quitButton]

    def draw(self, app):
        for button in self.buttons:
            button.draw()

    def toLevel(self):
        app.currentScreen = levelPage(app)

    def toSetting(self):
        app.currentScreen = settingPage(app)

    def mousePress(self, app, mouseX, mouseY):
        for button in self.buttons:
            button.mousePress(mouseX, mouseY)


class settingPage:
    def __init__(self, app):
        self.backButton = Button(app.tileHalf, app.tileHalf, 50, 50, r'images\backButton.png', lambda: self.back(app))
        self.buttons = [self.backButton]

    def draw(self, app):
        pass

    def mousePress(self, app, mouseX, mouseY):
        for button in self.buttons:
            button.mousePress(mouseX, mouseY)

    def back(self, app):
        app.currentScreen = homePage(app)


class creditPage:
    def __init__(self, app):
        self.backButton = Button(app.tileHalf, app.tileHalf, 50, 50, r'images\backButton.png', lambda: self.back(app))
        self.buttons = [self.backButton]

    def draw(self, app):
        pass

    def mousePress(self, app, mouseX, mouseY):
        for button in self.buttons:
            button.mousePress(mouseX, mouseY)

    def back(self, app):
        app.currentScreen = homePage(app)


class levelPage:
    def __init__(self, app):
        self.lv = 0
        self.backButton = Button(app.tileHalf, app.tileHalf, 50, 50, r'images\backButton.png', lambda: self.back(app))
        self.level1 = Button(96, 96, app.tileSize, app.tileSize, 'images\levelFlag.png', lambda: self.toLevel(app, 1))
        self.buttons = [self.level1, self.backButton]
        self.map = copy.deepcopy(worldMap)

    def draw(self, app):
        drawMap.draw(self, app, self.lv)

        for button in self.buttons:
            button.draw()

    def mousePress(self, app, mouseX, mouseY):
        for button in self.buttons:
            button.mousePress(mouseX, mouseY)

    def toLevel(self, app, lv):
        app.currentScreen = Level(app, lv)

    def back(self, app):
        app.currentScreen = homePage(app)


class Level:
    levels = [level1, level2]
    def __init__(self, app, lv):
        self.lv = lv
        self.backButton = Button(app.tileHalf, app.tileHalf, 50, 50, 'images\\backButton.png', lambda: self.back(app))
        self.nextWaveButton = Button(app.width - app.tileHalf, app.height - app.tileHalf, 50, 50, 'images\\nextWaveButton.png', lambda: self.callWave(app))
        self.pauseButton = Button(app.tileSize + app.tileHalf, app.tileHalf, 50, 50, 'images\\pauseButton.png', lambda: self.pause())
        self.unpauseButton = Button(app.tileSize + app.tileHalf, app.tileHalf, 50, 50, 'images\\unpauseButton.png', lambda: self.pause())
        self.restartButton = Button(app.tileHalf, app.height - app.tileHalf, 50, 50, 'images\\restartButton.png', lambda: self.restart(app))
        self.buttons = [self.backButton, self.nextWaveButton, self.pauseButton, self.restartButton]
        self.buildButtons = []
        self.towers = {}
        self.map = copy.deepcopy(Level.levels[lv - 1])
        self.run = True
        self.building = False
        self.m = money[lv - 1]
        self.hp = app.hp
        self.rangeStat = [False]
        self.waves = copy.deepcopy(enemyWave[lv - 1])
        self.thisWave = [0, 0, 0]
        self.enemyLoc = []
        self.count = 0
        self.enemies = []
        self.waveComplete = True

    def draw(self, app):
        drawMap.draw(self, app, self.lv)
        self.drawRange(self.rangeStat)

        for i in range(len(self.enemies)):
            if(self.enemies[i].dead):
                self.enemies[i].draw(app)
        
        for i in range(len(self.enemies) - 1, -1, -1):
            if(not self.enemies[i].dead):
                self.enemies[i].draw(app)

        for co in self.towers:
            self.towers[co].draw(app)

        for button in self.buttons:
            button.draw()

        if(self.building):
            for button in self.buildButtons:
                button.draw()

        drawLabel(str(self.m), app.width - app.tileSize, app.tileHalf, fill = 'white', size = 24, font = app.ithacaFont, bold = True, align = 'right')
        drawLabel(str(self.hp), 3 * app.tileSize, app.tileHalf, fill = 'white', size = 24, font = app.ithacaFont, bold = True, align = 'left')
    
    def mousePress(self, app, mouseX, mouseY):
        for button in self.buttons:
            if(not button.locked):
                button.mousePress(mouseX, mouseY)

        if(self.building):
            for button in self.buildButtons:
                button.mousePress(mouseX, mouseY)
            self.building = False
            self.rangeStat = [False]
        elif(app.tileSize < mouseX < app.width - app.tileSize and app.tileSize < mouseY < app.height - app.tileSize):
            row = mouseY // app.tileSize
            col = mouseX // app.tileSize
            thisTower = self.towers.get((row, col), None)
            if(thisTower):
                self.upgrade(app, row, col, thisTower.type)
            elif(type(self.map[row][col]) == int and self.map[row][col] < 2):
                self.build(app, row, col)

    def keyPress(self, app, key):
        if(key == 'space'):
            self.pause()
        if(key == 'r'):
            self.restart(app)

    def onStep(self, app):
        if(self.run):
            self.count = (self.count + 1) % (app.stepsPerSecond * 5)
            if(self.thisWave != [0, 0, 0]):
                if(self.count % enemySpawnRate[self.lv - 1][len(enemyWave[self.lv - 1]) - len(self.waves) - 1] == 0):
                    if(self.thisWave[0] > 0):
                        self.enemies.append(Enemy(app, self.map, start[self.lv], 0))
                        self.thisWave[0] -= 1
                    elif(self.thisWave[1 > 0]):
                        self.enemies.append(Enemy(app, self.map, start[self.lv], 1))
                        self.thisWave[1] -= 1
                    else:
                        self.enemies.append(Enemy(app, self.map, start[self.lv], 2))
                        self.thisWave[2] -= 1
            
            i = 0
            self.waveComplete = True
            while i < len(self.enemies):
                self.enemies[i].onStep(app)
                self.enemyLoc[i] = (self.enemies[i].x, self.enemies[i].y)
                self.waveComplete = self.waveComplete and self.enemies[i].dead
                if(self.map[abs(self.enemyLoc[i][1] - app.tileHalf) // app.tileSize][abs(self.enemyLoc[i][0] - app.tileHalf) // app.tileSize] == (0, 0)):
                    self.hp -= self.enemies[i].attack()
                    self.enemies.pop(i)
                    self.enemyLoc.pop(i)
                    if(self.hp <= 0):
                        app.currentScreen = settlePage(app, False, self.lv)
                else:
                    i += 1

            if(not self.waveComplete and self.count % 60 == 0):
                self.m += 1

            for tower in self.towers:
                targetNum = 0
                thisStat = self.towers[tower].stat
                for i in range(len(self.enemyLoc)):
                    if(self.enemyLoc[i] == 0 or targetNum == thisStat[5]):
                        break
                    towerY = app.tileSize * tower[0] + app.tileHalf
                    towerX = app.tileSize * tower[1] + app.tileHalf
                    if(self.getRange((towerX, towerY), self.enemyLoc[i], thisStat[3]) and self.count % thisStat[2] == 0 and not self.enemies[i].dead):
                        if(thisStat[6]):
                            for j in range(len(self.enemyLoc)):
                                if(j == i or self.enemyLoc[j] == 0):
                                    continue
                                if(self.getRange(self.enemyLoc[i], self.enemyLoc[j], thisStat[7]) and not self.enemies[j].dead):
                                    self.enemies[j].takeDamage(app, thisStat[1])
                                    if(self.enemies[j].dead):
                                        self.m += self.enemies[j].stat[4]
                        self.enemies[i].takeDamage(app, thisStat[1])
                        targetNum += 1
                        if(self.enemies[i].dead):
                            self.m += self.enemies[i].stat[4]

    def back(self, app):
        app.currentScreen = levelPage(app)

    def build(self, app, row, col):
        self.building = True
        self.tower0 = Button((col - 1) * app.tileSize + app.tileHalf, row * app.tileSize + app.tileHalf, 50, 50, 
                             towerButtonImages[0], lambda: self.buildTower(app, row, col, 0))
        self.tower3 = Button(col * app.tileSize + app.tileHalf, (row - 1) * app.tileSize + app.tileHalf, 50, 50, 
                             towerButtonImages[3], lambda: self.buildTower(app, row, col, 3))
        self.tower6 = Button((col + 1) * app.tileSize + app.tileHalf, row * app.tileSize + app.tileHalf, 50, 50, 
                             towerButtonImages[6], lambda: self.buildTower(app, row, col, 6))
        self.buildButtons = [self.tower0, self.tower3, self.tower6]

    def upgrade(self, app, row, col, type):
        self.building = True
        x = col * app.tileSize + app.tileHalf
        y = row * app.tileSize + app.tileHalf
        self.sell = Button(x, y - app.tileSize, 50, 50, r'images\backButton.png', lambda: self.sellTower(app, row, col, type))
        self.buildButtons = [self.sell]
        self.rangeStat = [True, x, y, towerStat[type][3]]
        if(type % 3 == 0):
            self.towerUpgrade1 = Button(x - app.tileSize, y, 50, 50, towerButtonImages[type + 1], lambda: self.buildTower(app, row, col, type + 1))
            self.towerUpgrade2 = Button(x + app.tileSize, y, 50, 50, towerButtonImages[type + 2], lambda: self.buildTower(app, row, col, type + 2))
            self.buildButtons.extend([self.towerUpgrade1, self.towerUpgrade2])

    def buildTower(self, app, row, col, type):
        cost = towerStat[type][4]
        if(self.m >= cost):
            self.towers[(row, col)] = Tower(app, row, col, type)
            self.m -= cost

    def sellTower(self, app, row, col, type):
        if(type % 3 == 0):
            self.m += towerStat[type][4]
        else:
            self.m += towerStat[type][4] + towerStat[type // 3][4]
        self.towers.pop((row, col))

    def drawRange(self, rangeStat):
        if(rangeStat[0]):
            drawCircle(rangeStat[1], rangeStat[2], rangeStat[3], fill = 'gray', opacity = 50)

    def callWave(self, app):
        if(self.waveComplete):
            if(self.waves == []):
                if(app.levelComplete[self.lv - 1]):
                    app.totalMoney += reward[self.lv - 1][1]
                else:
                    app.levelComplete[self.lv - 1] = True
                    app.totalMoney += reward[self.lv - 1][0]
                app.currentScreen = settlePage(app, True, self.lv)
            else:
                self.enemies = []
                self.thisWave = self.waves.pop(0)
                self.enemyLoc = [0] * sum(self.thisWave)

    def getRange(self, co1, co2, range):
        return abs(co1[0] - co2[0]) ** 2 + abs(co1[1] - co2[1]) ** 2 <= range ** 2
    
    def pause(self):
        if(self.run):
            self.run = False
            self.buttons[2] = self.unpauseButton
        else:
            self.run = True
            self.buttons[2] = self.pauseButton

    def restart(self, app):
        app.currentScreen = Level(app, self.lv)

class settlePage:
    def __init__(self, app, victory, lv):
        pass

    def draw(self, app):
        pass