from cmu_graphics import *
from button import Button
from map import *
import copy
import random

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
        pass

    def draw(self, app):
        pass

    def mousePress(self, app, mouseX, mouseY):
        for button in self.buttons:
            button.mousePress(mouseX, mouseY)

class creditPage:
    def __init__(self, app):
        pass

    def draw(self, app):
        pass

    def mousePress(self, app, mouseX, mouseY):
        for button in self.buttons:
            button.mousePress(mouseX, mouseY)

class levelPage:
    def __init__(self, app):
        self.backButton = Button(app.tileSize // 2, app.tileSize // 2, 50, 50, 'images\startButton.png', lambda: self.back(app))
        self.level1 = Button(96, 96, app.tileSize, app.tileSize, 'images\startButton.png', lambda: self.toLevel(app, 1))
        self.buttons = [self.level1, self.backButton]
        self.map = copy.deepcopy(worldMap)

    def draw(self, app):
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                imageIndex = self.map[i][j]
                imageX = app.tileSize // 2 + j * app.tileSize
                imageY = app.tileSize // 2 + i * app.tileSize
                if(type(imageIndex) == int):
                    drawImage(images[imageIndex], imageX, imageY, width = app.tileSize, height = app.tileSize, align = 'center')

        for button in self.buttons:
            button.draw()

    def mousePress(self, app, mouseX, mouseY):
        for button in self.buttons:
            button.mousePress(mouseX, mouseY)

    def toLevel(self, app, lv):
        app.currentScreen = level(app, lv)

    def back(self, app):
        app.currentScreen = homePage(app)

class level:
    levels = [level1, level2]
    def __init__(self, app, lv):
        self.backButton = Button(app.tileSize // 2, app.tileSize // 2, 50, 50, 'images\startButton.png', lambda: self.back(app))
        self.buttons = [self.backButton]
        self.map = copy.deepcopy(level.levels[lv - 1])
        self.run = True

    def draw(self, app):
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                imageIndex = self.map[i][j]
                imageX = app.tileSize // 2 + j * app.tileSize
                imageY = app.tileSize // 2 + i * app.tileSize
                if(type(imageIndex) == int):
                    drawImage(images[imageIndex], imageX, imageY, width = app.tileSize, height = app.tileSize, align = 'center')

        for button in self.buttons:
            button.draw()
    
    def mousePress(self, app, mouseX, mouseY):
        for button in self.buttons:
            button.mousePress(mouseX, mouseY)

    def back(self, app):
        app.currentScreen = levelPage(app)