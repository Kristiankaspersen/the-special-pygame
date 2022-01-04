import pygame
import math

class Player: 
    all = []
    def __init__(self, name, speed, health, x, y, width, height):
        self.name = name
        self.x = x
        self.y = y
        self.speed = speed
        self.health = health
        self.width = width
        self.height = height

        Player.all.append(self)
    
    def draw_player(self, screen):
        color = (0,0,0)
        pygame.draw.rect(screen, color, pygame.Rect(self.x, self.y, self.width, self.height))

    def attack(self): 
        pass


    def move(self, island):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            if keys[pygame.K_LSHIFT]:
                self.x -= math.floor(self.speed/2 * 1.5)
            else:
                self.x -= math.floor(self.speed/2)
            if self.x < island.x:
                self.x = island.x

        if keys[pygame.K_w]:
            if keys[pygame.K_LSHIFT]:
                self.y -= math.floor(self.speed/2 * 1.5)
            else:
                self.y -= math.floor(self.speed/2)
            if self.y < island.y:
                self.y = island.y

        if keys[pygame.K_d]:
            if keys[pygame.K_LSHIFT]:
                self.x += math.floor(self.speed/2 * 1.5)
            else:
                self.x += math.floor(self.speed/2)
            if self.x + self.width > island.width + island.offset:
                self.x = island.width + island.offset - self.width
        
        if keys[pygame.K_s]:
            if keys[pygame.K_LSHIFT]:
                self.y += math.floor(self.speed/2 * 1.5)
            else:
                self.y += math.floor(self.speed/2)
            if self.y + self.height > island.height + island.offset:
                self.y = island.height + island.offset - self.height   

