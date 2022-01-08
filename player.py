import pygame
import math
import random

class Player(pygame.sprite.Sprite): 
    all = []
    def __init__(self, style, name, screen):
        super().__init__()
        screen = screen
        self.style = style
        self.name = name
        self.x = screen.get_width()/2
        self.y = screen.get_height()/2
        self.speed = 2
        self.health = 10
        self.image = pygame.image.load(f"characters/Player{style}/F.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = (self.x,self.y))
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)

        self.last_action_time = -1
        self.chop_sounds = [pygame.mixer.Sound("audio/chop1.wav"), pygame.mixer.Sound("audio/chop2.wav"), pygame.mixer.Sound("audio/chop3.wav")]

        Player.all.append(self)

    def player_collision(self):
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, 15, 19)
        for x in self.solid_objects:
            if self.hitbox.colliderect(x.rect):
                return True
        for water_object in self.water_objects:
            for x in water_object:
                if self.hitbox.colliderect(x.rect):
                    return True

    def update(self, island, solid_objects, soft_objects, water_object1, water_object2, water_object3, water_object4, num):
        self.soft_objects = soft_objects
        self.island = island
        self.water_objects = [water_object1, water_object2, water_object3, water_object4]
        self.solid_objects = solid_objects
        self.rect = self.image.get_rect(topleft = (self.rect.x,self.rect.y))
        self.island = island
        self.num = num
        self.player_input()

    def use(self):
        #Check what item is in hand
        if 1==1:
            self.chop_tree()

    def attack(self): 
        pass

    def chop_tree(self):
        closest_tree = []
        player_cx, player_cy = self.rect.centerx, self.rect.centery
        if self.solid_objects:
            for entity in self.solid_objects:
                if entity.type == "tree" and entity.ischopped == False:
                    tree_cx, tree_cy = entity.rect.centerx, entity.rect.centery
                    if not closest_tree:
                        closest_tree = [entity, math.sqrt(abs(player_cx-tree_cx)**2 + abs(player_cy-tree_cy)**2)]
                    else: 
                        distance = math.sqrt(abs(player_cx-tree_cx)**2 + abs(player_cy-tree_cy)**2)
                        if distance < closest_tree[1]:
                            closest_tree = [entity,distance]

        if closest_tree:
            if closest_tree[1] < 30:
                self.last_action_time = pygame.time.get_ticks()
                random.choice(self.chop_sounds).play()
                closest_tree[0].health -= 1     #Better axes can do more damage

                if closest_tree[0].health <= 0:
                    closest_tree[0].chopped()
                closest_tree = []

    def player_input(self):
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        keys = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()

        #Move left
        if keys[pygame.K_a]:
            images = ["L.png", "LR.png", "LL.png"]
            self.image = pygame.image.load(f"characters/Player{self.style}/{images[self.num]}").convert_alpha()
            if keys[pygame.K_LSHIFT]:
                self.rect.x -= math.floor(self.speed * 1.5)
                if self.player_collision():
                    self.rect.x += math.floor(self.speed * 1.5)
            else:
                self.rect.x -= math.floor(self.speed)
                if self.player_collision():
                    self.rect.x += math.floor(self.speed)
        
        #Move up
        if keys[pygame.K_w]:
            images = ["B.png", "BR.png", "BL.png"]
            self.image = pygame.image.load(f"characters/Player{self.style}/{images[self.num]}").convert_alpha()
            if keys[pygame.K_LSHIFT]:
                self.rect.y -= math.floor(self.speed * 1.5)
                if self.player_collision():
                    self.rect.y += math.floor(self.speed * 1.5)
            else:
                self.rect.y -= math.floor(self.speed)
                if self.player_collision():
                    self.rect.y += math.floor(self.speed)

        #Move Right
        if keys[pygame.K_d]:
            images = ["R.png", "RR.png", "RL.png"]
            self.image = pygame.image.load(f"characters/Player{self.style}/{images[self.num]}").convert_alpha()
            if keys[pygame.K_LSHIFT]:
                self.rect.x += math.floor(self.speed * 1.5)
                if self.player_collision():
                    self.rect.x -= math.floor(self.speed * 1.5)
            else:
                self.rect.x += math.floor(self.speed)
                if self.player_collision():
                    self.rect.x -= math.floor(self.speed)
        
        #Move down
        if keys[pygame.K_s]:
            images = ["F.png", "FR.png", "FL.png"]
            self.image = pygame.image.load(f"characters/Player{self.style}/{images[self.num]}").convert_alpha()
            if keys[pygame.K_LSHIFT]:
                self.rect.y += math.floor(self.speed * 1.5)
                if self.player_collision():
                    self.rect.y -= math.floor(self.speed * 1.5)
            else:
                self.rect.y += math.floor(self.speed)
                if self.player_collision():
                    self.rect.y -= math.floor(self.speed) 
        
        if keys[pygame.K_SPACE]:
            if self.last_action_time == -1:
                self.use()
            elif pygame.time.get_ticks() - self.last_action_time > 500:
                self.use()

        if mouse_buttons[0]:
            if self.last_action_time == -1:
                self.use()
            elif pygame.time.get_ticks() - self.last_action_time > 500:
                self.use()
