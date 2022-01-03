import pygame 
import random



class Animal: 
    all = []
    def __init__(self,x,y,speed,health,width,height):
        self.x = x
        self.y = y
        self.speed = speed
        self.health = health
        self.width = width
        self.height = height

        Animal.all.append(self)
    
        
    def draw_animal(self, screen):
        color = (153,153,0)
        pygame.draw.rect(screen, color, pygame.Rect(self.x, self.y, self.width, self.height))
    
    def animal_movement(self, island): 
        num = random.randint(1,4)
        if num == 1 and self.x > island.x:
            self.x -= self.speed
        elif num == 2 and self.y > island.y:
            self.y -= self.speed
        elif num == 3 and self.x + self.width < island.x + island.width:
            self.x += self.speed
        elif num == 4 and self.y + self.height < island.y + island.height:
            self.y += self.speed



class Bamboo(Animal): 
    all = []
    def __init__(self, x, y, speed, health, width, height):
        super().__init__(x, y, speed, health, width, height)
    
        Animal.all.append(self)
        Bamboo.all.append(self)

class Hippo(Animal):
    def __init__(self, x, y, speed, health, width, height):
        super().__init__(x, y, speed, health, width, height)

        Animal.all.append(self)
        Hippo.all.append(self)
    
class Fish(Animal):
    def __init__(self, x, y, speed, health, width, height):
        super().__init__(x, y, speed, health, width, height)

        Animal.all.append(self)
        Fish.all.append(self)