import pygame
import random
from animal import *
from landscape import *
from player import Player
from island import * 

def animate():
    global animation_timer,animation_speed,animation_counter
    animation_timer += 1
    if animation_timer > animation_speed:
        animation_counter += 1
        if animation_counter > 2:
            animation_counter = 0
        animation_timer = 0

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
player_type = 1
animation_speed = 5     #This regulates animation speed      
animation_counter = 0
animation_timer = 0
trees_amount = 1
lion_amount = 1

# Spawn Player and Main Island
player = Player(player_type, "Geir", 5, 10, middle_spawn[0], middle_spawn[1])
main_island = Island(screen, island_offset, island_offset, width - island_offset*2, height - island_offset*2 )

def spawn_animals():
    # Spawn Baboons
    # for x in range(2):
    #     Baboon(random.randint(main_island.x, main_island.width+island_offset-5), random.randint(main_island.y, main_island.height+island_offset-5), 3, 100, 5, 5, 5)

    # Spawn Lions
    for x in range(lion_amount):
        Lion(random.randint(main_island.x, main_island.width+island_offset-5), random.randint(main_island.y, main_island.height+island_offset-5), 3, 300, 20, 5, 5)

def create_landscape():
    for x in range(trees_amount):
        Tree(screen, main_island)

spawn_animals()
create_landscape()
running = True
while running:
    #FPS
    clock.tick(60)

    #Animations
    animate()

    #Check for mouse or keyboard clicks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Player Movement
    player.move(main_island, Landscape.all, animation_counter)

    main_island.draw_island(screen)                     #Main Island
    player.draw_player(screen)  

    # Animal movement 
    for animal in Animal.all:
        animal.animal_movement(main_island, screen, animation_counter)

    for x in Landscape.all:
        Landscape.update(x)
       
    pygame.display.update()