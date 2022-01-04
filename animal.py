import pygame 
import random



class Animal: 
    all = []
    def __init__(self,x,y,speed,laziness,health,width,height):
        self.x = x
        self.y = y
        self.speed = speed
        self.health = health
        self.width = width
        self.height = height
        self.laziness = laziness

        Animal.all.append(self)
    
        
    def draw_animal(self, screen):
        color = (153,153,0)
        pygame.draw.rect(screen, color, pygame.Rect(self.x, self.y, self.width, self.height))
    
    def animal_movement(self, island): 
        num1 = random.randint(1,4)
        num2 = random.randint(1,self.laziness)
        if num2 < 3:
            if num1 == 1 and self.x > island.x:
                self.x -= self.speed
            elif num1 == 2 and self.y > island.y:
                self.y -= self.speed
            elif num1 == 3 and self.x + self.width < island.x + island.width:
                self.x += self.speed
            elif num1 == 4 and self.y + self.height < island.y + island.height:
                self.y += self.speed



class Baboon(Animal): 
    all = []
    def __init__(self, x, y, speed, laziness, health, width, height):
        super().__init__(x, y, speed, laziness, health, width, height)
    
        Animal.all.append(self)
        Baboon.all.append(self)

class Hippo(Animal):
    def __init__(self, x, y, speed, laziness, health, width, height):
        super().__init__(x, y, speed, laziness, health, width, height)

        Animal.all.append(self)
        Hippo.all.append(self)
    
class Fish(Animal):
    def __init__(self, x, y, speed, laziness, health, width, height):
        super().__init__(x, y, speed, laziness, health, width, height)

        Animal.all.append(self)
        Fish.all.append(self)