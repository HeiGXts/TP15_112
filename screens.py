from cmu_graphics import *
from button import Button
from map import *
from tower import *
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
        self.level1 = Button(96, 96, app.tileSize, app.tileSize, 'images\startButton.png', lambda: self.toLevel(app, 1))
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
        self.backButton = Button(app.tileHalf, app.tileHalf, 50, 50, r'images\backButton.png', lambda: self.back(app))
        self.buttons = [self.backButton]
        self.buildButtons = []
        self.towers = {}
        self.map = copy.deepcopy(Level.levels[lv - 1])
        self.run = True
        self.building = False
        self.m = money[lv - 1]
        self.hp = app.hp
        self.rangeStat = [False]

    def draw(self, app):
        drawMap.draw(self, app, self.lv)
        self.drawRange(self.rangeStat)

        for co in self.towers:
            self.towers[co].draw(app)

        for button in self.buttons:
            button.draw()

        if(self.building):
            for button in self.buildButtons:
                button.draw()

        drawLabel(str(self.m), app.width - app.tileSize, app.tileHalf, fill = 'white', size = 24, font = app.ithacaFont, bold = True, align = 'right')
    
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

    def onStep(self, app):
        if(self.run):
            pass
        pass

    def back(self, app):
        app.currentScreen = levelPage(app)

    def build(self, app, row, col):
        self.building = True
        self.tower0 = Button((col - 1) * app.tileSize + app.tileHalf, row * app.tileSize + app.tileHalf, 50, 50, 
                             r'images\backButton.png', lambda: self.buildTower(app, row, col, 0))
        self.tower3 = Button(col * app.tileSize + app.tileHalf, (row - 1) * app.tileSize + app.tileHalf, 50, 50, 
                             r'images\backButton.png', lambda: self.buildTower(app, row, col, 3))
        self.tower6 = Button((col + 1) * app.tileSize + app.tileHalf, row * app.tileSize + app.tileHalf, 50, 50, 
                             r'images\backButton.png', lambda: self.buildTower(app, row, col, 6))
        self.buildButtons = [self.tower0, self.tower3, self.tower6]

    def upgrade(self, app, row, col, type):
        self.building = True
        x = col * app.tileSize + app.tileHalf
        y = row * app.tileSize + app.tileHalf
        self.sell = Button(x, y - app.tileSize, 50, 50, r'images\backButton.png', lambda: self.sellTower(app, row, col, type))
        self.buildButtons = [self.sell]
        self.rangeStat = [True, x, y, towerStat[type][3]]
        if(type % 3 == 0):
            self.towerUpgrade1 = Button(x - app.tileSize, y, 50, 50, r'images\backButton.png', lambda: self.buildTower(app, row, col, type + 1))
            self.towerUpgrade2 = Button(x + app.tileSize, y, 50, 50, r'images\backButton.png', lambda: self.buildTower(app, row, col, type + 2))
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