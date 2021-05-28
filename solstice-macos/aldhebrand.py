import pygame

from leftmove import *
from rightmove import *
from upmove import *
from downmove import *

class Aldhebrand:
    def __init__(self,x,y,w,h,z, th):
        self.x = x
        self.y = y

        self.width = w
        self.height = h
        
        self.z = z
        
        self.tileheight = th

        self.screenx = self.x ### FIXME 
        self.screeny = self.y ### FIXME
        self.dt = 0.5
        
        self.image = pygame.image.load("./pics/wizard1.png")
        self.image.set_colorkey((255,255,255))

        self.lastmove = None

    def jump(self):
        1

    def magiccrystal(self):
        1

    ### NOTE the movement functions are on the rectified tilemap
    ###      then they get transformed when blitting
    def moveLeft(self):
        self.lastmove = LeftMove()
        self.lastmove.move(self)
###        self.x -= 1
        self.screenx -= 4
        self.screeny -= 4*self.dt

        if self.screeny % self.tileheight * self.dt == 0: ### self.tileheight / 2
            self.y -= 1
        
    def moveRight(self):
        self.lastmove = RightMove()
        self.lastmove.move(self)
###        self.x += 1
        self.screenx += 4
        self.screeny += 4*self.dt
        
        if self.screeny % self.tileheight * self.dt == 0: ### self.tileheight / 2
            self.y += 1

    def moveUp(self):
        self.lastmove = UpMove()
        self.lastmove.move(self)

###        self.x += 1
        self.screenx += 4
        self.screeny -= 4*self.dt
        
        if self.screeny % self.tileheight * self.dt == 0: ### self.tileheight / 2
            self.y -= 1
            
    def moveDown(self):
        self.lastmove = DownMove()
        self.lastmove.move(self)

##        self.x -= 1
        self.screenx -= 4
        self.screeny += 4*self.dt

        if self.screeny % self.tileheight * self.dt == 0: ### self.tileheight / 2
            self.y += 1
        
    def fall(self, tile):
        if tile != None and self.z > tile.z:
            self.fallOnce()

    ### fall several pixels at a time
    def fallOnce(self):
        self.z -= 0.10

    ### check if player is on tile
    def matchTile(self, tile, tilemap):
        if tile.collidexy(self, tilemap):
            return tile
        else:
            return False

    def collide(self, tile, tilemap):
        return tile.collidexy(self,tilemap)

    
    def update(self, tilemap):
        currenttile = tilemap.getcurrenttile(self, tilemap)
        if currenttile != None and currenttile.collidez(self,tilemap) and self.lastmove != None:
            self.lastmove.undomove(self)
            return
        if self.fall(currenttile):
            self.fallOnce()
                
    def blit(self, screen):
        screen.blit(self.image, [self.screenx, self.screeny])

    def warp(self,x,y):
        self.x = x
        self.y = y
