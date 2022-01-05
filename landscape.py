import pygame 
import random
from island import Island

class Landscape: 
    all = []
    def __init__(self, screen, island):
        island = island
        self.screen = screen

    def update(self):
        self.screen.blit(self.surface,self.rect)

class Tree(Landscape):
    all = []
    def __init__(self, screen, island):
        super().__init__(screen, island)
        self.tree_type = random.randint(1,4)
        self.surface = pygame.image.load(f"landscape/tree{self.tree_type}.png").convert_alpha()
        self.x_midbot = random.randint(island.x, island.width)
        self.y_midbot = random.randint(island.y, island.height)
        self.rect = self.surface.get_rect(midbottom = (self.x_midbot, self.y_midbot))

        Landscape.all.append(self)
        Tree.all.append(self)