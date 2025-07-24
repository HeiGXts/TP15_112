from cmu_graphics import *
from button import Button

class homePage:
    def __init__(self, app):
        self.startButton = Button(app.width // 2, app.height * 0.6, 200, 80, 'images\startButton.png', lambda: self.toLevel())
        self.settingButton = Button(app.width // 2, app.height * 0.72, 150, 60, 'images\startButton.png', lambda: self.toSetting())
        self.quitButton = Button(app.width // 2, app.height * 0.82, 150, 60, 'images\quitButton.png', lambda: app.quit())
        self.buttons = [self.startButton, self.settingButton, self.quitButton]

    def draw(self):
        for button in self.buttons:
            button.draw()

    def toLevel(self):
        app.currentScreen = levelPage(app)

    def toSetting(self):
        app.currentScreen = settingPage(app)

class settingPage:
    def __init__(self, app):
        pass

    def draw(self):
        pass

class creditPage:
    def __init__(self, app):
        pass

    def draw(self):
        pass

class levelPage:
    def __init__(self, app):
        self.level1 = Button(100, 100, 100, 100, 'images\startButton.png', lambda: self.toLevel(app, 1))
        self.buttons = [self.level1]

    def draw(self):
        for button in self.buttons:
            button.draw()

    def toLevel(self, app, lv):
        app.currentScreen = level(app, lv)

class level:
    def __init__(self, app, lv):
        pass

    def draw(self):
        pass