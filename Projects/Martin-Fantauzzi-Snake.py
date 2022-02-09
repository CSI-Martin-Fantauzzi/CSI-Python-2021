#create the screen
import pygame
pygame.init()

orange = (196, 10, 10)#Score
green = (255, 128, 0)#Snake
maroon = (228, 19, 19)#Game Over
red = (153, 0, 0)#Food
pine = (51, 0, 0)#Background

dis=pygame.display.set_mode((700,600))

pygame.display.set_caption("Snake game by MF")
game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
    pygame.draw.rect(dis, green,[200, 150, 10, 10])
    pygame.display.update()
pygame.quit()
quit()
