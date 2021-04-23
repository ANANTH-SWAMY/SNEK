import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
black = (0, 0, 0)
 
width = 600
height = 400
 
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('SNEK')
 
clock = pygame.time.Clock()
 
block = 10
#speed = 15

 
font = pygame.font.SysFont("bahnschrift", 25)
font_small = pygame.font.SysFont("bahnschrift", 15)



 
def u_score(score):
    value = font.render("SCORE: " + str(score), True, white)
    win.blit(value, [0, 0])
 
 
 
def main_snek(block, snek_list):
    for x in snek_list:
        pygame.draw.rect(win, white, [x[0], x[1], block, block])
        
        
 

 
def gameLoop(sped):

    speed = sped
    gameover = False
    game_exit = False
 
    x1 = width / 2
    y1 = height / 2
 
    x1_change = 0
    y1_change = 0
 
    snek_list = []
    length_snek = 1
 
    foodx = round(random.randrange(0, width - block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - block) / 10.0) * 10.0
 
    while not gameover:

        

        while game_exit == True:
            win.fill(black)
            
            win.blit(font.render("GAME OVER",True,white) ,[233,100])
            win.blit(font.render("PRESS C TO CONTINUE",True,white) ,[180,200])

            u_score(length_snek - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        main_menu()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key==pygame.K_a:
                    x1_change = -block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT or event.key==pygame.K_d:
                    x1_change = block
                    y1_change = 0
                elif event.key == pygame.K_UP or event.key==pygame.K_w:
                    y1_change = -block
                    x1_change = 0
                elif event.key == pygame.K_DOWN or event.key==pygame.K_s:
                    y1_change = block
                    x1_change = 0
                elif event.key == pygame.K_ESCAPE:
                    paused()
 
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_exit = True
            
        x1 += x1_change
        y1 += y1_change
        win.fill(black)
        pygame.draw.rect(win, white, [foodx, foody, block, block])
        snek_hed = []
        snek_hed.append(x1)
        snek_hed.append(y1)
        snek_list.append(snek_hed)
        if len(snek_list) > length_snek:
            del snek_list[0]
 
        
 
        main_snek(block, snek_list)
        u_score(length_snek - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - block) / 10.0) * 10.0
            length_snek += 1
            
 
        clock.tick(speed)
 
    pygame.quit()
    quit()




def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


 
def main_menu():
    
    
    click = False 
    
    
    while True:
 
        win.fill((0,0,0))
        draw_text('SNEK', font, (255, 255, 255), win, 265, 20)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(197, 100, 200, 50)
        button_2 = pygame.Rect(197, 200, 200, 50)
        

        if button_1.collidepoint((mx, my)):
            if click:
                options()

        if button_2.collidepoint((mx, my)):
            if click:
                leave()

        pygame.draw.rect(win, white, button_1)
        win.blit(font.render("PLAY",True,black) , [265,110])
        
        pygame.draw.rect(win, white, button_2)
        win.blit(font.render("QUIT",True,black) , [270,210])

        

        click = False
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                leave()        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True 
 
        pygame.display.update()
 



def leave():
    pygame.quit()



def options():
    
    click = False
    
    while True:
        
        win.fill(black)
        mx, my = pygame.mouse.get_pos()
        
        
        win.blit(font.render("SPEED",True,white) , [263,20])
        
        button_back=pygame.Rect(10,366,100,25)
        pygame.draw.rect(win, white, button_back)
        win.blit(font_small.render("BACK",True,black) , [40,370])


        button_lvl1=pygame.Rect(197,100,200,25)
        button_lvl2=pygame.Rect(197,150,200,25)
        button_lvl3=pygame.Rect(197,200,200,25)
        button_lvl4=pygame.Rect(197,250,200,25)
        button_lvl5=pygame.Rect(197,300,200,25)

        pygame.draw.rect(win, white, button_lvl1)
        pygame.draw.rect(win, white, button_lvl2)
        pygame.draw.rect(win, white, button_lvl3)
        pygame.draw.rect(win, white, button_lvl4)
        pygame.draw.rect(win, white, button_lvl5)
        
        win.blit(font_small.render("LVL 1",True,black) , [280,100])
        win.blit(font_small.render("LVL 2",True,black) , [280,150])
        win.blit(font_small.render("LVL 3",True,black) , [280,200])
        win.blit(font_small.render("LVL 4",True,black) , [280,250])
        win.blit(font_small.render("LVL 5",True,black) , [280,300])
        
        if button_back.collidepoint((mx, my)):
            if click:
                main_menu()

        if button_lvl1.collidepoint((mx, my)):
            if click:
                gameLoop(10)
                

        if button_lvl2.collidepoint((mx, my)):
            if click:
                gameLoop(15)

        if button_lvl3.collidepoint((mx, my)):
            if click:
                gameLoop(20)

        if button_lvl4.collidepoint((mx, my)):
            if click:
                gameLoop(25)

        if button_lvl5.collidepoint((mx, my)):
            if click:
                gameLoop(30)
                    
        
        click = False
        
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                leave()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        pygame.display.update()



def paused():
    

    win.fill(black)
    draw_text('PAUSED', font, white, win, 255, 20)
    
    button_resume=pygame.Rect(197, 100, 200, 50)
    button_quit = pygame.Rect(197, 200, 200, 50)

    pygame.draw.rect(win, white, button_resume)
    win.blit(font.render("RESUME",True,black) , [255,110])
    
    pygame.draw.rect(win, white, button_quit)
    win.blit(font.render("QUIT",True,black) , [270,210])

    click = False
    paused = True
    
    pygame.display.update()

    while paused:
        mx,my = pygame.mouse.get_pos()

        if button_resume.collidepoint((mx,my)):
            if click:
                paused = False
        if button_quit.collidepoint((mx,my)):
            if click:
                main_menu()        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                leave()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
    
    clock.tick(10)
                    
main_menu()
