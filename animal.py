import pygame 
import random

class Animal(pygame.sprite.Sprite): 
    all = []
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.animal_type = "na" 
        self.animal_name = "Animal"      

        Animal.all.append(self)
    
    def update(self, island, solid_objects, water_object1, water_object2, water_object3, water_object4, animate_num):
        self.water_objects = [water_object1, water_object2, water_object3, water_object4]
        self.solid_objects = solid_objects
        self.island = island
        self.animal_movement(animate_num)
        self.isdead()

    def spawn_collision(self, solid_objects, water_object1, water_object2, water_object3, water_object4):
        water_objects = [water_object1, water_object2, water_object3, water_object4]
        for x in solid_objects:
            for y in self.all:
                if x.rect.colliderect(y.rect):
                    y.kill()
        if self.animal_type == "land":
            for water_object in water_objects:
                for water in water_object:
                    if self.hitbox.colliderect(water.rect):
                        self.kill()

    def collision(self):
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, 22, 19)
        for x in self.solid_objects:
            if self.hitbox.colliderect(x.rect):
                return True
        if self.animal_type == "land":
            for water_object in self.water_objects:
                for water in water_object:
                    if self.hitbox.colliderect(water.rect):
                        return True
        elif self.animal_type == "water":
            if self.hitbox.colliderect(self.island.rect) or self.rect.right > self.screen.get_width() or self.rect.left < 0 \
                or self.rect.bottom > self.screen.get_height() or self.rect.top < 0:
                return True

    def animate(self, images=[], animate_num=-1, move=False):
        if animate_num != -1 and images and move:
            self.image = pygame.image.load(f"animals/{self.animal_name}/{images[animate_num]}").convert_alpha()
    
    def isdead(self):
        if self.health <= 0:
            self.kill()

    def animal_movement(self, animate_num):
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        move_direction = random.randint(1,4)
        num_move = random.randint(1,self.laziness)
        if num_move < 3:
            if move_direction == 1:
                self.rect.x -= self.speed
                if self.collision():
                    self.rect.x += self.speed
                images = ["L.png", "LR.png", "LL.png"]
                self.animate(images, animate_num, True)
            elif move_direction == 2:
                self.rect.y -= self.speed
                if self.collision():
                    self.rect.y += self.speed
                images = ["B.png", "BR.png", "BL.png"]
                self.animate(images, animate_num, True)
            elif move_direction == 3:
                self.rect.x += self.speed
                if self.collision():
                    self.rect.x -= self.speed
                images = ["R.png", "RR.png", "RL.png"]
                self.animate(images, animate_num, True)
            elif move_direction == 4:
                self.rect.y += self.speed
                if self.collision():
                    self.rect.y -= self.speed
                images = ["F.png", "FR.png", "FL.png"]
                self.animate(images, animate_num, True)
        self.animate(animate_num)

    def on_island(self, island):
        x = random.randint(island.x, island.width-10)
        y = random.randint(island.y, island.height-10) 
        return x, y

    def off_island(self):
        for x in self.location:
            water_object = x
        
        x = random.randint(water_object.rect.left+6, water_object.rect.right-10)
        y = random.randint(water_object.rect.top+8, water_object.rect.bottom)
        return x,y

class Lion(Animal):
    all = []
    def __init__(self, screen, island):
        super().__init__(screen)
        self.animal_type = "land"
        self.animal_name = "lion"
        self.speed = 3
        self.health = 20
        self.laziness = 100  

        self.x, self.y = self.on_island(island)
        self.image = pygame.image.load(f"animals/{self.animal_name}/F.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = (self.x,self.y))
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, 5)
        self.width = self.rect.width
        self.height = self.rect.height

        Animal.all.append(self)
        Lion.all.append(self)

class Baboon(Animal): 
    all = []
    def __init__(self, x, y, speed, laziness, health, width, height):
        super().__init__(x, y, speed, laziness, health, width, height)
        self.animal_type = "land"
        self.animal_name = "baboon"

        Animal.all.append(self)
        Baboon.all.append(self)

class Hippo(Animal):
    def __init__(self, x, y, speed, laziness, health, width, height):
        super().__init__(x, y, speed, laziness, health, width, height)
        self.animal_type = "landwater"
        self.animal_name = "hippo"
        Animal.all.append(self)
        Hippo.all.append(self)
    
class Fish(Animal):
    all = []
    def __init__(self, screen, water_object1, water_object2, water_object3, water_object4):
        super().__init__(screen)
        self.animal_type = "water"
        self.animal_name = "fish"
        self.speed = 4
        self.health = 2
        self.laziness = 100

        self.location = random.choice([water_object1, water_object2, water_object3, water_object4])
        self.x, self.y = self.off_island()

        self.image = pygame.image.load(f"animals/{self.animal_name}/F.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = (self.x,self.y))
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, 5)
        self.width = self.rect.width
        self.height = self.rect.height

        Animal.all.append(self)
        Fish.all.append(self)

