import pygame
import os, sys
from pygame.locals import *

BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)


class MainGame:

    def __init__(self,width=640,height=640):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width,self.height))

    def GameLoop(self):
        self.LoadSprites();
        pygame.key.set_repeat(500, 30)
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((255,255,255))
        
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    if ((event.key == K_RIGHT)
                    or (event.key == K_LEFT)
                    or (event.key == K_UP)
                    or (event.key == K_DOWN)):
                        self.player.move(event.key)

            Collide1 = pygame.sprite.spritecollide(self.player,self.point_sprites,True)
            self.player.points = self.player.points + len(Collide1)
            
            self.screen.blit(self.background, (0, 0))
            if pygame.font:
                font = pygame.font.Font(None,36)
                text = font.render("Points %s" % self.player.points,1,(0,0,255))
                textpos = text.get_rect(centerx=self.width/2)
                self.screen.blit(text,textpos)
            

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
                self.point_sprites.add(Point(pygame.Rect(x*70,y*70,10,10)))


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([28,28])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.points = 0
        self.x_dist = 8
        self.y_dist = 8

    def move(self, key):
        xMove = 0;
        yMove = 0;

        if (key == K_RIGHT):
            xMove = self.x_dist
        elif (key == K_LEFT):
            xMove = -self.x_dist
        elif (key == K_UP):
            yMove = -self.y_dist
        elif (key == K_DOWN):
            yMove = self.y_dist
        self.rect.move_ip(xMove,yMove);

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


    
    
