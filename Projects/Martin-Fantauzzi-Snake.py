#create the screen
import pygame
import random
import time
pygame.init()

reddish = (196, 10, 10)#Score
orange = (255, 128, 0)#Snake
red = (228, 19, 19)#Game Over
rose = (166, 8, 50)#Food
maroon = (51, 0, 0)#Background

dis_width = 800
dis_height = 700

dis=pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption("Snake game by MF")
game_over=False

clock = pygame.time.Clock()
snake_speed = 20
snake_block = 10

font_style = pygame.font.SysFont(None, 32)

def my_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,orange, [x[0], x[1], snake_block, snake_block])

def the_score(score):
    value = font_style.render("Score: " + str(score), True, reddish)
    dis.blit(value, [0,0])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/4.1, dis_height/2])

def gameLoop():
    game_over = False
    game_close = False 
    
    x1 = dis_width/2
    y1 = dis_height/2
    
    x1_change = 0
    y1_change = 0

    snake_List = []
    length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10) * 10
    foody = round(random.randrange(0, dis_height - snake_block) / 10) * 10

    while not game_over:
        while game_close == True:
            dis.fill(maroon)
            message('''YOU DIED. Press Q to quit and P to play again.''', red)
            the_score(length_of_snake -1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_q:
                        gameLoop()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 <0:
            game_close = True

        x1 += x1_change
        y1 += y1_change 
        dis.fill(maroon)
        pygame.draw.rect(dis, rose,[foodx, foody, snake_block, snake_block])
        #pygame.draw.rect(dis, orange,[x1, y1, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)
        if len(snake_List) > length_of_snake:
            del snake_List[0]

        for x in snake_List[: -1]:
            if x == snake_head:
                game_close == True

        my_snake(snake_block, snake_List)
        the_score(length_of_snake -1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10) * 10
            foody = round(random.randrange(0, dis_height - snake_block) / 10) * 10
            length_of_snake += 1


        clock.tick(snake_speed)


    pygame.quit()
    quit()

gameLoop() 
