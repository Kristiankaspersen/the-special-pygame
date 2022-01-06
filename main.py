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
island_offset = 100      #Distance from edge of screen to island
player_type = 1
animation_speed = 5     #This regulates animation speed      
animation_counter = 0
animation_timer = 0
grass_amount = 1000
trees_amount = 50
lion_amount = 20

# Create Island Ground and water covering the ground
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

# Create player
player = pygame.sprite.GroupSingle()
player.add(Player(player_type, "Geir", screen))

# Create landscape objects
grass_objects = pygame.sprite.Group()
for x in range(grass_amount):
    grass_objects.add(Grass(screen, main_island))  

landscape_objects = pygame.sprite.Group()
for x in range(trees_amount):
    landscape_objects.add(Tree(screen, main_island))  

# Create animals
animals = pygame.sprite.Group()
for x in range(lion_amount):
    animals.add(Lion(screen, main_island, landscape_objects))         

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

    #Draw Main everything
    ground_object.draw(screen)
    water_object1.draw(screen)
    water_object2.draw(screen)
    water_object3.draw(screen)
    water_object4.draw(screen)
    grass_objects.draw(screen)

    player.update(main_island, landscape_objects, animation_counter)
    player.draw(screen)

    animals.update(main_island, landscape_objects, animation_counter)
    animals.draw(screen)

    landscape_objects.update()
    landscape_objects.draw(screen)
       
    pygame.display.update()