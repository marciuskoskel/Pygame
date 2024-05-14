import pygame
import sys

# Initsialiseeri Pygame
pygame.init()

# Mängu seaded
screen_width = 640
screen_height = 480
background_color = (255, 255, 255)  

# Palli seaded
ball_image = pygame.image.load('ball.png')
ball_rect = ball_image.get_rect()
ball_speed_x = 3
ball_speed_y = 3

# Aluse seaded
paddle_image = pygame.image.load('pad.png')
paddle_rect = paddle_image.get_rect()
paddle_rect.y = screen_height / 1.5
paddle_speed = 5

# Alguspunktid
ball_rect.x = screen_width / 2 - ball_rect.width / 2
ball_rect.y = screen_height / 2 - ball_rect.height / 2
paddle_rect.x = (screen_width - paddle_rect.width) / 2

# Skori hoidmine
score = 0

# Loome ekraani
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pall ja Alus Mäng")

# Kell aja hoidmiseks
clock = pygame.time.Clock()

# Mängu peamine tsükkel
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Palli liigutamine
    ball_rect.x += ball_speed_x
    ball_rect.y += ball_speed_y

    # Palli põrkamine seintest
    if ball_rect.left <= 0 or ball_rect.right >= screen_width:
        ball_speed_x = -ball_speed_x
    if ball_rect.top <= 0:
        ball_speed_y = -ball_speed_y
    elif ball_rect.bottom >= screen_height:
        ball_speed_y = -ball_speed_y
        score -= 1  # Negatiivne punkt alumise ääre puudutamisel

    # Palli ja aluse kokkupõrke tuvastamine
    if ball_rect.colliderect(paddle_rect) and ball_speed_y > 0:  # Lisakontroll
        ball_speed_y = -ball_speed_y
        score += 1  # Positiivne punkt aluse puudutamisel

    # Aluse liigutamine
    paddle_rect.x += paddle_speed
    if paddle_rect.left <= 0 or paddle_rect.right >= screen_width:
        paddle_speed = -paddle_speed

    # Ekraani uuendamine
    screen.fill(background_color)
    screen.blit(ball_image, ball_rect)
    screen.blit(paddle_image, paddle_rect)

    # Skori kuvamine
    font = pygame.font.SysFont(None, 36)
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Uuenda ekraani
    pygame.display.flip()
    clock.tick(60)  # Piira kaadrisagedus 60 FPS-ile
