import pygame

from aldhebrand import *

from crossroadroom1 import *
from underdarkroom1 import *

from openingscreen import *

class Solstice:
    def __init__(self):
        pygame.init()

        self.WIDTH = 800
        self.HEIGHT = 600
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        pygame.display.set_caption('Solstice : Underdark')
        
        pygame.display.flip()
        pygame.key.set_repeat(100,10)

        self.room = CrossRoadRoom1()
        self.nextroom = None
        self.player = Aldhebrand(340,340,48,48,0, self.room.tilemap.tileheight)
        
        self.openingscreen = OpeningScreen()
        
        self.is_running = True

    def runopening(self):
        self.openingscreen.mainloop_silverhawk(self.SCREEN)
        self.openingscreen.mainloop_authors(self.SCREEN)
        
    def mainloop(self):

        self.runopening()
        
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        self.is_running = False

                    if event.key == pygame.K_LEFT:
                        self.player.moveLeft()
                        ###print(self.player.x)
                        ###print(self.player.y)
                    if event.key == pygame.K_RIGHT:
                        self.player.moveRight()
                    if event.key == pygame.K_DOWN:
                        self.player.moveDown()
                    if event.key == pygame.K_UP:
                        self.player.moveUp()

                    if event.key == pygame.K_x:
                        self.player.jump()
                        
                    if event.key == pygame.K_z:
                        self.player.magiccrystal()

                self.player.update(self.room.tilemap)

                self.nextroom = self.room.exit(self.player, self.SCREEN)
                if self.nextroom != None:
                    self.room = self.nextroom
                    self.nextroom = None
                
                self.SCREEN.fill((0,0,0))
                self.room.blit(self.SCREEN)
                self.player.blit(self.SCREEN)
                pygame.display.flip()

        ###self.SCREEN.fill((0,0,0))
        pygame.quit()
        
if __name__ == "__main__":
    Solstice().mainloop() 
