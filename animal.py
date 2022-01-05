import pygame 
import random

class Animal: 
    all = []
    def __init__(self, x, y, speed, laziness, health, width, height):
        self.x = x
        self.y = y
        self.speed = speed
        self.health = health
        self.width = width
        self.height = height
        self.laziness = laziness  
        self.animal_type = "Animal"      

        Animal.all.append(self)
    
   
    def draw_animal(self, screen, images=[], animate_num=-1, move=False):
        if animate_num != -1 and images and move:
            self.surface = pygame.image.load(f"animals/{self.animal_type}/{images[animate_num]}").convert_alpha()
        self.animal_rect = self.surface.get_rect(topleft = (self.x,self.y))
        screen.blit(self.surface,self.animal_rect)
    

    def animal_movement(self, island, screen, animate_num):
        self.width = self.surface.get_width()
        self.height = self.surface.get_height()
        screen = screen
        move_direction = random.randint(1,4)
        num_move = random.randint(1,self.laziness)
        if num_move < 3:
            if move_direction == 1:
                self.x -= self.speed
                self.check_bounds(island, screen)
                images = ["L.png", "LR.png", "LL.png"]
                self.draw_animal(screen, images, animate_num, True)
            elif move_direction == 2:
                self.y -= self.speed
                self.check_bounds(island, screen)
                images = ["B.png", "BR.png", "BL.png"]
                self.draw_animal(screen, images, animate_num, True)
            elif move_direction == 3:
                self.x += self.speed
                self.check_bounds(island, screen)
                images = ["R.png", "RR.png", "RL.png"]
                self.draw_animal(screen, images, animate_num, True)
            elif move_direction == 4:
                self.y += self.speed
                self.check_bounds(island, screen)
                images = ["F.png", "FR.png", "FL.png"]
                self.draw_animal(screen, images, animate_num, True)
        self.draw_animal(screen, animate_num)

    #Make sure the animals stay within their bounds
    def check_bounds(self, island, screen):
        if not self.animal_type == "fish":
            if self.x < island.x:
                self.x = island.x
            elif self.y < island.y:
                self.y = island.y
            elif self.x + self.width > island.width + island.offset:
                self.x = island.width + island.offset - self.width
            elif self.y + self.height > island.height + island.offset:
                self.y = island.height + island.offset - self.height
        #Fish colliding with island
        else:
            if self.x < 0:
                self.x = 0
            elif self.x + self.width > screen.get_width():
                self.x = screen.get_width() - self.width
            elif self.y < 0:
                self.y = 0
            elif self.y + self.height > screen.get_height():
                self.y = screen.get_height() + self.height

            #Left side
            elif self.x + self.width > island.offset and self.x + self.width < island.offset + 10 and self.y > island.offset and self.y + self.height < screen.get_height() - island.offset:
                self.x = island.offset - self.width

            #Right side
            elif self.x < island.width and self.x > island.width - 10 and self.y > island.offset and self.y + self.height < screen.get_height() - island.offset:
                self.x = island.width

            #Top side
            elif self.y + self.height > island.offset and self.y + self.height < island.offset + 10 and self.x > island.offset and self.x + self.width < screen.get_width() - island.offset:
                self.y = island.offset + self.height

            #Bottom side
            elif self.y < island.height and self.y > island.height - 10 and self.x > island.offset and self.x + self.width < screen.get_width() - island.offset:
                self.y = island.height

class Lion(Animal):
    def __init__(self, x, y, speed, laziness, health, width, height):
        super().__init__(x, y, speed, laziness, health, width, height)

        self.animal_type = "lion"
        self.surface = pygame.image.load(f"animals/{self.animal_type}/F.png").convert_alpha()

        Animal.all.append(self)
        Lion.all.append(self)


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

