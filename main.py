from cmu_graphics import *
from screens import *

def onAppStart(app):
    app.width = 1280
    app.height = 768
    app.tileSize = 64
    app.currentScreen = homePage(app)

def redrawAll(app):
    app.currentScreen.draw(app)

def onMousePress(app, mouseX, mouseY):
    for button in app.currentScreen.buttons:
        button.mousePress(mouseX, mouseY)

runApp()