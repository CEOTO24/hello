import pygame
import time
import math

pygame.init()
pygame.display.set_caption(" clock vip pro")

screen = pygame.display.set_mode((500,600))

YELLOW=(255, 255, 204)
RED=(255, 0, 0)
BLACK=(51, 51, 0)
WHITE=(255, 255, 255)

font=pygame.font.SysFont('sans',50)
text_1 = font.render('+', True , BLACK)
text_2 = font.render('-', True , BLACK)
text_3 = font.render('+', True , BLACK)
text_4 = font.render('-', True , BLACK)
text_5 = font.render('Start', True , BLACK)
text_6 = font.render('Reset', True , BLACK)


running = True
total_secs=0
total=0
start = False
sound1=pygame.mixer.Sound('cheer.wav')
sound2=pygame.mixer.Sound('tick.wav')

while running:

    screen.fill(YELLOW)

    mouse_x , mouse_y = pygame.mouse.get_pos()
 #   print(f" x: {mouse_x} y: {mouse_y} ")

    pygame.draw.rect(screen, RED , (80,50,50,50))
    pygame.draw.rect(screen, RED , (80,200,50,50))
    pygame.draw.rect(screen, RED , (180,50,50,50))
    pygame.draw.rect(screen, RED , (180,200,50,50)) 
    pygame.draw.rect(screen, RED , (280,50,150,50))
    pygame.draw.rect(screen, RED , (280,200,150,50))

    screen.blit(text_1,(95,45))
    screen.blit(text_2,(95,195))
    screen.blit(text_3,(195,45))
    screen.blit(text_4,(195,195))
    screen.blit(text_5,(295,45))
    screen.blit(text_6,(295,195))

    pygame.draw.rect(screen, BLACK , (50,520,400,50))
    pygame.draw.rect(screen, WHITE , (60,530,380,30))

    pygame.draw.circle(screen, BLACK , (250,400),100)
    pygame.draw.circle(screen, WHITE , (250,400),90)
    pygame.draw.circle(screen, BLACK , (250,400),10)

 #   pygame.draw.line(screen, BLACK , (250,400),(250,310))
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if(80 < mouse_x <130) and (50 < mouse_y < 100):
                    total_secs += 60
                    total=total_secs
                    print("press + min")
                if(80 < mouse_x < 130) and (200 < mouse_y < 250):
                    total_secs -=60
                    total=total_secs
                    print("press - min")
                if(180 < mouse_x <230) and (50 < mouse_y < 100):
                    total_secs +=1
                    total=total_secs
                    print("press + sec")
                if(180 < mouse_x < 230) and (200 < mouse_y < 250):
                    total_secs -=1
                    total=total_secs
                    print("press - sec")
                if(280 < mouse_x <430) and (50 < mouse_y < 100):
                    start = True
                    total=total_secs
                    print("press Start")
                if(280 < mouse_x <430) and (200 < mouse_y < 250):
                    total_secs=0
                    total=total_secs
                    print("press Reset")

    # cho thoi gian giam
    if start:
        if total_secs >0 :
            pygame.mixer.Sound.play(sound2)
            total_secs-=1
            time.sleep(1)
        else:
            pygame.mixer.Sound.play(sound1)
            start = False

    if total_secs < 0:
        total_secs = 0

    #tinh thoi gian
    mins = int (total_secs/60)
    secs = total_secs - mins*60

    time_now = str(mins) + "   :   "+ str(secs)

    text_time = font.render(time_now, True, BLACK)
    screen.blit(text_time, (90,120))

    # hinh chu nhat
    if total != 0:
        pygame.draw.rect(screen, RED,(60,530,int(380*(total_secs/total)),30))

    # dong ho
    x_sec = 250 + 90*math.sin(6* secs * math.pi/180)
    y_sec = 400 - 90*math.cos(6* secs * math.pi/180)
    pygame.draw.line(screen, BLACK, (250,400), (int(x_sec), int(y_sec)))

    x_min = 250 + 50*math.sin(6* mins * math.pi/180)
    y_min = 400 - 50*math.cos(6* mins * math.pi/180)
    pygame.draw.line(screen, RED, (250,400), (int(x_min), int(y_min)))    


    pygame.display.flip() 

pygame.quit()



