import pygame
import sys  

pygame.init()

screen = pygame.display.set_mode([300, 600])
pygame.display.set_caption("Foor - Marcus Kosk")

pygame.draw.rect(screen, [0, 225, 0], [100, 20, 100, 230], 2)
pygame.draw.circle(screen, [245, 22, 22], (150, 65), 33)
pygame.draw.circle(screen, [255, 255, 0], (150, 137), 33)
pygame.draw.circle(screen, [0, 255, 0], (150, 210), 33)
pygame.draw.rect(screen, [255, 255, 255], [135, 250, 30, 500], 0)
pygame.draw.polygon(screen, [255, 255, 255], [[100,600],[134,500],[134,600]], 0)
pygame.draw.polygon(screen, [255, 255, 255], [[199,600],[165,500],[165,600]], 0)
pygame.draw.rect(screen, [0, 0, 0], [125, 550, 50, 20], 0)
pygame.draw.rect(screen, [0, 0, 255], [125, 530, 50, 20], 0)
pygame.draw.rect(screen, [0, 0, 0], [125, 570, 50, 20], 2)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

sys.exit()