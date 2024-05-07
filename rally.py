import pygame
import random

# Pygame'i initsialiseerimine
pygame.init()

# Ekraani seaded
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Liiklusmäng")

# Värvid
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Pildid
background_image = pygame.image.load("bg_rally.jpg")
red_car_image = pygame.image.load("f1_red.png")
blue_car_image = pygame.image.load("f1.blue.png")

# Punase auto asukoht
red_car_x = (screen_width - red_car_image.get_width()) // 2
red_car_y = screen_height - red_car_image.get_height()

# Siniste autode seaded ja rajad
lanes = [
    screen_width // 4 - blue_car_image.get_width() // 2,  # Esimene rada
    3 * screen_width // 4 - blue_car_image.get_width() // 2  # Teine rada
]
blue_cars = []
for lane in lanes:
    for _ in range(1):  # Igas reas on 2 autot
        x_pos = lane
        y_pos = random.randrange(screen_height, screen_height + 300, step=150)  # Teine auto on kaugemal
        blue_cars.append([x_pos, y_pos])

# Kiirus
blue_car_speed = 5

# Skoor
score = 0
font = pygame.font.Font(None, 36)

# Mängu põhiluup
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Ekraani uuendamine
    screen.blit(background_image, (0, 0))

    # Siniste autode liikumine
    for car in blue_cars:
        car[1] -= blue_car_speed  # Autod liiguvad ülespoole
        if car[1] < -blue_car_image.get_height():
            car[1] = random.randrange(screen_height, screen_height + 300, step=150)  # Autod tulevad tagasi alumisest servast
            score += 1  # Lisame skoori

    # Siniste autode joonistamine
    for car in blue_cars:
        screen.blit(blue_car_image, (car[0], car[1]))

    # Punase auto joonistamine
    screen.blit(red_car_image, (red_car_x, red_car_y))

    # Skoori kuvamine
    score_text = font.render(f"Skoor: {str(score)}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Kuva uuendamine
    pygame.display.flip()

    # Frame'i värskendamise sagedus
    pygame.time.Clock().tick(60)

pygame.quit()

