import pygame
import math

class Player(pygame.sprite.Sprite): 
    all = []
    def __init__(self, style, name, screen):
        super().__init__()
        screen = screen
        self.style = style
        self.name = name
        self.x = screen.get_width()/2
        self.y = screen.get_height()/2
        self.speed = 5
        self.health = 10
        self.image = pygame.image.load(f"characters/Player{style}/F.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = (self.x,self.y))
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, 5)

        Player.all.append(self)

    def player_collision(self, landscape_objects):
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, 5)
        for x in landscape_objects:
            if self.hitbox.colliderect(x.rect):
                return True

    def update(self, island, landscape_objects, num):
        self.island = island
        self.num = num
        self.player_input(landscape_objects)
        self.rect = self.image.get_rect(topleft = (self.rect.x,self.rect.y))

    def attack(self): 
        pass

    def player_input(self, landscape_objects):
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        keys = pygame.key.get_pressed()

        #Move left
        if keys[pygame.K_a]:
            images = ["L.png", "LR.png", "LL.png"]
            self.image = pygame.image.load(f"characters/Player{self.style}/{images[self.num]}").convert_alpha()
            if keys[pygame.K_LSHIFT]:
                self.rect.x -= math.floor(self.speed/2 * 1.5)
                if self.player_collision(landscape_objects):
                    self.rect.x += math.floor(self.speed/2 * 1.5)
            else:
                self.rect.x -= math.floor(self.speed/2)
                if self.player_collision(landscape_objects):
                    self.rect.x += math.floor(self.speed/2)
            if self.rect.x < self.island.x:
                self.rect.x = self.island.x
        
        #Move up
        if keys[pygame.K_w]:
            images = ["B.png", "BR.png", "BL.png"]
            self.image = pygame.image.load(f"characters/Player{self.style}/{images[self.num]}").convert_alpha()
            if keys[pygame.K_LSHIFT]:
                self.rect.y -= math.floor(self.speed/2 * 1.5)
                if self.player_collision(landscape_objects):
                    self.rect.y += math.floor(self.speed/2 * 1.5)
            else:
                self.rect.y -= math.floor(self.speed/2)
                if self.player_collision(landscape_objects):
                    self.rect.y += math.floor(self.speed/2)
            if self.rect.y < self.island.y:
                self.rect.y = self.island.y

        #Move Right
        if keys[pygame.K_d]:
            images = ["R.png", "RR.png", "RL.png"]
            self.image = pygame.image.load(f"characters/Player{self.style}/{images[self.num]}").convert_alpha()
            if keys[pygame.K_LSHIFT]:
                self.rect.x += math.floor(self.speed/2 * 1.5)
                if self.player_collision(landscape_objects):
                    self.rect.x -= math.floor(self.speed/2 * 1.5)
            else:
                self.rect.x += math.floor(self.speed/2)
                if self.player_collision(landscape_objects):
                    self.rect.x -= math.floor(self.speed/2)
            if self.rect.x + self.width > self.island.width:
                self.rect.x = self.island.width - self.width
        
        #Move down
        if keys[pygame.K_s]:
            images = ["F.png", "FR.png", "FL.png"]
            self.image = pygame.image.load(f"characters/Player{self.style}/{images[self.num]}").convert_alpha()
            if keys[pygame.K_LSHIFT]:
                self.rect.y += math.floor(self.speed/2 * 1.5)
                if self.player_collision(landscape_objects):
                    self.rect.y -= math.floor(self.speed/2 * 1.5)
            else:
                self.rect.y += math.floor(self.speed/2)
                if self.player_collision(landscape_objects):
                    self.rect.y -= math.floor(self.speed/2)
            if self.rect.y + self.height > self.island.height:
                self.rect.y = self.island.height - self.height   

