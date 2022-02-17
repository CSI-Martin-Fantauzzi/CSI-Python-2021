#create the screen
import pygame
pygame.init()

reddish = (196, 10, 10)#Score
orange = (255, 128, 0)#Snake
red = (228, 19, 19)#Game Over
rose = (166, 8, 50)#Food
maroon = (51, 0, 0)#Background

dis=pygame.display.set_mode((700,600))

pygame.display.set_caption("Snake game by MF")
game_over=False

x1 = 300
y1 = 350

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -5
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 5
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -5
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 5
    x1 += x1_change
    y1 += y1_change 
    dis.fill(maroon)
    pygame.draw.rect(dis, orange,[x1, y1, 10, 10])
    pygame.display.update()

    clock.tick(30)
pygame.quit()
quit()
