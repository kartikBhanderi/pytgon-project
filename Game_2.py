# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 18:32:23 2020
@author: kartik
"""



import pygame
import time
import random

pygame.init()

def play():
    
    display_width = 800
    display_height = 600
    final_score=0
       
    background = pygame.image.load('pakku.png')
       
    black = (0,0,0)
   # white = (255,255,255)
    red = (255,0,0)
    #green=(0,255,0)
    blue=(0,0,255)
    bright_red=(247,124,124)
    bright_blue = (162, 154, 227)
    #bgcolor=(226, 225, 235)
       
    car_width = 73
       
    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('A bit Racey')
    clock = pygame.time.Clock()
       
    carImg = pygame.image.load('racecar.png')
       
    def showbd():
        gameDisplay.blit(background,(0,0))
       
    def things(thingx, thingy, thingw, thingh, color):
        pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
        #gameDisplay.blit(carImg,(thingx,thingy))
       
    def car(x,y):
        gameDisplay.blit(carImg,(x,y))
       
    def text_objects(text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()
       
    def message_display(text,score):
        largeText = pygame.font.Font('freesansbold.ttf',70)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
       
        nx = display_width/2
        ny = display_height/2+60
        text = "Your Score : "+str(score)
       
        largeText = pygame.font.Font('freesansbold.ttf',30)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center=(nx,ny)
        gameDisplay.blit(TextSurf, TextRect)
       
        pygame.display.update()
       
        time.sleep(2)
        pygame.quit()
       
       
       
       
    #green=(0,255,0)
    bright_green=(0,200,0)
       
    def checkexit(score):
        mouse = pygame.mouse.get_pos()
       
        if(mouse[0]>690 and mouse[0]<790 and mouse[1]>0 and mouse[1]<50):
            click = pygame.mouse.get_pressed()
            if(click[0]==1):    
                exitt(score)
                return True
        return False
       
    def button(msg,x,y,w,h,ic,ac):
        mouse = pygame.mouse.get_pos()
       
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        else:
            pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
       
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        gameDisplay.blit(textSurf, textRect)
       
       
       
    def crash(score):
        message_display('You Crashed',score)
       
    def exitt(score):
        message_display('See you soon',score)
       
    def disscore(score):
        font=pygame.font.Font('freesansbold.ttf',20)
        text=font.render("Score : "+str(score),True,bright_red)
        gameDisplay.blit(text,(1,1))
       
  
    x = (display_width * 0.45)
    y = (display_height * 0.8)
   
    x_change = 0
   
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100
    passed=0
   
    newcol = (25, 5, 181)
    choosecolor=[black,newcol,red,bright_green,blue]
    ind=random.randint(0,4)
   
    gameExit = False
   
    while not gameExit:
   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #pygame.quit()
                gameExit=True
               # quit()
   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -7
                if event.key == pygame.K_RIGHT:
                    x_change = 7
   
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
   
        x += x_change
        #gameDisplay.fill(bgcolor)
        showbd()
   
        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, choosecolor[ind])
        thing_starty += thing_speed
        car(x,y)
   
        if x > display_width - car_width or x < 0:
            crash(final_score)
   
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(20,display_width-thing_width-20)
           
            passed+=1
            final_score+=1+int(passed/10)
            thing_speed*=1.03
            ind=random.randint(0,4)
   
        button("Quit",690,0,100,50,bright_red,red)
        button("Score : "+str(final_score),10,0,100,50,bright_red,red)
        button("",110,0,580,50,bright_blue,bright_blue)
        button("",10,570,780,30,bright_blue,bright_blue)
        HaYaNa = checkexit(final_score)
        if HaYaNa==True:
            break
       
       
        if x > display_width - car_width or x < 0:
            crash(final_score)
            break
            
       
        if y < thing_starty+thing_height:
   
            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                crash(final_score)
                break
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    return final_score

#ans=play()
#print(ans)