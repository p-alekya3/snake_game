import pygame
import time
import random
from pygame.locals import *
if __name__=="__main__":
    pygame.init()
    
    #Creating Window
    
    Surface=pygame.display.set_mode((600,600))
    Surface.fill((53,89,11))
    pygame.display.flip()
    running=True
    x=300
    y=300
    a,b=15,0
    f_x,f_y=random.randrange(0,600)//15*15,random.randrange(0,600)//15*15
    clock=pygame.time.Clock()
    body_list=[(x,y)]
    die=False
    font=pygame.font.SysFont("bahnschrift",50)
    score=0
    
    # Creating snake
    
    def snake():
        global x,y,f_x,f_y,die,score
        
        x=(x+a)%600
        y=(y+b)%600
        
        if ((x,y) in body_list) or (x>=600 and y>=600) :
            die=True
        body_list.append((x,y))
        if f_x==x and f_y==y:
            while (f_x,f_y) in body_list:
                f_x,f_y=random.randrange(50,600)//15*15,random.randrange(25,600)//15*15
                score=score+1
        else:
            del body_list[0]
        Surface.fill((53,89,11))
        pygame.draw.rect(Surface,(159,43,104),[f_x,f_y,15,15])
        for (i,j) in body_list:
            pygame.draw.rect(Surface,(176,97,32),[i,j,15,15])
            

        pygame.display.update()
        
    # Score on screen
    
    def show_score(score):
       
        msg1_font=pygame.font.SysFont("arial",25)
        msg1=msg1_font.render("Score: "+str(score),True,(255,255,255))
        Surface.blit(msg1,(0,0))
        pygame.display.update()
        time.sleep(0)
     
    # Game over method
    
    def game_over():
        Surface.fill((255,255,255))
        msg=font.render("GAME OVER!",True,(0,0,0))
        Surface.blit(msg,(600//3,600//3))
        msg1_font=pygame.font.SysFont("arial",25)
        msg1=msg1_font.render("Score: "+str(score),True,(0,0,0))
        Surface.blit(msg1,(600//2,600//2))
        pygame.display.update()
        time.sleep(10)
        pygame.quit()
        quit()

        
    # Running code
    
    while True:
        
        
        
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    if a!=15:
                        a=-15
                    b=0
                    
                elif event.key==pygame.K_RIGHT:
                    if a!=-15:
                        a=+15
                    b=0
                    
                elif event.key==pygame.K_DOWN:
                    a=0
                    if b!=-15:
                        b=+15
                    
                elif event.key==pygame.K_UP:
                    a=0
                    if b!=15:
                        b=-15
                    
                else:
                    continue
                snake()
        if(die):
            game_over()
            
            
            

       
        if(not pygame.event.get()):
            snake()

        show_score(score)
        clock.tick(5)
    pygame.display.update()
            
            

input()       



