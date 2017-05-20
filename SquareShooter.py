#Game States

class gameObj():
    xCord = 100
    yCord = 100
    width = 20
    height = 20
    color = [0, 0, 0]
    def __init__(self, x = 100, y = 100, xSize = 20, ySize = 20, col = [0,0,0]):
        self.xCord = x
        self.yCord = y
        self.width= xSize
        self.height = ySize
        self.color = col
    def move(self, x, y):
        self.xCord += x
        self.yCord += y
    def display(self):
        return [self.xCord, self.yCord, self.width, self.height]
    def collide(self, other):
        if not (((self.xCord + self.width) < other.xCord) or (self.xCord > (other.xCord + other.height)) or ((self.yCord + self.height) <  (other.yCord)) or ((self.yCord) > (other.yCord + other.height))):
            return True
    def outBounds(self):
        if self.xCord > 700 or self.xCord < 0:
            return True
        if self.yCord > 500 or self.yCord < 0:
            return True
        return False
    def update():
        return

class player(gameObj):
    lives = 4
    def lifePowerUp(self):
        self.lives += 1
    def shoot(self):
        return bullet(self.xCord, self.yCord, 10, 10, [0,0,255])

class bullet(gameObj):
    gameTime = 0.0
    gameTime2 = 1.0
    originX = 0
    originY = 0
    start = 0
    def __init__(self, x, y, xSize, ySize, col):
        self.xCord = x + 8
        self.yCord = y
        self.size_x = xSize
        self.size_y = ySize
        self.color = col
        self.originX = x + 8
        self.originY = y
        self.width = 5
    def update(self):
        self.yCord -= 4 

class enemy(gameObj):
    gameTime = 0.0
    def update(self):
        self.yCord += 2
        self.xCord += 5 * cos(self.yCord / 10.0)


class level1():
    size = (700, 500)
    WHITE = (255, 255, 255)
    BLACK = (0, 0,0)
    done = False
    pObj = player()
    bList = []
    bLSize = 0
    eneList = []
    eneLSize = 0
    directionX = 0
    directionY = 0
    enemyGenerator = 19
    
    #def __init(self):
        
    def mainloop(self):
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        while not self.done:
            self.events()
            self.update()
            self.render()
        
    def events(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bList.append(self.pObj.shoot())
                    self.bLSize += 1
                if event.key == pygame.K_DOWN:
                    self.directionY = 5
                if event.key == pygame.K_UP:
                    self.directionY = -5
                if event.key == pygame.K_LEFT:
                    self.directionX = -5
                if event.key == pygame.K_RIGHT:
                    self.directionX = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.directionY = 0
                if event.key == pygame.K_UP:
                    self.directionY = 0
                if event.key == pygame.K_LEFT:
                    self.directionX = 0
                if event.key == pygame.K_RIGHT:
                    self.directionX = 0
        self.pObj.move(self.directionX, self.directionY)
        
    def update(self):
        for x in range(0, self.bLSize):
            self.bList[x].update()
        x = 0
        while x < self.bLSize:
            if self.bList[x].outBounds():
                del self.bList[x]
                self.bLSize -= 1
            else:
                x += 1
        x = 0
        while x < self.eneLSize:
            if self.eneList[x].outBounds():
                del self.eneList[x]
                self.eneLSize -= 1
            else:
                x += 1
                
        x = 0

        for x in range(0, self.eneLSize):
            self.eneList[x].update()


        x=0
        while x < self.bLSize:
            y = 0
            while y < self.eneLSize:
                if self.eneList[y].collide(self.bList[x]):
                    del self.eneList[y]
                    del self.bList[x]
                    self.eneLSize -= 1
                    self.bLSize -= 1
                    y = 0
                    return
                else:
                    y += 1
            x += 1
            
        self.enemyGenerator += 1
       
        if self.enemyGenerator == 300:
            self.eneList.append(enemy(random.randrange(20, 460), 20, 20, 20))
            self.eneLSize += 1
            self.enemyGenerator = random.randrange(100, 300)
        
    def render(self):
        self.screen.fill(self.BLACK)

        pygame.draw.rect(self.screen, self.WHITE, self.pObj.display(), 2)


        
        for x in range(0, self.bLSize):
            pygame.draw.rect(self.screen, [255, 0 , 0], self.bList[x].display(), 2)

        for x in range(0, self.eneLSize):
            pygame.draw.rect(self.screen, [0, 255 , 0], self.eneList[x].display(), 2)
    
        pygame.display.flip()

        self.clock.tick(60)
        
class engine():
    FirstLevel = level1()
    state = 1
    def mainloop(self):
        if self.state == 1 :
            self.FirstLevel.mainloop()



    
    

import sys, pygame, random
from math import *

pygame.init()

game = engine()


game.mainloop()

pygame.quit()
