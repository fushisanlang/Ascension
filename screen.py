import sys
import pygame

#使用pygame之前必须初始化
pygame.init()
pygame.key.set_repeat(10, 15)
weight=1024
height=720
#设置主屏窗口
screen = pygame.display.set_mode(size=(weight,height))
#填充主窗口的背景颜色，参数值RGB（颜色元组）
screen.fill((0,0,0))
#设置图标
logo=pygame.image.load('resoure/imgs/logo.png').convert()  
pygame.display.set_icon(logo)

#设置窗口标题
pygame.display.set_caption('飞升')

#加载字体
f_title = pygame.font.Font('resoure/siyuan-hei.otf',150)
f_second = pygame.font.Font('resoure/siyuan-hei.otf',75)
f_text = pygame.font.Font('resoure/siyuan-hei.otf',20)

def enterGame():
    print("enter")
    sys.exit()

class wordsTitle(pygame.sprite.Sprite):
    #定义构造函数
    def __init__(self,wordStr,location,font,color):
        # 调父类来初始化子类
        pygame.sprite.Sprite.__init__(self)
        self.color=color
        self.word=font.render(wordStr,True,self.color)
        self.rect = self.word.get_rect()
        self.rect.center=location
        
        

titleLocation=(weight/2,height/3)
title=wordsTitle("飞升",titleLocation,f_title,"white")

userLocation=(weight/2,height/3*2)
user=wordsTitle("0",userLocation,f_text,"yellow")

quitLocation=(weight/4*3,height/3*2)
quit=wordsTitle("关闭窗口",quitLocation,f_second,(62.8,	65.1,	53.8))
enterLocation=(weight/4,height/3*2)
enter=wordsTitle("进入游戏",enterLocation,f_second,(62.8,	65.1,	53.8))


helpLocation=(weight/2,10)
help=wordsTitle("通过方向键控制人物移动",helpLocation,f_text,"gray")

 
#crash_result = pygame.sprite.collide_rect(userRect,startGameRect)
global userAndEnterCrashResult 
global userAndQuitCrashResult 
userAndEnterCrashResult= pygame.sprite.collide_rect(user,enter)
userAndQuitCrashResult = pygame.sprite.collide_rect(user,quit)
def drawStartScreenBg():
    global userAndEnterCrashResult 
    global userAndQuitCrashResult 
    screen.fill("black")
    screen.blit(title.word,title.rect.topleft)
    userAndEnterCrashResult = pygame.sprite.collide_rect(user,enter)
    userAndQuitCrashResult = pygame.sprite.collide_rect(user,quit)


    if userAndEnterCrashResult is True:
        enter2=wordsTitle("进入游戏",enterLocation,f_second,"green")
        screen.blit(enter2.word,enter.rect.topleft)
        help2Location=(weight/2,40)
        help2=wordsTitle("点击 空格 进入游戏",help2Location,f_text,"green")
        screen.blit(help2.word,help2.rect.topleft)
    else:
        screen.blit(enter.word,enter.rect.topleft)
        screen.blit(help.word,help.rect.topleft)


    if userAndQuitCrashResult is True:
        quit2=wordsTitle("关闭窗口",quitLocation,f_second,"red")

        screen.blit(quit2.word,quit2.rect.topleft)
        help3Location=(weight/2,40)
        help3=wordsTitle("点击 空格 关闭窗口",help3Location,f_text,"red")
        screen.blit(help3.word,help3.rect.topleft)
    else:
        screen.blit(quit.word,quit.rect.topleft)
        screen.blit(help.word,help.rect.topleft)

# 如果没有下列主循环代码，运行结果会一闪而过
drawStartScreenBg() 
while True:
    site=[0,0]
    for event in pygame.event.get():
        #print(user.rect)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP:
                site[1] -= 2
            if event.key == pygame.K_DOWN:
                site[1] += 2
            if event.key == pygame.K_LEFT:
                site[0] -= 2
            if event.key == pygame.K_RIGHT:
                site[0] += 2
            if event.key == pygame.K_SPACE:
                if userAndEnterCrashResult is True:
                    enterGame()
                 
                if userAndQuitCrashResult is True:
                    sys.exit()
   
    
    drawStartScreenBg()             
          
    user.rect=user.rect.move(site)
    screen.blit(user.word,user.rect)

    while user.rect.centerx > weight-10:
        user.rect=user.rect.move((-1,0))
    while user.rect.centerx < 10:
        user.rect=user.rect.move((1,0))
    while user.rect.centery >  height-10:
        user.rect=user.rect.move((0,-1))
    while user.rect.centery <  10:
        user.rect=user.rect.move((0,1))

    
    pygame.display.flip()
 
 