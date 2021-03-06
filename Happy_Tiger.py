#-*- coding: utf-8 -*-
#DATE:2018/8/1 9:31
#Date: 2018 / 6 / 2 Time: 10:15
#Author: Darren
import pygame,sys
from pygame.locals import *
import time
#初始化创建
pygame.init()
clock=pygame.time.Clock()
size=width,height=640,480
rgb=[255,255,255]
screen=pygame.display.set_mode(size,RESIZABLE)
screen.fill(rgb)
# font=pygame.font.Font('arial',40)
pygame.display.set_caption('HAPPY TIGER')
background=pygame.image.load('background.jpg').convert()
otiger=pygame.image.load('tiger.png').convert_alpha()
tiger=pygame.image.load('tiger.png').convert_alpha()
otiger_rect=otiger.get_rect()
tiger_rect=tiger.get_rect()

Ptiger = pygame.image.load('tiger.png').convert_alpha()
Ptiger_rect = Ptiger.get_rect()
Ptiger = pygame.transform.rotate(Ptiger, 90)
start=Ptiger_rect.centerx,Ptiger_rect.centery=width-36,36
otiger_rect.right,otiger_rect.top=width,0
speed=[-30,20]
allsize=pygame.display.list_modes()
fullsize=allsize[0]
fullscreen=False
done=False
ratio=1.0
a=0
b=1
# txt='Start'
#创建事件
l_heald=tiger
r_heald=pygame.transform.flip(tiger,True,False)
clarity=150
def tiger_alpha(screens,tigers,positions,clarity):
    tigers_rect=tigers.get_rect()
    x=positions[0]
    y=positions[1]
    temp=pygame.Surface((tigers_rect.width,tigers_rect.height)).convert()
    temp.blit(screens,(-x,-y))
    temp.blit(tigers,(0,0))
    temp.set_alpha(clarity)
    screen.blit(temp,positions)
while True:
    position=otiger_rect.right, otiger_rect.top
    #判断边界碰撞
    if otiger_rect.right>width or otiger_rect.left<0:
        # txt='Touch the boundary'
        otiger=pygame.transform.flip(otiger,True,False)
        otiger_rect=otiger.get_rect()
        otiger_rect.right,otiger_rect.top=position

        speed[0]=-speed[0]

    if otiger_rect.bottom>height or otiger_rect.top<0:
        speed[1]=-speed[1]
        # txt = 'Touch the boundary'

    for event in pygame.event.get():
        if event.type==pygame.QUIT or event.type==pygame.K_ESCAPE:
            sys.exit()
        #键盘控制移动
        elif event.type==KEYDOWN:
            if event.key==K_RIGHT:
                speed[0]=abs(speed[0])
                otiger=r_heald
            elif event.key==K_LEFT:
                speed[0]=-abs(speed[0])
                otiger=l_heald
            elif event.key==K_UP:
                speed[0]*=1.2
                speed[1]*=1.2
            elif event.key==K_DOWN:
                speed[0]*=0.6
                speed[1]*=0.6
        #全屏模式切换
            elif event.key == K_F11:
                fullscreen=not fullscreen
                if fullscreen:
                    screen=pygame.display.set_mode(fullsize,FULLSCREEN)
                    # txt='Full Screen'
                else:
                    screen=pygame.display.set_mode(size)
                    # txt='Exit Full Screen'
        # 调整Tiger尺寸"+"加大，"-"减小
            elif event.key==K_EQUALS or event.key==K_MINUS or event.key==K_SPACE:

                if event.key==K_EQUALS and ratio<4:
                    ratio+=0.6
                    # txt = 'Amplify'
                elif event.key==K_MINUS and ratio>1.3:
                    ratio-=0.8
                    txt='Lessen'
                elif event.key==K_SPACE:
                    ratio=1.0
                    # txt='Resile'
                otiger=pygame.transform.smoothscale(otiger,(int(tiger_rect.width*ratio),
                                                          int(tiger_rect.height*ratio)))
                otiger_rect=otiger.get_rect()
                otiger_rect.right, otiger_rect.top = position
        #沿幕壁行走
            elif event.key==K_s:
                done=not done
                width = screen.get_rect().width
                height = screen.get_rect().height
                start_t=time.clock()
                while done:
                    if Ptiger_rect.centery>height-36 and Ptiger_rect.centerx>=width-36:
                        a=-1
                        b=0
                        Ptiger = pygame.transform.rotate(Ptiger, 270)

                    elif Ptiger_rect.centerx<36 and Ptiger_rect.centery>=height-36:
                        a=0
                        b=-1
                        Ptiger = pygame.transform.rotate(Ptiger, 270)
                    elif Ptiger_rect.centery<36 and Ptiger_rect.centerx<=36:
                        a=1
                        b=0
                        Ptiger = pygame.transform.rotate(Ptiger, 270)
                    elif Ptiger_rect.centerx>width-36 and Ptiger_rect.centery<=36:
                        a=0
                        b=1
                        Ptiger = pygame.transform.rotate(Ptiger, 270)
                    end_t=time.clock()
                    if end_t-start_t>21:
                        Ptiger = pygame.transform.rotate(tiger, 90)
                        break
                    Ptiger_rect = Ptiger.get_rect()
                    Ptiger_rect.centerx, Ptiger_rect.centery = start
                    speedd = [5 * a, 5 * b]
                    Ptiger_rect = Ptiger_rect.move(speedd)
                    start=Ptiger_rect.centerx, Ptiger_rect.centery
                    screen.blit(background, (0, 0))
                    screen.blit(Ptiger,Ptiger_rect)
                    pygame.display.flip()
                    clock.tick(20)

        elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==4:
                clarity+=30
            elif event.button==5:
                clarity-=30
        #调整窗口尺寸
        elif event.type==VIDEORESIZE:
            # txt = 'Change the window\'s format'
            size=event.size
            screen=pygame.display.set_mode(size,VIDEORESIZE | HWSURFACE)
        width = screen.get_rect().width
        height = screen.get_rect().height

    if not done:
        otiger_rect = otiger_rect.move(speed)
        screen.blit(background,(0,0))
        tiger_alpha(screen, otiger, (otiger_rect.left, otiger_rect.top), clarity)

        pygame.display.flip()
        clock.tick(5)
pygame.quit()