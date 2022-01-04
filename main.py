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
width = 1400
height = 960
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("The Baboon Island")

# Useful variables
middle_spawn = [width/2,height/2]
island_offset = 100      #Distance from edge of screen to island
player_type = 1         #This determines the player model
animation_speed = 5     #This regulates animation speed      
animation_counter = 0
animation_timer = 0

# Spawn Player and Main Island
player = Player(player_type, "Geir", 5, 10, middle_spawn[0], middle_spawn[1])
main_island = Island(island_offset, island_offset, width - island_offset*2, height - island_offset*2 )

# Spawn Baboons
for x in range(20):
    Baboon(random.randint(main_island.x, main_island.width+island_offset-5), random.randint(main_island.y, main_island.height+island_offset-5), 3, 100, 5, 5, 5)

running = True
while running:
    #FPS
    clock.tick(60)
    
    #Handle animation timing
    animation_timer += 1
    if animation_timer > animation_speed:
        animation_counter += 1
        if animation_counter > 2:
            animation_counter = 0
        animation_timer = 0

    #Check for mouse or keyboard clicks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Player Movement
    player.move(main_island, animation_counter)

    screen.fill((70,188,239))                           #Simple water covering the entire screen  
    main_island.draw_island(screen)                     #Main Island
    player.draw_player(screen)                          #Player

    # Animal movement 
    for animal in Animal.all:
        animal.animal_movement(main_island)
    for animal in Animal.all:
        animal.draw_animal(screen)
       
    pygame.display.update()