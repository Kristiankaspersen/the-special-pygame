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

# Spawn Player and Main Island
player = Player("Geir", 4, 10, middle_spawn[0], middle_spawn[1], 10, 10)
main_island = Island(60, 60, width - 60*2, height - 60*2 )

# Spawn Baboons
for x in range(500):
    Baboon(random.randint(main_island.x, main_island.width+60-5), random.randint(main_island.y, main_island.height+60-5), 3, 100, 5, 5, 5)

running = True
while running:
    #FPS
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Player Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x > main_island.x:
            player.x -= player.speed
        if keys[pygame.K_w] and player.y > main_island.y:
            player.y -= player.speed
        if keys[pygame.K_d] and player.x + player.width < main_island.x + main_island.width:
            player.x += player.speed
        if keys[pygame.K_s] and player.y + player.height < main_island.y + main_island.height:
            player.y += player.speed


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