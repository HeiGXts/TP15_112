from cmu_graphics import *
from map import *

def draw(self, app, lv):
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                imageIndex = self.map[i][j]
                imageX = app.tileHalf + j * app.tileSize
                imageY = app.tileHalf + i * app.tileSize
                if(type(imageIndex) == int):
                    drawImage(images[imageIndex], imageX, imageY, width = app.tileSize, height = app.tileSize, align = 'center')
        
        row, col = start[lv]
        drawPath(self, app, (0, 0), self.map[row][col], (row, col))

        for button in self.buttons:
            button.draw()

        if(self.building):
            for button in self.buildButtons:
                button.draw()
    
def drawPath(self, app, ldir, ndir, co):
    lrow, lcol = ldir
    nrow, ncol = ndir
    row, col = co
    img = 'images\path'
    if(lrow == 0 and nrow == 0):
        img += 'LR.png'
    elif(lcol == 0 and ncol == 0):
        img += 'TD.png'
    elif((lrow == 1 and ncol == 1) or (lcol == -1 and nrow == -1)):
        img += 'TR.png'
    elif((lrow == 1 and ncol == -1) or (lcol == 1 and nrow == -1)):
        img += 'TL.png'
    elif((lcol == -1 and nrow == 1) or (lrow == -1 and ncol == 1)):
        img += 'DR.png'
    elif((lcol == 1 and nrow == 1) or (lrow == -1 and ncol == -1)):
        img += 'DL.png'
    drawImage(img, col * app.tileSize + app.tileHalf, row * app.tileSize + app.tileHalf, width = app.tileSize, height = app.tileSize, align = 'center')
    row, col = row + nrow, col + ncol
    if(ndir != (0, 0)):
        drawPath(self, app, ndir, self.map[row][col], (row, col))