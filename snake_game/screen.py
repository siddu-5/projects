#building a screen and designing & moving a block

import pygame
from pygame.locals import *

def draw_block():
    surface.fill((110,110,5))
    surface.blit(block,(block_x,block_y))
    pygame.display.flip()
    
    
if __name__=="__main__":
    pygame.init()
    
    surface=pygame.display.set_mode((500,500))
    surface.fill((110,110,5))
    pygame.display.flip()
    
    block = pygame.image.load("snake_game/resources/block.jpg").convert()
    block_x=100
    block_y=100
    surface.blit(block,(block_x,block_y))
    pygame.display.flip()
    
    
    run=True
    while(run):
        for event in pygame.event.get(): #gives all keyboard,mouse events
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    run=False
                if event.key==K_UP:
                    block_y-=10
                    draw_block()
                
                if event.key==K_DOWN:
                    block_y+=10
                    draw_block()
                    
                if event.key==K_LEFT:
                    block_x-=10
                    draw_block()
                    
                if event.key==K_RIGHT:
                    block_x+=10
                    draw_block()
                    
            elif event.type==QUIT:
                run=False