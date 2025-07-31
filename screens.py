from cmu_graphics import *
from button import Button
from map import *
from tower import *
from unit import *
import copy
import random
import drawMap

#Background Images:
#https://stock.adobe.com/search?k=pixel+art+background&asset_id=726960402
#https://stock.adobe.com/search?k=pixel+art+background&asset_id=760560007
#https://www.shutterstock.com/image-vector/pixel-art-game-level-background-8-2303999851
#https://www.shutterstock.com/image-vector/pixel-art-game-level-background-space-2553891639

backgroundImages = ['images/background1.png', 'images/background2.png', 'images/background3.png', 'images/background4.png']

class homePage:
    def __init__(self, app):
        self.startButton = Button(app.width // 2, app.height * 0.6, 200, 80, 'images\startButton.png', lambda: self.toLevel())
        self.settingButton = Button(app.tileHalf, app.tileHalf, 50, 50, 'images\settingButton.png', lambda: self.toSetting())
        self.creditButton = Button(app.width // 2, app.height * 0.72, 150, 60, 'images\creditButton.png', lambda: self.toCredit())
        self.quitButton = Button(app.width // 2, app.height * 0.82, 150, 60, 'images\quitButton.png', lambda: app.quit())
        self.buttons = [self.startButton, self.settingButton, self.creditButton, self.quitButton]
        self.backgroundImage = backgroundImages[random.randint(0, 3)]

    def draw(self, app):
        drawImage(self.backgroundImage, 0, 0, width = app.width, height = app.height)
        for button in self.buttons:
            button.draw()
        drawImage('images/title.png', app.width // 2, app.height * 0.35, width = 500, height = 250, align = 'center')

    def toLevel(self):
        app.currentScreen = levelPage(app)

    def toSetting(self):
        app.currentScreen = settingPage(app)

    def toCredit(self):
        app.currentScreen = creditPage(app)

    def mousePress(self, app, mouseX, mouseY):
        for button in self.buttons:
            button.mousePress(mouseX, mouseY)


class settingPage:
    def __init__(self, app):
        self.backButton = Button(app.tileHalf, app.tileHalf, 50, 50, 'images/backButton.png', lambda: self.back(app))
        self.difficultyButton = Button(app.width // 2, 7 * app.tileSize, 150, 60, 'images/emptyButton.png', lambda: self.changeDifficulty(app))
        self.FPSButton = Button(app.width // 2, 9 * app.tileSize, 150, 60, 'images/emptyButton.png', lambda: self.changeFPS(app))
        self.screenSizeButton = Button(app.width // 2, 11 * app.tileSize, 150, 60, 'images/emptyButton.png', lambda: self.changeScreenSize(app))
        self.unlockButton = Button(2 * app.tileSize, app.height - app.tileHalf, 150, 60, 'images/emptyButton.png', lambda: self.unlockAll(app))
        self.buttons = [self.backButton, self.difficultyButton, self.FPSButton, self.screenSizeButton, self.unlockButton]
        self.backgroundImage = backgroundImages[random.randint(0, 3)]

    def draw(self, app):
        drawImage(self.backgroundImage, 0, 0, width = app.width, height = app.height)
        drawLabel('Setting', app.width // 2, app.tileSize, fill = rgb(210, 175, 90), size = 60, font = 'Ithaca', bold = True, align = 'center')

        drawLabel('Controls:', app.width // 2, 3 * app.tileSize, fill = rgb(210, 175, 90), font = 'Ithaca', size = 40)
        drawLabel("Press 'r' to restart current level", app.width // 2, 4 * app.tileSize, fill = 'white', font = 'Ithaca', size = 30)
        drawLabel("Press 'space' to pause/unpause current level", app.width // 2, 5 * app.tileSize, fill = 'white', font = 'Ithaca', size = 30)

        for button in self.buttons:
            button.draw()

        drawLabel('Difficulty:', app.width // 2, 6 * app.tileSize, fill = rgb(210, 175, 90), font = 'Ithaca', size = 40)
        if(app.hp == 20):
            drawLabel('Easy', app.width // 2, 7 * app.tileSize - 5, fill = 'white', font = 'Ithaca', size = 30)
        elif(app.hp == 15):
            drawLabel('Normal', app.width // 2, 7 * app.tileSize - 5, fill = 'white', font = 'Ithaca', size = 30)
        else:
            drawLabel('Hard', app.width // 2, 7 * app.tileSize - 5, fill = 'white', font = 'Ithaca', size = 30)

        drawLabel('Default FPS:', app.width // 2, 8 * app.tileSize, fill = rgb(210, 175, 90), font = 'Ithaca', size = 40)
        drawLabel(str(app.stepsPerSecond), app.width // 2, 9 * app.tileSize - 5, fill = 'white', font = 'Ithaca', size = 30)

        drawLabel('Screen Size:', app.width // 2, 10 * app.tileSize, fill = rgb(210, 175, 90), font = 'Ithaca', size = 40)
        if(app.width == 1280):
            drawLabel('Normal', app.width // 2, 11 * app.tileSize - 5, fill = 'white', font = 'Ithaca', size = 30)
        elif(app.width == 1600):
            drawLabel('Large', app.width // 2, 11 * app.tileSize - 5, fill = 'white', font = 'Ithaca', size = 30)

        drawLabel('Unlock All', app.tileSize * 2, app.height - app.tileHalf - 5, fill = 'white', font = 'Ithaca', size = 30)

    def mousePress(self, app, mouseX, mouseY):
        for button in self.buttons:
            button.mousePress(mouseX, mouseY)

    def back(self, app):
        app.currentScreen = homePage(app)

    def changeDifficulty(self, app):
        if(app.hp == 20):
            app.hp = 15
            app.moneyRate = 120
        elif(app.hp == 15):
            app.hp = 10
            app.moneyRate = 150
        else:
            app.hp = 20
            app.moneyRate = 90

    def changeFPS(self, app):
        if(app.stepsPerSecond == 60):
            app.stepsPerSecond = 30
        else:
            app.stepsPerSecond = 60

    def changeScreenSize(self, app):
        if(app.width == 1280):
            app.width = 1600
            app.height = 960
            app.tileSize = 80
            app.tileHalf = 40
            self.difficultyButton = Button(app.width // 2, 7 * app.tileSize, 150, 60, 'images/emptyButton.png', lambda: self.changeDifficulty(app))
            self.FPSButton = Button(app.width // 2, 9 * app.tileSize, 150, 60, 'images/emptyButton.png', lambda: self.changeFPS(app))
            self.screenSizeButton = Button(app.width // 2, 11 * app.tileSize, 150, 60, 'images/emptyButton.png', lambda: self.changeScreenSize(app))
            self.unlockButton = Button(2 * app.tileSize, app.height - app.tileHalf, 150, 60, 'images/emptyButton.png', lambda: self.unlockAll(app))
            self.buttons = [self.backButton, self.difficultyButton, self.FPSButton, self.screenSizeButton, self.unlockButton]
        else:
            app.width = 1280
            app.height = 768
            app.tileSize = 64
            app.tileHalf = 32
            self.difficultyButton = Button(app.width // 2, 7 * app.tileSize, 150, 60, 'images/emptyButton.png', lambda: self.changeDifficulty(app))
            self.FPSButton = Button(app.width // 2, 9 * app.tileSize, 150, 60, 'images/emptyButton.png', lambda: self.changeFPS(app))
            self.screenSizeButton = Button(app.width // 2, 11 * app.tileSize, 150, 60, 'images/emptyButton.png', lambda: self.changeScreenSize(app))
            self.unlockButton = Button(2 * app.tileSize, app.height - app.tileHalf, 150, 60, 'images/emptyButton.png', lambda: self.unlockAll(app))
            self.buttons = [self.backButton, self.difficultyButton, self.FPSButton, self.screenSizeButton, self.unlockButton]

    def unlockAll(self, app):
        app.levelComplete = [True, True, True, True, True]
        app.towerLock = [False, False, False, False, False, False, False, False, False]

class creditPage:
    def __init__(self, app):
        self.backButton = Button(app.tileHalf, app.tileHalf, 50, 50, r'images\backButton.png', lambda: self.back(app))
        self.buttons = [self.backButton]
        self.backgroundImage = backgroundImages[random.randint(0, 3)]

    def draw(self, app):
        drawImage(self.backgroundImage, 0, 0, width = app.width, height = app.height)
        drawLabel('Credit', app.width // 2, app.tileSize, fill = rgb(210, 175, 90), size = 60, font = 'Ithaca', bold = True)
        drawLabel('Programming:', 2 * app.tileSize, 3 * app.tileSize, fill = rgb(210, 175, 90), font = 'Ithaca', size = 40, align = 'left')
        drawLabel('Gavin Yin', 5 * app.tileSize, 3 * app.tileSize, fill = 'white', font = 'Ithaca', size = 38, align = 'left')
        drawLabel('Art:', 12 * app.tileSize, 3 * app.tileSize, fill = rgb(210, 175, 90), font = 'Ithaca', size = 40, align = 'left')
        drawLabel('Gavin Yin', 15 * app.tileSize, 3 * app.tileSize, fill = 'white', font = 'Ithaca', size = 38, align = 'left')
        drawLabel('Language:', 2 * app.tileSize, 4 * app.tileSize + app.tileHalf, fill = rgb(210, 175, 90), font = 'Ithaca', size = 40, align = 'left')
        drawLabel('Python v3.12.10', 5 * app.tileSize, 4 * app.tileSize + app.tileHalf, fill = 'white', font = 'Ithaca', size = 38, align = 'left')
        drawLabel('Library:', 12 * app.tileSize, 4 * app.tileSize + app.tileHalf, fill = rgb(210, 175, 90), font = 'Ithaca', size = 40, align = 'left')
        drawLabel('CMU Graphics v1.1.42', 15 * app.tileSize, 4 * app.tileSize + app.tileHalf, fill = 'white', font = 'Ithaca', size = 38, align = 'left')

        drawLabel('Background Images:', app.width // 2, 6 * app.tileSize, fill = rgb(210, 175, 90), font = 'Ithaca', size = 40)
        drawLabel('https://stock.adobe.com/search?k=pixel+art+background&asset_id=726960402', 
                  app.width // 2, 6 * app.tileSize + app.tileHalf, fill = 'white', font = 'Ithaca', size = 30)
        drawLabel('https://stock.adobe.com/search?k=pixel+art+background&asset_id=760560007', 
                  app.width // 2, 7 * app.tileSize, fill = 'white', font = 'Ithaca', size = 30)
        drawLabel('https://www.shutterstock.com/image-vector/pixel-art-game-level-background-8-2303999851', 
                  app.width // 2, 7 * app.tileSize + app.tileHalf, fill = 'white', font = 'Ithaca', size = 30)
        drawLabel('https://www.shutterstock.com/image-vector/pixel-art-game-level-background-space-2553891639', 
                  app.width // 2, 8 * app.tileSize, fill = 'white', font = 'Ithaca', size = 30)
        
        drawLabel('Font:', app.width // 2, 9 * app.tileSize, fill = rgb(210, 175, 90), font = 'Ithaca', size = 40)
        drawLabel('Ithaca', app.width // 2, 9 * app.tileSize + app.tileHalf, fill = 'white', font = 'Ithaca', size = 35)

        for button in self.buttons:
            button.draw()

    def mousePress(self, app, mouseX, mouseY):
        for button in self.buttons:
            button.mousePress(mouseX, mouseY)

    def back(self, app):
        app.currentScreen = homePage(app)


class levelPage:
    def __init__(self, app):
        self.lv = 0
        self.backButton = Button(app.tileHalf, app.tileHalf, 50, 50, 'images/backButton.png', lambda: self.back(app))
        self.flagImages = {True: 'images\levelFlag.png', False: 'images\levelFlagIncomplete.png'}
        self.level1 = Button(app.tileSize + app.tileHalf, app.tileSize + app.tileHalf, app.tileSize, app.tileSize, 
                             self.flagImages[app.levelComplete[0]], lambda: self.toLevel(app, 1))
        self.level2 = Button(3 * app.tileSize + app.tileHalf, 4 * app.tileSize + app.tileHalf, app.tileSize, app.tileSize, 
                             self.flagImages[app.levelComplete[1]], lambda: self.toLevel(app, 2))
        self.level2.locked = not app.levelComplete[0]
        self.level3 = Button(7 * app.tileSize + app.tileHalf, 7 * app.tileSize + app.tileHalf, app.tileSize, app.tileSize, 
                             self.flagImages[app.levelComplete[2]], lambda: self.toLevel(app, 3))
        self.level3.locked = not app.levelComplete[1]
        self.level4 = Button(16 * app.tileSize + app.tileHalf, 6 * app.tileSize + app.tileHalf, app.tileSize, app.tileSize, 
                             self.flagImages[app.levelComplete[3]], lambda: self.toLevel(app, 4))
        self.level4.locked = not app.levelComplete[2]
        self.level5 = Button(13 * app.tileSize + app.tileHalf, app.tileSize + app.tileHalf, app.tileSize, app.tileSize, 
                             self.flagImages[app.levelComplete[4]], lambda: self.toLevel(app, 5))
        self.level5.locked = not app.levelComplete[3]
        self.shopButton = Button(app.width - app.tileHalf, app.height - app.tileHalf, 50, 50, 'images/shopButton.png', lambda: self.toShop(app))
        self.buttons = [self.level1, self.level2, self.level3, self.level4, self.level5, self.backButton, self.shopButton]
        self.map = copy.deepcopy(worldMap)

    def draw(self, app):
        drawMap.draw(self, app, self.lv)

        for button in self.buttons:
            button.draw()

        drawLabel('World Map', app.width // 2, app.tileSize, fill = rgb(210, 175, 90), size = 60, font = 'Ithaca', bold = True, align = 'center')
        drawLabel(str(app.totalMoney), app.width - app.tileSize, app.tileHalf, fill = 'white', size = 26, font = 'Ithaca', bold = True, align = 'right')
        drawImage('images\goldCoin.png', app.width - app.tileHalf, app.tileHalf, align = 'center')

    def mousePress(self, app, mouseX, mouseY):
        for button in self.buttons:
            if(not button.locked):
                button.mousePress(mouseX, mouseY)

    def toLevel(self, app, lv):
        app.currentScreen = Level(app, lv)

    def back(self, app):
        app.currentScreen = homePage(app)

    def toShop(self, app):
        app.currentScreen = shopPage(app)


class Level:
    levels = [level1, level2, level3, level4, level5]
    def __init__(self, app, lv):
        self.lv = lv
        self.backButton = Button(app.tileHalf, app.tileHalf, 50, 50, 'images\\backButton.png', lambda: self.back(app))
        self.nextWaveButton = Button(app.width - app.tileHalf, app.height - app.tileHalf, 50, 50, 'images\\nextWaveButton.png', lambda: self.callWave(app))
        self.pauseButton = Button(app.tileSize + app.tileHalf, app.tileHalf, 50, 50, 'images\\pauseButton.png', lambda: self.pause())
        self.unpauseButton = Button(app.tileSize + app.tileHalf, app.tileHalf, 50, 50, 'images\\unpauseButton.png', lambda: self.pause())
        self.restartButton = Button(app.tileHalf, app.height - app.tileHalf, 50, 50, 'images\\restartButton.png', lambda: self.restart(app))
        self.changeSpeedButton = Button(2 * app.tileSize + app.tileHalf, app.tileHalf, 50, 50, 'images\\changeSpeedButton.png', lambda: self.changeSpeed(app))
        self.buttons = [self.backButton, self.nextWaveButton, self.pauseButton, self.restartButton, self.changeSpeedButton]
        self.buildButtons = []
        self.buildCosts = []
        self.explosions = []
        self.towers = {}
        self.map = copy.deepcopy(Level.levels[lv - 1])
        self.run = True
        self.building = False
        self.m = money[lv - 1]
        self.hp = app.hp
        self.rangeStat = [False]
        self.waves = copy.deepcopy(enemyWave[lv - 1])
        self.thisWave = [0, 0, 0, 0]
        self.enemyLoc = []
        self.count = 0
        self.enemies = []
        self.waveComplete = True
        self.bullets = []

    def draw(self, app):
        drawMap.draw(self, app, self.lv)
        self.drawRange(self.rangeStat)

        for co in self.towers:
            self.towers[co].draw(app)

        for i in range(len(self.enemies)):
            if(self.enemies[i].dead):
                self.enemies[i].draw(app)
        
        for i in range(len(self.enemies) - 1, -1, -1):
            if(not self.enemies[i].dead):
                self.enemies[i].draw(app)

        for bullet in self.bullets:
            if(bullet[2]):
                drawLine(bullet[0][0], bullet[0][1], bullet[1][0], bullet[1][1], fill = 'orange', lineWidth = 5, opacity = 50)
            else:
                drawLine(bullet[0][0], bullet[0][1], bullet[1][0], bullet[1][1], fill = 'gray', lineWidth = 2, opacity = 50)

        for explosion in self.explosions:
            drawImage(explosionImages[explosion[2]], explosion[0][0], explosion[0][1], 
                      width = app.tileSize * explosion[1] // 32, height = app.tileSize * explosion[1] // 32, align = 'center')

        for button in self.buttons:
            button.draw()

        if(self.building):
            for button in self.buildButtons:
                button.draw()
            if(self.buildCosts != []):
                drawLabel(self.buildCosts[0][0], self.buildCosts[0][1], self.buildCosts[0][2], size = 20, font = 'Ithaca', align = 'center')
                drawLabel(self.buildCosts[0][0], self.buildCosts[0][1], self.buildCosts[0][2], 
                          fill = rgb(210, 175, 90), size = 16, font = 'Ithaca', align = 'center')
                drawLabel(self.buildCosts[1][0], self.buildCosts[1][1], self.buildCosts[1][2], size = 20, font = 'Ithaca', align = 'center')
                drawLabel(self.buildCosts[1][0], self.buildCosts[1][1], self.buildCosts[1][2], 
                          fill = rgb(210, 175, 90), size = 16, font = 'Ithaca', align = 'center')
                if(len(self.buildCosts) > 2):
                    drawLabel(self.buildCosts[2][0], self.buildCosts[2][1], self.buildCosts[2][2], size = 20, font = 'Ithaca', align = 'center')
                    drawLabel(self.buildCosts[2][0], self.buildCosts[2][1], self.buildCosts[2][2], 
                              fill = rgb(210, 175, 90), size = 16, font = 'Ithaca', align = 'center')

        drawLabel(str(self.m), app.width - app.tileSize, app.tileHalf, fill = 'white', size = 26, font = 'Ithaca', bold = True, align = 'right')
        drawImage('images\silverCoin.png', app.width - app.tileHalf, app.tileHalf, align = 'center')
        drawLabel(str(self.hp), 4 * app.tileSize, app.tileHalf, fill = 'white', size = 26, font = 'Ithaca', bold = True, align = 'left')
        if(self.hp / app.hp >= 0.67):
            drawImage('images/hp100.png', 3 * app.tileSize + app.tileHalf, app.tileHalf, align = 'center')
        elif(self.hp / app.hp >= 0.33):
            drawImage('images/hp70.png', 3 * app.tileSize + app.tileHalf, app.tileHalf, align = 'center')
        else:
            drawImage('images/hp30.png', 3 * app.tileSize + app.tileHalf, app.tileHalf, align = 'center')
    
    def mousePress(self, app, mouseX, mouseY):
        for button in self.buttons:
            if(not button.locked):
                button.mousePress(mouseX, mouseY)

        if(self.building):
            for button in self.buildButtons:
                if(not button.locked):
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
            self.count = (self.count + 1) % (app.stepsPerSecond * 6)
            if(self.thisWave != [0, 0, 0, 0]):
                if(self.count % enemySpawnRate[self.lv - 1][len(enemyWave[self.lv - 1]) - len(self.waves) - 1] == 0):
                    if(self.thisWave[0] > 0):
                        self.enemies.append(Enemy(app, self.map, start[self.lv], 0))
                        self.thisWave[0] -= 1
                    elif(self.thisWave[1] > 0):
                        self.enemies.append(Enemy(app, self.map, start[self.lv], 1))
                        self.thisWave[1] -= 1
                    elif(self.thisWave[2] > 0):
                        self.enemies.append(Enemy(app, self.map, start[self.lv], 2))
                        self.thisWave[2] -= 1
                    else:
                        self.enemies.append(Enemy(app, self.map, start[self.lv], 3))
                        self.thisWave[3] -= 1
            
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
                        app.currentScreen = settlePage(app, False, self.lv, None)
                else:
                    i += 1

            if(not self.waveComplete and self.count % app.moneyRate == 0):
                self.m += 1

            j = 0
            while j < len(self.explosions):
                self.explosions[j][3] = (self.explosions[j][3] + 1) % 6
                if(self.explosions[j][3] == 5):
                    if(self.explosions[j][2] == 4):
                        self.explosions.pop(j)
                        continue
                    self.explosions[j][2] += 1
                j += 1

            k = 0
            while k < len(self.bullets):
                self.bullets[k][3] += 1
                if((self.bullets[k][3] == 8 and self.bullets[k][2]) or (self.bullets[k][3] == 5 and not self.bullets[k][2])):
                    self.bullets.pop(k)
                else:
                    k += 1

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
                            self.bullets.append([(towerX, towerY), self.enemyLoc[i], True, 0])
                            self.explosions.append([self.enemyLoc[i], thisStat[7], 0, 0])
                            for j in range(len(self.enemyLoc)):
                                if(j == i or self.enemyLoc[j] == 0):
                                    continue
                                if(self.getRange(self.enemyLoc[i], self.enemyLoc[j], thisStat[7]) and not self.enemies[j].dead):
                                    self.enemies[j].takeDamage(app, thisStat[1])
                                    if(self.enemies[j].dead):
                                        self.m += self.enemies[j].stat[4]
                        else:
                            self.bullets.append([(towerX, towerY), self.enemyLoc[i], False, 0])
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
        self.tower3.locked = app.towerLock[3]
        self.tower6 = Button((col + 1) * app.tileSize + app.tileHalf, row * app.tileSize + app.tileHalf, 50, 50, 
                             towerButtonImages[6], lambda: self.buildTower(app, row, col, 6))
        self.tower6.locked = app.towerLock[6]
        self.buildButtons = [self.tower0, self.tower3, self.tower6]
        self.buildCosts = [[towerStat[0][4], (col - 1) * app.tileSize + app.tileHalf, (row + 1) * app.tileSize],
                           [towerStat[3][4], col * app.tileSize + app.tileHalf, row * app.tileSize],
                           [towerStat[6][4], (col + 1) * app.tileSize + app.tileHalf, (row + 1) * app.tileSize]]

    def upgrade(self, app, row, col, type):
        self.building = True
        x = col * app.tileSize + app.tileHalf
        y = row * app.tileSize + app.tileHalf
        self.sell = Button(x, y - app.tileSize, 50, 50, 'images/sellButton.png', lambda: self.sellTower(app, row, col, type))
        self.buildButtons = [self.sell]
        self.rangeStat = [True, x, y, towerStat[type][3]]
        self.buildCosts = []
        if(type % 3 == 0):
            self.towerUpgrade1 = Button(x - app.tileSize, y, 50, 50, towerButtonImages[type + 1], lambda: self.buildTower(app, row, col, type + 1))
            self.towerUpgrade1.locked = app.towerLock[type + 1]
            self.towerUpgrade2 = Button(x + app.tileSize, y, 50, 50, towerButtonImages[type + 2], lambda: self.buildTower(app, row, col, type + 2))
            self.towerUpgrade2.locked = app.towerLock[type + 2]
            self.buildButtons.extend([self.towerUpgrade1, self.towerUpgrade2])
            self.buildCosts = [[towerStat[type + 1][4], (col - 1) * app.tileSize + app.tileHalf, (row + 1) * app.tileSize],
                                [towerStat[type + 2][4], (col + 1) * app.tileSize + app.tileHalf, (row + 1) * app.tileSize]]

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
                    app.currentScreen = settlePage(app, True, self.lv, reward[self.lv - 1][1])
                else:
                    app.levelComplete[self.lv - 1] = True
                    app.totalMoney += reward[self.lv - 1][0]
                    app.currentScreen = settlePage(app, True, self.lv, reward[self.lv - 1][0])
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

    def changeSpeed(self, app):
        if(app.stepsPerSecond == 60):
            app.stepsPerSecond = 30
        else:
            app.stepsPerSecond = 60

class settlePage:
    def __init__(self, app, victory, lv, reward):
        self.lv = lv
        self.victory = victory
        self.reward = reward
        self.backButton = Button(app.tileHalf, app.tileHalf, 50, 50, 'images/backButton.png', lambda: self.back(app))
        if(victory):
            self.nextLevelButton = Button(11 * app.tileSize + app.tileHalf, 7 * app.tileSize + app.tileHalf, 50, 50, 
                                          'images/nextWaveButton.png', lambda: self.nextLevel(app))
            self.restartButton = Button(8 * app.tileSize + app.tileHalf, 7 * app.tileSize + app.tileHalf, 50, 50, 
                                        'images/restartButton.png', lambda: self.restart(app))
            self.buttons = [self.backButton, self.nextLevelButton, self.restartButton]
        else:
            self.restartButton = Button(app.width // 2, 7 * app.tileSize + app.tileHalf, 50, 50, 'images/restartButton.png', lambda: self.restart(app))
            self.buttons = [self.backButton, self.restartButton]

    def draw(self, app):
        if(self.victory):
            drawRect(0, 0, app.width, app.height, fill = 'lightGreen')
            drawLabel('Level Complete', app.width // 2, app.tileSize, fill = rgb(210, 175, 90), font = 'Ithaca', size = 60, bold = True)
            drawLabel('Reward:', app.width // 2, app.tileSize * 4 + app.tileHalf, fill = rgb(210, 175, 90), font = 'Ithaca', size = 30)
            drawLabel('+' + str(self.reward), app.width // 2 - app.tileHalf, app.tileSize * 5 + app.tileHalf, 
                      fill = 'white', font = 'Ithaca', size = 26, align = 'right')
            drawImage('images\goldCoin.png', app.width // 2 + app.tileHalf, app.tileSize * 5 + app.tileHalf, width = 48, height = 48, align = 'center')
        else:
            drawRect(0, 0, app.width, app.height, fill = 'pink')
            drawLabel('Level Failed', app.width // 2, app.tileSize, fill = rgb(210, 175, 90), font = 'Ithaca', size = 60, bold = True)

        for button in self.buttons:
            button.draw()

        if(self.victory):
            drawLabel(f"{app.totalMoney - self.reward}(+{self.reward})", app.width - app.tileSize, app.tileHalf, 
                      fill = 'white', size = 26, font = 'Ithaca', bold = True, align = 'right')
        else:
            drawLabel(str(app.totalMoney), app.width - app.tileSize, app.tileHalf, 
                      fill = 'white', size = 26, font = 'Ithaca', bold = True, align = 'right')
            
        drawImage('images\goldCoin.png', app.width - app.tileHalf, app.tileHalf, align = 'center')

    def mousePress(self, app, mouseX, mouseY):
        for button in self.buttons:
            button.mousePress(mouseX, mouseY)

    def back(self, app):
        app.currentScreen = levelPage(app)

    def nextLevel(self, app):
        if(len(app.levelComplete) == self.lv):
            app.currentScreen = levelPage(app)
        else:
            app.currentScreen = Level(app, self.lv + 1)

    def restart(self, app):
        app.currentScreen = Level(app, self.lv)

class shopPage:
    def __init__(self, app):
        self.backButton = Button(app.tileHalf, app.tileHalf, 50, 50, 'images/backButton.png', lambda: self.back(app))
        self.buyTower3 = Button(8 * app.tileSize, 5 * app.tileSize + app.tileHalf, 50, 50, 'images/tower3Button.png', lambda: self.buy(app, 2))
        self.buyTower4 = Button(10 * app.tileSize, 9 * app.tileSize + app.tileHalf, 50, 50, 'images/tower4Button.png', lambda: self.buy(app, 3))
        self.buyTower5 = Button(10 * app.tileSize, 7 * app.tileSize + app.tileHalf, 50, 50, 'images/tower5Button.png', lambda: self.buy(app, 4))
        self.buyTower5.locked = app.towerLock[3]
        self.buyTower6 = Button(10 * app.tileSize, 5 * app.tileSize + app.tileHalf, 50, 50, 'images/tower6Button.png', lambda: self.buy(app, 5))
        self.buyTower6.locked = app.towerLock[3]
        self.buyTower7 = Button(12 * app.tileSize, 9 * app.tileSize + app.tileHalf, 50, 50, 'images/tower7Button.png', lambda: self.buy(app, 6))
        self.buyTower8 = Button(12 * app.tileSize, 7 * app.tileSize + app.tileHalf, 50, 50, 'images/tower8Button.png', lambda: self.buy(app, 7))
        self.buyTower8.locked = app.towerLock[6]
        self.buyTower9 = Button(12 * app.tileSize, 5 * app.tileSize + app.tileHalf, 50, 50, 'images/tower9Button.png', lambda: self.buy(app, 8))
        self.buyTower9.locked = app.towerLock[6]
        self.buttons = [self.backButton, self.buyTower3, self.buyTower4, self.buyTower5, self.buyTower6, self.buyTower7, self.buyTower8, self.buyTower9]
        self.backgroundImage = backgroundImages[random.randint(0, 3)]

    def draw(self, app):
        drawImage(self.backgroundImage, 0, 0, width = app.width, height = app.height)
        drawLabel('Shop', app.width // 2, app.tileSize, fill = rgb(210, 175, 90), size = 60, font = 'Ithaca', bold = True, align = 'center')
        drawLabel(str(app.totalMoney), app.width - app.tileSize, app.tileHalf, fill = 'white', size = 26, font = 'Ithaca', bold = True, align = 'right')
        drawImage('images\goldCoin.png', app.width - app.tileHalf, app.tileHalf, align = 'center')
        drawRect(8 * app.tileSize, 7 * app.tileSize + app.tileHalf, 5, 4 * app.tileSize, fill = 'gray', align = 'center', opacity = 50)
        drawRect(10 * app.tileSize, 7 * app.tileSize + app.tileHalf, 5, 4 * app.tileSize, fill = 'gray', align = 'center', opacity = 50)
        drawRect(12 * app.tileSize, 7 * app.tileSize + app.tileHalf, 5, 4 * app.tileSize, fill = 'gray', align = 'center', opacity = 50)
        drawImage('images/tower1Button.png', 8 * app.tileSize, 9 * app.tileSize + app.tileHalf, align = 'center')
        drawImage('images/tower2Button.png', 8 * app.tileSize, 7 * app.tileSize + app.tileHalf, align = 'center')

        index = 0
        for i in range(3):
            for j in range(2, -1, -1):
                if(not app.towerLock[index]):
                    drawLabel("Owned", app.tileSize * (i * 2 + 8), app.tileSize * (j * 2 + 6), 
                              font = 'Ithaca', size = 20, align = 'center')
                    drawLabel("Owned", app.tileSize * (i * 2 + 8), app.tileSize * (j * 2 + 6), 
                              fill = rgb(210, 175, 90), font = 'Ithaca', size = 16, align = 'center')
                else:
                    drawLabel(str(towerPrice[index]), app.tileSize * (i * 2 + 8), app.tileSize * (j * 2 + 6), 
                              font = 'Ithaca', size = 20, align = 'center')
                    drawLabel(str(towerPrice[index]), app.tileSize * (i * 2 + 8), app.tileSize * (j * 2 + 6), 
                              fill = rgb(210, 175, 90), font = 'Ithaca', size = 16, align = 'center')
                index += 1

        for button in self.buttons:
            button.draw()

    def mousePress(self, app, mouseX, mouseY):
        for button in self.buttons:
            if(not button.locked):
                button.mousePress(mouseX, mouseY)

    def back(self, app):
        app.currentScreen = levelPage(app)

    def buy(self, app, type):
        if(app.towerLock[type]):
            if(app.totalMoney >= towerPrice[type]):
                app.towerLock[type] = False
                app.totalMoney -= towerPrice[type]
                if(type == 3):
                    self.buyTower5.locked = False
                    self.buyTower6.locked = False
                elif(type == 6):
                    self.buyTower8.locked = False
                    self.buyTower9.locked = False