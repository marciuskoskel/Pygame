import pygame
import sys
pygame.init()

#Värvid
red = [255, 0, 0]
green = [153, 255, 153]

#Ekraani seaded
screen = pygame.display.set_mode([640,480])
pygame.display.set_caption("Ülesanne 3")
screen.fill(green)

# Funktsioon ekraani täisruutude joonistamiseks
def draw_grid(screen, suurus, read, veerud, varv):
    for i in range(read):
        for j in range(veerud):
            pygame.draw.rect(screen, varv, (j * suurus, i * suurus, suurus, suurus), 1)

# Funktsioon, mis käivitab mängu
def run_game(suurus, read, veerud, varv):

    
    #Kutsub funktsiooni välja
    draw_grid(screen, suurus, read, veerud, varv)
    
    #Kasutaja saab panna ristist pygame kinni
    running = True
    while running:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
    #Värskendab ekraani        
        pygame.display.flip()

    pygame.quit()
    sys.exit()

#Kutsub funktsiooni välja
suurus = 20  # Ruudu suurus
read = 50    # Ridu
veerud = 50  # Veerge
varv = (red) # Joone värv
#Kutsub funktsiooni välja
run_game(suurus, read, veerud, varv)