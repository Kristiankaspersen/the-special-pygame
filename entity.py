import pygame 
import random

class Entity(pygame.sprite.Sprite): 
    all = []
    def __init__(self, screen, island):
        super().__init__()
        self.island = island
        self.screen = screen
        self.solid = False

    def update(self, player, animal):
        self.respawn(player, animal)

    def spawn_collision(self, player):
        if self.rect.colliderect(player.sprite.rect):
            self.kill()
        for entity in Entity.all:
            if entity.solid == True:
                if self.rect != entity.rect:
                    if self.rect.colliderect(entity.rect):
                        self.kill()
                        break

    def respawn(self, player, animals):
        if self.type == "tree":
            if self.ischopped and pygame.time.get_ticks() - self.chopped_timer > 10000:
                for animal in animals:
                    if self.original_rect.colliderect(animal.rect):
                        pass
                if self.original_rect.colliderect(player.sprite.rect):
                    pass
                else:
                    self.image = pygame.image.load(f"entity/tree{self.tree_type}.png").convert_alpha()
                    self.rect = self.image.get_rect(midbottom = (self.x_midbot, self.y_midbot))
                    self.health = 5
                    self.ischopped = False

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
        self.solid = True
        self.type = "tree"
        self.health = 5
        self.ischopped = False
        self.tree_type = random.randint(1,4)

        self.tree_falling_sound = pygame.mixer.Sound("audio/tree_falling.wav")
        self.tree_falling_sound.set_volume(0.3)
        
        self.x_midbot, self.y_midbot = self.on_island(island)
        self.image = pygame.image.load(f"entity/tree{self.tree_type}.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = (self.x_midbot, self.y_midbot))
        self.original_rect = self.rect

        Entity.all.append(self)
        Tree.all.append(self)

    def chopped(self):
        self.tree_falling_sound.play()
        self.ischopped = True
        self.chopped_timer = pygame.time.get_ticks()
        self.image = pygame.image.load(f"entity/stub1.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = (self.x_midbot, self.y_midbot))

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
