from cmu_graphics import *
from button import Button
from map import *
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
        self.buildButtons = []
        self.building = False
        self.map = copy.deepcopy(worldMap)

    def draw(self, app):
        drawMap.draw(self, app, self.lv)

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

    def draw(self, app):
        drawMap.draw(self, app, self.lv)
    
    def mousePress(self, app, mouseX, mouseY):
        for button in self.buttons:
            if(button.visible):
                button.mousePress(mouseX, mouseY)

        if(self.building):
            for button in self.buildButtons:
                button.mousePress(mouseX, mouseY)
            self.building = False
        elif(app.tileSize < mouseX < app.width - app.tileSize and app.tileSize < mouseY < app.height - app.tileSize):
            row = mouseY // app.tileSize
            col = mouseX // app.tileSize
            if(self.towers.get((row, col), None)):
                self.upgrade(self, app, row, col)
            elif(type(self.map[row][col]) == int):
                self.build(app, row, col)

    def onStep(self, app):
        if(self.run):
            pass
        pass

    def back(self, app):
        app.currentScreen = levelPage(app)

    def build(self, app, row, col):
        self.building = True
        self.towerA = Button((col - 1) * app.tileSize + app.tileHalf, row * app.tileSize + app.tileHalf, 50, 50, 
                             r'images\backButton.png', lambda: self.buildTower(app, row, col, 0))
        self.towerB = Button(col * app.tileSize + app.tileHalf, (row - 1) * app.tileSize + app.tileHalf, 50, 50, 
                             r'images\backButton.png', lambda: self.buildTower(app, row, col, 1))
        self.towerC = Button((col + 1) * app.tileSize + app.tileHalf, row * app.tileSize + app.tileHalf, 50, 50, 
                             r'images\backButton.png', lambda: self.buildTower(app, row, col, 2))
        self.buildButtons = [self.towerA, self.towerB, self.towerC]

    def upgrade(self, app, row, col):
        self.building = True

    def buildTower(self, app, row, col, type):
        pass

    def upgradeTower(self, app, row, col, type):
        pass