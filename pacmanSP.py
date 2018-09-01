import pygame
import os, sys
from pygame.locals import *

BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)



class MainGame:

    def __init__(self,width=672,height=720):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width,self.height))

    def GameLoop(self):
        self.LoadSprites();
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((255,255,255))
        
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.move(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.player.move(1, 0)
                    elif event.key == pygame.K_UP:
                        self.player.move(0, -1)
                    elif event.key == pygame.K_DOWN:
                        self.player.move(0, 1)
 
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.player.move(1, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.player.move(-1, 0)
                    elif event.key == pygame.K_UP:
                        self.player.move(0, 1)
                    elif event.key == pygame.K_DOWN:
                        self.player.move(0, -1)
                        

            Collide1 = pygame.sprite.spritecollide(self.player,self.point_sprites,True)
            self.player.points = self.player.points + len(Collide1)

            
            self.screen.blit(self.background, (0, 0))
            if pygame.font:
                font = pygame.font.Font(None,36)
                text = font.render("Points %s" % self.player.points,1,(0,0,255))
                textpos = text.get_rect(centerx=self.width/2)
                self.screen.blit(text,textpos)
                

            self.all_sprites.update()
            self.all_sprites.draw(self.screen)
            pygame.display.flip()

    def LoadSprites(self):

        level = [
            "                     ",
            " 1111111111111111111 ",
            " 1000000001000000001 ",
            " 1011011101011101101 ",
            " 1020000000000000001 ",
            " 1011010111110101101 ",
            " 1000010001000100001 ",
            " 1111011101011101111 ",
            " 1111010000000101111 ",
            " 1111010111110101111 ",
            " 1000000111110000001 ",
            " 1111010111110101111 ",
            " 1111010000000101111 ",
            " 1111010111110101111 ",
            " 1000000001000000001 ",
            " 1011011101011101101 ",
            " 1001000000000001001 ",
            " 1101010111110101011 ",
            " 1000010001000100001 ",
            " 1011111101011111101 ",
            " 1000000000000000001 ",
            " 1111111111111111111 ",
            "                     "
            ]


        self.all_sprites = pygame.sprite.Group()
        self.point_sprites = pygame.sprite.Group()
        self.wall_sprites = pygame.sprite.Group()
        self.player_sprites = pygame.sprite.Group()
        self.Swidth = 32

        for y, row in enumerate(level):
            for x, item in enumerate(row):
                if item == '1':
                    self.wall = Wall(x*self.Swidth,y*self.Swidth)
                    self.all_sprites.add(self.wall)
                    self.wall_sprites.add(self.wall)
                elif item == '0':
                    self.point = Point(x*self.Swidth,y*self.Swidth)
                    self.all_sprites.add(self.point)
                    self.point_sprites.add(self.point)
                elif item == '2':
                    self.player = Player(x*self.Swidth,y*self.Swidth)
                    self.all_sprites.add(self.player)
                    self.player_sprites.add(self.player)

        self.player.walls = self.wall_sprites
                    


class Player(pygame.sprite.Sprite):

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([32,32])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(topleft=(x,y))
        self.points = 0
        self.x_dist = 0
        self.y_dist = 0
        self.walls = None

    def move(self,x,y):
        self.x_dist += x
        self.y_dist += y

    def update(self):
        self.rect.x += self.x_dist
        block_hit_list = pygame.sprite.spritecollide(self,self.walls,False)
        for block in block_hit_list:
            if self.x_dist > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right

        self.rect.y += self.y_dist
        block_hit_list = pygame.sprite.spritecollide(self,self.walls,False)
        for block in block_hit_list:
            if self.y_dist > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
        
        

class Point(pygame.sprite.Sprite):

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([32,32])
        self.image.fill(RED)
        self.rect = self.image.get_rect(topleft=(x,y))

class Wall(pygame.sprite.Sprite):

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([32,32])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(topleft=(x,y))


if __name__ == "__main__":
    MainWindow = MainGame()
    MainWindow.GameLoop()      


    
    
