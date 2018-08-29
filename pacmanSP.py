import pygame
import os, sys

BLUE = (0,255,0)

class MainGame:

    def __init__(self,width=640,height=640):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width,self.height))

    def GameLoop(self):
        self.LoadSprites();

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.player_sprites.draw(self.screen)
            pygame.display.flip()

    def LoadSprites(self):
        self.player = Player()
        self.player_sprites = pygame.sprite.RenderPlain((self.player))


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([28,28])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.points = 0


if __name__ == "__main__":
    MainWindow = MainGame()
    MainWindow.GameLoop()        


    
    
