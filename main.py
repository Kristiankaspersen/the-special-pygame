import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
running = True

#Finn på et navn til spillet
pygame.display.set_caption("NAVN")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255,255,0))
    pygame.display.update()