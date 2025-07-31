from cmu_graphics import *
from screens import *

#All Coding and Art in this project is DONE BY MYSELF
#No use of any AI, tutorial, or any code copied else where
#Except for the font and background images at the title screen, which I found online

#Font in use:
# 'Ithaca', 'font\ithaca-font\Ithaca-LVB75.ttf'
#https://fontesk.com/ithaca-font/

def onAppStart(app):
    app.width = 1280
    app.height = 768
    app.tileSize = 64
    app.tileHalf = 32
    app.currentScreen = homePage(app)
    app.stepsPerSecond = 60
    app.hp = 20
    app.levelComplete = [False, False, False, False, False]
    app.towerLock = [False, False, True, True, True, True, True, True, True]
    app.totalMoney = 0
    app.moneyRate = 90

def redrawAll(app):
    app.currentScreen.draw(app)

def onMousePress(app, mouseX, mouseY):
    app.currentScreen.mousePress(app, mouseX, mouseY)

def onKeyPress(app, key):
    if(isinstance(app.currentScreen, Level)):
        app.currentScreen.keyPress(app, key)

def onStep(app):
    if(isinstance(app.currentScreen, Level)):
        app.currentScreen.onStep(app)

runApp()