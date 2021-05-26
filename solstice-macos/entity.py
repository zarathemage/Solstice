import pygame

class Entity:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.image = None ### pygame.image.load("./pics/demon1.png")

    def blit(self, screen):
        screen.blit(self.image, [self.x, self.y])
