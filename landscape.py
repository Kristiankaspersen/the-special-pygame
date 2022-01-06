import pygame 
import random

class Landscape(pygame.sprite.Sprite): 
    all = []
    def __init__(self, screen, island):
        super().__init__()
        self.island = island
        self.screen = screen

    def update(self):
        pass

    def spawn_collision(self):
        for x in Tree.all:
            for y in Tree.all:
                if x.rect != y.rect:
                    if x.rect.colliderect(y.rect):
                        y.kill()

class Tree(Landscape):
    all = []
    def __init__(self, screen, island):
        super().__init__(screen, island)
        self.tree_type = random.randint(1,4)
        self.x_midbot = random.randint(island.x, island.width-5)
        self.y_midbot = random.randint(island.y+5, island.height)
        self.image = pygame.image.load(f"landscape/tree{self.tree_type}.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = (self.x_midbot, self.y_midbot))

        Landscape.all.append(self)
        Tree.all.append(self)

        #Used to make sure trees do not spawn on top of each other. Should be optimized.
        self.spawn_collision()

class Grass(Landscape):
    all = []
    def __init__(self, screen, island):
        super().__init__(screen, island)
        self.grass_type = random.randint(1,4)
        self.x_midbot = random.randint(island.x, island.width-10)
        self.y_midbot = random.randint(island.y+5, island.height)
        self.image = pygame.image.load(f"landscape/grass{self.grass_type}.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = (self.x_midbot, self.y_midbot))

        Landscape.all.append(self)
        Grass.all.append(self)
