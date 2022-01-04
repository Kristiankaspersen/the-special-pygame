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

islandX = 60
islandY = 60
middle_spawn = [width/2,height/2]

# Spawn Player and Main Island
player = Player("Geir", 4, 10, middle_spawn[0], middle_spawn[1], 10, 10)
main_island = Island(islandX, islandY, width - islandX*2, height - islandY*2 )

# Spawn Baboons
for x in range(50):
    Baboon(random.randint(main_island.x, main_island.width), random.randint(main_island.y, main_island.height), 3, 100, 5, 5, 5)

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


    screen.fill((70,188,239))       #This is currently the water covering the entire screen
    main_island.drawIsland(screen)  #Main Island
    player.drawPlayer(screen)       #Player

    # Animal movement 
    for animal in Animal.all:
        animal.animal_movement(main_island)
    for animal in Animal.all:
        animal.draw_animal(screen)
       

    pygame.display.update()