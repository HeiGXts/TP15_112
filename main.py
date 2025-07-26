from cmu_graphics import *
from screens import *

def onAppStart(app):
    app.width = 1280
    app.height = 768
    app.tileSize = 64
    app.tileHalf = 32
    app.currentScreen = homePage(app)
    app.stepsPerSecond = 60

def redrawAll(app):
    app.currentScreen.draw(app)

def onMousePress(app, mouseX, mouseY):
    app.currentScreen.mousePress(app, mouseX, mouseY)

def onStep(app):
    if(isinstance(app.currentScreen, Level)):
        app.currentScreen.onStep(app)

runApp()