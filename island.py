import pygame

class Island:
    all = []
    def __init__(self, x, y, width, height):
        self.offset = x
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        Island.all.append(self)

    def generateWater():
        pass

    def generateTrees(self, tree):
        # amount_of_trees = tree * random_generate 
        pass

    def generateRocks(self, rocks):
        pass

    def draw_island(self, screen):
        color = (0,135,102)
        pygame.draw.rect(screen, color, pygame.Rect(self.x, self.y, self.width, self.height))
 
