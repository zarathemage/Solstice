import pygame

from tilemap import *

from ochrecubez import *
from ochrefloor import *

class UnderdarkRoom2Tilemap(TileMap):
    def __init__(self):
        TileMap.__init__(self)

        ### map with (piece, zposition)
        self.map = [
            [(0,0),(1,30),(1,30),(1,30),(0,0)],
            [(0,0),(0,0),(1,20),(0,0),(0,0)],
            [(0,0),(1,10),(1,10),(1,10),(0,0)],
            [(0,0),(0,0),(0,0),(0,0),(0,0)],
            [(0,0),(0,0),(0,0),(0,0),(0,0)],
            ]
        
        self.tilewidth = 48
        self.tileheight = 38

        self.mapwidth = 5
        self.mapheight = 5

        self.ochrecubeslab = 1
        self.floortile = 0

        self.x = -100
        self.y = 200
    
        self.tilemap = []

        for j in range(0,self.mapheight):
            self.tilemap.append([])
            for i in range(0, self.mapwidth):
                if self.map[i][j][0] == 1:
                    ### NOTE zpos 10
                    self.tilemap[j].append(OchreCubeZ(self.x+i*self.tilewidth, self.y+j*self.tileheight, self.map[i][j][1], self.tilewidth, self.tileheight))
                if self.map[i][j][0] == 0:
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
        l = self.tileheight / 2 
        j = self.mapheight-1
        while j >= 0:
            k += self.tilewidth            
            i = self.mapwidth-1
            while i  >= 0:
                if self.map[i][j] == self.ochrecubeslab:
                    screen.blit(self.tilemap[i][j].image, [k+i*self.tilewidth/2+self.x, j*self.tileheight - i*l + self.y - self.map[i][j][1]])
                if self.map[i][j] == self.floortile:
                    screen.blit(self.tilemap[i][j].image, [k+i*self.tilewidth+self.x, j*self.tileheight+ - i*l + self.y])
                i -= 1
            j -= 1

