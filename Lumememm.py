import pygame
import sys  

pygame.init()

screen = pygame.display.set_mode([300, 300])
pygame.display.set_caption("Lumemees - Marcus Kosk") 
screen.fill([204, 255, 255])


pygame.draw.circle(screen, [255, 255, 255], (150, 75), 40) # Joonistab lumememme keha
pygame.draw.circle(screen, [255, 255, 255], (150, 150), 50) # Joonistab lumememme keha
pygame.draw.circle(screen, [255, 255, 255], (150, 250), 60) # Joonistab lumememme keha

pygame.draw.circle(screen, [0, 0, 0], (160, 70), 5) # Joonistab lumememme silma
pygame.draw.circle(screen, [0, 0, 0], (140, 70), 5) # Joonistab lumememme silma

pygame.draw.polygon(screen, [255, 165, 0], [[140,78],[160,78],[150,90]], 0) # Joonistab lumememmele nina

pygame.draw.line(screen, [0, 0, 0], [60,190], [100,140]) # Joonistab Lumememme käe 
pygame.draw.line(screen, [0, 0, 0], [240,190], [200,140]) # Joonistab lumeme käe

pygame.draw.circle(screen, [0, 0, 0], (150, 120), 4) # Joonistab lumememme nööbi
pygame.draw.circle(screen, [0, 0, 0], (150, 140), 4) # Joonistab lumememme nööbi
pygame.draw.circle(screen, [0, 0, 0], (150, 160), 4) # Joonistab lumememme nööbi

pygame.draw.line(screen, [0, 0, 0], [120,35], [180,35], 2) # Joonistab lumememme mütsi
pygame.draw.rect(screen, [0, 0, 0], [135, 1, 30, 35], 0) # Joonistab lumememme mütsi

pygame.draw.circle(screen, [255, 255, 0], (265, 30), 20) # Joonistab Päikse
pygame.draw.line(screen, [255, 255, 0], [220,30], [265,27]) # Joonistab päikse kiire
pygame.draw.line(screen, [255, 255, 0], [220,10], [265,27]) # Joonistab päikse kiire
pygame.draw.line(screen, [255, 255, 0], [220,40], [265,27]) # Joonistab päikse kiire
pygame.draw.line(screen, [255, 255, 0], [220,20], [265,27]) # Joonistab päikse kiire
pygame.draw.line(screen, [255, 255, 0], [220,60], [265,27]) # Joonistab päikse kiire
pygame.draw.line(screen, [255, 255, 0], [230,70], [265,27]) # Joonistab päikse kiire
pygame.draw.line(screen, [255, 255, 0], [240,80], [265,27]) # Joonistab päikse kiire

pygame.draw.ellipse(screen, [255, 255, 255], [7, 10, 40, 20], 0) # Joonistab pilve 
pygame.draw.ellipse(screen, [255, 255, 255], [50, 40, 40, 20], 0) # Joonistab pilve 
pygame.draw.ellipse(screen, [255, 255, 255], [45, 10, 40, 20], 0) # Joonistab pilve

pygame.draw.line(screen, [150, 75, 0], [60,240], [60,100], 5) # Joonistab harja pulga
pygame.draw.line(screen, [150, 75, 0], [52,62], [60,100], 2) # Joonistab harja otsa
pygame.draw.line(screen, [150, 75, 0], [56,62], [60,100], 2) # Joonistab harja otsa
pygame.draw.line(screen, [150, 75, 0], [62,62], [60,100], 2) # Joonistab harja otsa
pygame.draw.line(screen, [150, 75, 0], [66,62], [60,100], 2) # Joonistab harja otsa
pygame.draw.line(screen, [150, 75, 0], [72,62], [60,100], 2) # Joonistab harja otsa
pygame.draw.line(screen, [150, 75, 0], [60,62], [60,100], 2) # Joonistab harja otsa







running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
sys.exit()