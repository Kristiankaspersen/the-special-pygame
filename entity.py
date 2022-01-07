import pygame 
import random

class Entity(pygame.sprite.Sprite): 
    all = []
    def __init__(self, screen, island):
        super().__init__()
        self.island = island
        self.screen = screen
        self.solid = False

    def update(self):
        pass

    def spawn_collision(self, player):
        if self.rect.colliderect(player.sprite.rect):
            self.kill()
        for entity in Entity.all:
            if entity.solid == True:
                if self.rect != entity.rect:
                    if self.rect.colliderect(entity.rect):
                        self.kill()
                        break

    def on_island(self, island):
        x = random.randint(island.x, island.width-10)
        y = random.randint(island.y+5, island.height) 
        return x, y

    def off_island(self):
        for x in self.location:
            water_object = x
        
        x = random.randint(water_object.rect.left+6, water_object.rect.right-10)
        y = random.randint(water_object.rect.top+8, water_object.rect.bottom)
        return x,y

class Tree(Entity):
    all = []
    def __init__(self, screen, island):
        super().__init__(screen, island)
        self.type = "tree"
        self.tree_type = random.randint(1,4)
        self.solid = True

        self.x_midbot, self.y_midbot = self.on_island(island)
        self.image = pygame.image.load(f"entity/tree{self.tree_type}.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = (self.x_midbot, self.y_midbot))

        Entity.all.append(self)
        Tree.all.append(self)

        #Used to make sure trees do not spawn on top of each other. Should be optimized.
        # self.spawn_collision()

    def chopped(self):
        print("I got chopped")

class Grass(Entity):
    all = []
    def __init__(self, screen, island):
        super().__init__(screen, island)
        self.type = "grass"
        self.grass_type = random.randint(1,4)

        self.x_midbot, self.y_midbot = self.on_island(island)
        self.image = pygame.image.load(f"entity/grass{self.grass_type}.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = (self.x_midbot, self.y_midbot))

        Entity.all.append(self)
        Grass.all.append(self)

class Water_effect(Entity):
    all = []
    def __init__(self, screen, island, water_object1, water_object2, water_object3, water_object4):
        super().__init__(screen, island)
        self.type = "water_effect"
        self.location = random.choice([water_object1, water_object2, water_object3, water_object4])
        self.x_midbot, self.y_midbot = self.off_island()
        self.image = pygame.image.load(f"entity/water_effect1.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = (self.x_midbot, self.y_midbot))

        Entity.all.append(self)
        Water_effect.all.append(self)
