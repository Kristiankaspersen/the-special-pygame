import pygame 

class Player: 
    all = []
    def __init__(self, name, speed, health, x, y, width, height):
        self.name = name
        self.x = x
        self.y = y
        self.speed = speed
        self.health = health
        self.width = width
        self.height = height

        Player.all.append(self)
    
    def drawPlayer(self, screen):
        color = (0,0,0)
        pygame.draw.rect(screen, color, pygame.Rect(self.x, self.y, self.width, self.height))

    def attack(self): 
        pass

    def move(self):
        pass







