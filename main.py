import pygame
import random
from animal import *
from entity import *
from player import *
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
# width = 1000
# height = 560
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("The Baboon Island")

# Useful variables
island_offset = 100      #Distance from edge of screen to island
player_type = 1
animation_speed = 5     #This regulates animation         speed      
animation_counter = 0
animation_timer = 0
grass_amount = height
trees_amount = 20
lion_amount = 10
fish_amount = 15

def new_game():
    # Create Island Ground and water covering the ground
    global ground_object
    global water_object1
    global water_object2
    global water_object3
    global water_object4

    global solid_objects
    global soft_objects
    global animals
    global player
    global main_island

    #The Island
    ground_object = pygame.sprite.Group()
    ground_object.add(Ground(screen))
    for x in ground_object:
        main_island = x
    water_object1 = pygame.sprite.Group()
    water_object1.add(Water1(screen, main_island))
    water_object2 = pygame.sprite.Group()
    water_object2.add(Water2(screen, main_island))
    water_object3 = pygame.sprite.Group()
    water_object3.add(Water3(screen, main_island))
    water_object4 = pygame.sprite.Group()
    water_object4.add(Water4(screen, main_island))

    #Sprite groups
    player = pygame.sprite.GroupSingle()
    solid_objects = pygame.sprite.Group()
    soft_objects = pygame.sprite.Group()
    animals = pygame.sprite.Group()

    # Create player
    player.add(Player(player_type, "Geir", screen))

    # Create Enteties
    for x in range(100):
        soft_objects.add(Water_effect(screen, main_island, water_object1, water_object2, water_object3, water_object4))
    for x in range(grass_amount):
        soft_objects.add(Grass(screen, main_island))  
    for x in range(trees_amount):
        solid_objects.add(Tree(screen, main_island))  

    # Check if solid objects spawns are valid
    for x in solid_objects:
        Entity.spawn_collision(x, player) 

    # Create animals
    for x in range(lion_amount):
        animals.add(Lion(screen, main_island))   
    for x in range(fish_amount):
        animals.add(Fish(screen, water_object1, water_object2, water_object3, water_object4)) 

    # Check if animal spawns are valid
    for x in Animal.all:
        Animal.spawn_collision(x, solid_objects, water_object1, water_object2, water_object3, water_object4)   

new_game()
game_menu = False       #Will be used later to show game menu
game_paused = False     #Will be used later to show paused screen
game_started = True
running = True
while running:
    #FPS
    clock.tick(60)
    current_time = pygame.time.get_ticks()  #Time in milliseconds after game started

    #Animations
    animate()

    #Check for mouse or keyboard clicks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if game_started:
        #Draw and update everything
        ground_object.draw(screen)
        water_object1.draw(screen)
        water_object2.draw(screen)
        water_object3.draw(screen)
        water_object4.draw(screen)

        soft_objects.draw(screen)

        player.update(main_island, solid_objects, soft_objects, water_object1, water_object2, water_object3, water_object4, animation_counter)
        player.draw(screen)

        animals.update(main_island, solid_objects, water_object1, water_object2, water_object3, water_object4, animation_counter)
        animals.draw(screen)

        solid_objects.update(player, animals)
        solid_objects.draw(screen)

    elif game_paused:
        pass

    elif game_menu:
        pass

    pygame.display.update()