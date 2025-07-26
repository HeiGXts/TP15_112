from cmu_graphics import *

class Button:
    def __init__(self, x, y, width, height, image, action):
        self.y = y
        self.x = x
        self.width = width
        self.height = height
        self.image = image
        self.action = action
        self.locked = False

    def draw(self):
        drawImage(self.image, self.x, self.y, width = self.width, height = self.height, align = 'center')

    def mousePress(self, mouseX, mouseY):
        if(self.x - self.width // 2 <= mouseX <= self.x + self.width // 2 and 
           self.y - self.height // 2 <= mouseY <= self.y + self.height // 2 and not self.locked):
            self.action()
            return True