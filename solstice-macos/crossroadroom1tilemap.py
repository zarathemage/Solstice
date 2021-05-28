import pygame

from tilemap import *

from ochreslab import *
from ochredoubleheightslab import *
from ochrefloor import *

class CrossRoadRoom1Tilemap(TileMap):
    def __init__(self):
        TileMap.__init__(self)
        
        self.map = [
            [0,0,2,0,0],
            [0,0,1,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            ]
        
        self.tilewidth = 48
        self.tileheight = 48

        self.mapwidth = 5
        self.mapheight = 5

        self.ochredoubleslab = 2
        self.ochreslab = 1
        self.floortile = 0

        self.x = -100
        self.y = 200
    
        self.tilemap = []

        for j in range(0,self.mapheight):
            self.tilemap.append([])
            for i in range(0, self.mapwidth):
                if self.map[i][j] == 2:
                    ### NOTE zpos 20
                    self.tilemap[j].append(OchreDoubleHeightSlab(self.x+i*self.tilewidth, self.y+j*self.tileheight, 20, self.tilewidth, self.tileheight))
                if self.map[i][j] == 1:
                    ### NOTE zpos 10
                    self.tilemap[j].append(OchreSlab(self.x+i*self.tilewidth, self.y+j*self.tileheight, 10, self.tilewidth, self.tileheight))
                if self.map[i][j] == 0:
                    self.tilemap[j].append(OchreFloor(self.x+i*self.tilewidth, self.y+j*self.tileheight, self.tilewidth, self.tileheight))
        
    def getcurrenttile(self, player, tilemap):
        ### kludge : test left,right,up and down tile
        for j in range(0,len(self.map)):
            for i in range(0,len(self.map[j])):
                t = player.matchTile(self.tilemap[i][j], tilemap)
                if t:
                    return t

        return None

    def blit(self, screen):
        k = self.mapwidth*self.tilewidth
        ###for j in range(0, self.mapheight):
        j = self.mapheight-1
        while j >= 0:
            k += self.tilewidth            
            ###for i in range(0, self.mapwidth):
            i = 0 ###self.mapwidth-1
            while i < self.mapwidth:### >= 0:
                if self.map[i][j] == self.ochredoubleslab:
                    screen.blit(self.tilemap[i][j].image, [k+i*self.tilewidth+self.x, j*self.tileheight+self.y])
                if self.map[i][j] == self.ochreslab:
                    screen.blit(self.tilemap[i][j].image, [k+i*self.tilewidth+self.x, j*self.tileheight+self.y])
                if self.map[i][j] == self.floortile:
                    screen.blit(self.tilemap[i][j].image, [k+i*self.tilewidth+self.x, j*self.tileheight+self.y])
                i += 1
            j -= 1


    def checkboundaries(self, player):
        ### under upper tiles (north wall)
        if player.y > 100: ## FIXME coord
            return True
        
        ### FIXME fix y2,y1,x2,x1 for this room coords
        if not self.leftDiagonalSolution(100,100,150,50,
                                         player.x, player.y):
            return True
        else:
            return False
            
