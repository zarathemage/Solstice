import pygame

class OpeningScreen:
    def __init__(self):
        self.is_running = True
        self.image = pygame.image.load("./pics/silverhawkgamessoftware-3.jpg")
        self.font = pygame.font.SysFont(None, 32)
        self.font2 = pygame.font.SysFont(None, 24)
        self.text = None
        self.text2 = None
        self.textrect = None
        
    def mainloop_silverhawk(self, screen):
        screen.blit(self.image, [screen.get_rect().centerx, screen.get_rect().centery])
        pygame.display.flip()

        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

                if event.type == pygame.MOUSEBUTTONUP or event.type == pygame.KEYUP:
                    self.is_running = False
        screen.fill((0,0,0))


    def mainloop_authors(self, screen):
        self.is_running = True
        
        while self.is_running:
            self.text = self.font.render('Programmed by Johan.', True, (0, 64, 64), (255, 255, 255))
            self.textrect = self.text.get_rect()
            self.textrect.centerx = screen.get_rect().centerx
            self.textrect.centery = screen.get_rect().centery
            screen.blit(self.text, self.textrect)
            self.text2 = self.font.render('Graphics by Johan.', True, (0, 64, 64), (255, 255, 255))
            self.textrect = self.text2.get_rect()
            self.textrect.centerx = screen.get_rect().centerx
            self.textrect.centery = screen.get_rect().centery+32
            screen.blit(self.text2, self.textrect)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

                if event.type == pygame.MOUSEBUTTONUP or event.type == pygame.KEYUP:
                    self.is_running = False

            
            
        screen.fill((0,0,0))
        
        
    
