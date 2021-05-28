import time

class MoveThroughDoorLoopObject:
    def __init__(self):
        self.counter = 10
        
    def move_mainloop(self, player, room, screen):

        while self.counter > 0:
            screen.fill((0,0,0))
            room.blit(screen)
            player.blit(screen)
            self.counter -= 1
            time.sleep(1/100.0)
            ### change player x,y based on playe.lastmove
            player.lastmove.move(player)
