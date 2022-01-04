import pygame
import random
from animal import Baboon
from animal import Animal
from player import Player
from island import Island 

#Initiate Pygame
pygame.init()

#Window and Game settings
clock = pygame.time.Clock()
width = 1000
height = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("The Baboon Island")

#Graphics
water_surface =  pygame.image.load("ocean.jpg")
island_surface = pygame.image.load("grass.jpg")

# Useful variables
middle_spawn = [width/2,height/2]
island_offset = 60                  #Distance from edge of screen to island

# Spawn Player and Main Island
player = Player("Geir", 5, 10, middle_spawn[0], middle_spawn[1], 10, 10)
main_island = Island(island_offset, island_offset, width - island_offset*2, height - island_offset*2 )

# Spawn Baboons
for x in range(20):
    Baboon(random.randint(main_island.x, main_island.width+island_offset-5), random.randint(main_island.y, main_island.height+island_offset-5), 3, 100, 5, 5, 5)

running = True
while running:
    #FPS
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Player Movement
    player.move(main_island)

    screen.fill((70,188,239))                           #Simple water covering the entire screen
    #screen.blit(water_surface,(0,0))                   #Testing realistic water    
    main_island.draw_island(screen, island_surface)     #Main Island
    player.draw_player(screen)                          #Player

    # Animal movement 
    for animal in Animal.all:
        animal.animal_movement(main_island)
    for animal in Animal.all:
        animal.draw_animal(screen)
       
    pygame.display.update()