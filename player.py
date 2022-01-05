import pygame
import math
import random

class Player: 
    all = []
    def __init__(self, style, name, speed, health, x, y):
        self.style = style
        self.name = name
        self.x = x
        self.y = y
        self.speed = speed
        self.health = health
        self.surface = pygame.image.load(f"characters/Player{style}/F.png").convert_alpha()
        self.player_rect = self.surface.get_rect(topleft = (self.x,self.y))

        Player.all.append(self)
    
    def draw_player(self, screen):
        self.player_rect = self.surface.get_rect(topleft = (self.x,self.y))
        screen.blit(self.surface,self.player_rect)

    def attack(self): 
        pass

    def check_collision(self, landscape):
        for x in landscape:
            return self.player_rect.colliderect(x.rect)
            #TEST pygame.sprite.collide_rect_ratio()


    def move(self, island, landscape, num):
        self.width = self.surface.get_width()
        self.height = self.surface.get_height()
        keys = pygame.key.get_pressed()

        #Move left
        if keys[pygame.K_a]:
            images = ["L.png", "LR.png", "LL.png"]
            self.surface = pygame.image.load(f"characters/Player{self.style}/{images[num]}").convert_alpha()
            if keys[pygame.K_LSHIFT]:
                self.x -= math.floor(self.speed/2 * 1.5)
                if self.check_collision(landscape):
                    self.x += math.floor(self.speed/2 * 1.5 + 1)
            else:
                self.x -= math.floor(self.speed/2)
                if self.check_collision(landscape):
                    self.x += math.floor(self.speed/2 + 1)
            if self.x < island.x:
                self.x = island.x
        
        #Move up
        if keys[pygame.K_w]:
            images = ["B.png", "BR.png", "BL.png"]
            self.surface = pygame.image.load(f"characters/Player{self.style}/{images[num]}").convert_alpha()
            if keys[pygame.K_LSHIFT]:
                self.y -= math.floor(self.speed/2 * 1.5)
                if self.check_collision(landscape):
                    self.y += math.floor(self.speed/2 * 1.5 + 1)
            else:
                self.y -= math.floor(self.speed/2)
                if self.check_collision(landscape):
                    self.y += math.floor(self.speed/2 + 1)
            if self.y < island.y:
                self.y = island.y

        #Move Right
        if keys[pygame.K_d]:
            images = ["R.png", "RR.png", "RL.png"]
            self.surface = pygame.image.load(f"characters/Player{self.style}/{images[num]}").convert_alpha()
            if keys[pygame.K_LSHIFT]:
                self.x += math.floor(self.speed/2 * 1.5)
                if self.check_collision(landscape):
                    self.x -= math.floor(self.speed/2 * 1.5 + 1)
            else:
                self.x += math.floor(self.speed/2)
                if self.check_collision(landscape):
                    self.x -= math.floor(self.speed/2 + 1)
            if self.x + self.width > island.width:
                self.x = island.width - self.width
        
        #Move down
        if keys[pygame.K_s]:
            images = ["F.png", "FR.png", "FL.png"]
            self.surface = pygame.image.load(f"characters/Player{self.style}/{images[num]}").convert_alpha()
            if keys[pygame.K_LSHIFT]:
                self.y += math.floor(self.speed/2 * 1.5)
                if self.check_collision(landscape):
                    self.y -= math.floor(self.speed/2 * 1.5 + 1)
            else:
                self.y += math.floor(self.speed/2)
                if self.check_collision(landscape):
                    self.y -= math.floor(self.speed/2 + 1)
            if self.y + self.height > island.height:
                self.y = island.height - self.height   

