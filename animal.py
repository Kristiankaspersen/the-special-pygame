import pygame 
import random
from island import Island

class Animal(pygame.sprite.Sprite): 
    all = []
    def __init__(self, screen, island):
        super().__init__()
        self.screen = screen
        self.x = random.randint(island.x, island.width-10)
        self.y = random.randint(island.y, island.height-10)
        self.animal_type = "Animal"      

        Animal.all.append(self)
    
    def update(self, island, landscape_objects, animate_num):
        self.landscape_objects = landscape_objects
        self.animal_movement(island, animate_num)
        self.isdead()

    def spawn_collision(self, landscape_objects):
        for x in landscape_objects:
            for y in self.all:
                if x.rect.colliderect(y.rect):
                    y.kill()

    def collision(self, landscape_objects):
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, 5)
        for x in landscape_objects:
            if self.hitbox.colliderect(x.rect):
                return True

    def animate(self, images=[], animate_num=-1, move=False):
        if animate_num != -1 and images and move:
            self.image = pygame.image.load(f"animals/{self.animal_type}/{images[animate_num]}").convert_alpha()
    
    def isdead(self):
        if self.health <= 0:
            self.kill()

    def animal_movement(self, island, animate_num):
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        move_direction = random.randint(1,4)
        num_move = random.randint(1,self.laziness)
        if num_move < 3:
            if move_direction == 1:
                self.rect.x -= self.speed
                self.check_bounds(island)
                if self.collision(self.landscape_objects):
                    self.rect.x += self.speed
                images = ["L.png", "LR.png", "LL.png"]
                self.animate(images, animate_num, True)
            elif move_direction == 2:
                self.rect.y -= self.speed
                self.check_bounds(island)
                if self.collision(self.landscape_objects):
                    self.rect.y += self.speed
                images = ["B.png", "BR.png", "BL.png"]
                self.animate(images, animate_num, True)
            elif move_direction == 3:
                self.rect.x += self.speed
                self.check_bounds(island)
                if self.collision(self.landscape_objects):
                    self.rect.x -= self.speed
                images = ["R.png", "RR.png", "RL.png"]
                self.animate(images, animate_num, True)
            elif move_direction == 4:
                self.rect.y += self.speed
                self.check_bounds(island)
                if self.collision(self.landscape_objects):
                    self.rect.y -= self.speed
                images = ["F.png", "FR.png", "FL.png"]
                self.animate(images, animate_num, True)
        self.animate(animate_num)

    #Make sure the animals stay within their bounds. Fix when island is re-structured
    def check_bounds(self, island):
        if not self.animal_type == "fish":
            if self.rect.x < island.x:
                self.rect.x = island.x
            elif self.rect.y < island.y:
                self.rect.y = island.y
            elif self.rect.x + self.width > island.width:
                self.rect.x = island.width - self.width
            elif self.rect.y + self.height > island.height:
                self.rect.y = island.height - self.height
        #Fish colliding with island
        else:
            if self.rect.x < 0:
                self.rect.x = 0
            elif self.rect.x + self.width > self.screen.get_width():
                self.rect.x = self.screen.get_width() - self.width
            elif self.rect.y < 0:
                self.rect.y = 0
            elif self.rect.y + self.height > self.screen.get_height():
                self.rect.y = self.screen.get_height() + self.height

            #Left side
            elif self.rect.x + self.width > island.offset and self.rect.x + self.width < island.offset + 10 and self.rect.y > island.offset and self.rect.y + self.height < self.screen.get_height() - island.offset:
                self.rect.x = island.offset - self.width

            #Right side
            elif self.rect.x < island.width and self.rect.x > island.width - 10 and self.rect.y > island.offset and self.rect.y + self.height < self.screen.get_height() - island.offset:
                self.rect.x = island.width

            #Top side
            elif self.rect.y + self.height > island.offset and self.rect.y + self.height < island.offset + 10 and self.rect.x > island.offset and self.rect.x + self.width < self.screen.get_width() - island.offset:
                self.rect.y = island.offset + self.height

            #Bottom side
            elif self.rect.y < island.height and self.rect.y > island.height - 10 and self.rect.x > island.offset and self.rect.x + self.width < self.screen.get_width() - island.offset:
                self.rect.y = island.height

class Lion(Animal):
    def __init__(self, screen, island, landscape_objects):
        super().__init__(screen, island)
        self.animal_type = "lion"
        self.speed = 3
        self.health = 20
        self.laziness = 50  
        self.image = pygame.image.load(f"animals/{self.animal_type}/F.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = (self.x,self.y))
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, 5)
        self.width = self.rect.width
        self.height = self.rect.height

        Animal.all.append(self)
        Lion.all.append(self)

        self.spawn_collision(landscape_objects)



class Baboon(Animal): 
    all = []
    def __init__(self, x, y, speed, laziness, health, width, height):
        super().__init__(x, y, speed, laziness, health, width, height)
    
        self.animal_type = "baboon"

        Animal.all.append(self)
        Baboon.all.append(self)

class Hippo(Animal):
    def __init__(self, x, y, speed, laziness, health, width, height):
        super().__init__(x, y, speed, laziness, health, width, height)
        
        self.animal_type = "hippo"
        Animal.all.append(self)
        Hippo.all.append(self)
    
class Fish(Animal):
    def __init__(self, x, y, speed, laziness, health, width, height):
        super().__init__(x, y, speed, laziness, health, width, height)

        self.animal_type = "fish"
        Animal.all.append(self)
        Fish.all.append(self)
