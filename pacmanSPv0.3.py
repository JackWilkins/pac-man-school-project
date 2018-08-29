import pygame
import os, sys

BLUE = (0,255,0)
RED = (255,0,0)

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

            self.point_sprites.draw(self.screen)
            self.player_sprites.draw(self.screen)
            pygame.display.flip()

    def LoadSprites(self):
        self.player = Player()
        self.player_sprites = pygame.sprite.RenderPlain((self.player))

        HorizontalP = int(self.width/64)
        VerticalP = int(self.height/64)

        self.point_sprites = pygame.sprite.Group()

        for x in range(HorizontalP):
            for y in range(VerticalP):
                self.point_sprites.add(Point(pygame.Rect(x*64,y*64,64,64)))


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([28,28])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.points = 0

class Point(pygame.sprite.Sprite):

    def __init__(self,rect = None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10,10])
        self.image.fill(RED)
        if rect != None:
            self.rect = rect
        


if __name__ == "__main__":
    MainWindow = MainGame()
    MainWindow.GameLoop()      


    
    
