import pygame
import random

class Island(pygame.sprite.Sprite): 
    all = []
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.offset = 100
        self.x = self.offset
        self.y = self.offset
        self.width = screen.get_width() - self.offset*2
        self.height = screen.get_height() - self.offset*2
        self.screen = screen

class Ground(Island):
    def __init__(self, screen):
        super().__init__(screen)
        self.image = pygame.image.load(f"entity/plain_grass.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width,self.height))
        self.rect = self.image.get_rect(topleft = (self.x,self.y))
        self.width = self.rect.right
        self.height = self.rect.bottom

        Island.all.append(self)
        
class Water1(Island):
    def __init__(self, screen, main_island):
        super().__init__(screen)
        self.image = pygame.image.load(f"entity/plain_water.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (main_island.rect.left,self.screen.get_height()))
        self.rect = self.image.get_rect(topleft = (0,0))
        Island.all.append(self)

class Water2(Island):
    def __init__(self, screen, main_island):
        super().__init__(screen)
        self.image = pygame.image.load(f"entity/plain_water.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.screen.get_width(), main_island.rect.top))
        self.rect = self.image.get_rect(topleft = (0,0))
        Island.all.append(self)

class Water3(Island):
    def __init__(self, screen, main_island):
        super().__init__(screen)
        self.image = pygame.image.load(f"entity/plain_water.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.screen.get_width(), self.offset))
        self.rect = self.image.get_rect(topleft = (0, main_island.rect.bottom))  
        Island.all.append(self)

class Water4(Island):
    def __init__(self, screen, main_island):
        super().__init__(screen)
        self.image = pygame.image.load(f"entity/plain_water.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.offset, self.screen.get_height()))
        self.rect = self.image.get_rect(topleft = (main_island.rect.right, 0))
        Island.all.append(self)
        

 
