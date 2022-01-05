import pygame

class Island:
    all = []
    def __init__(self, screen, x, y, width, height):
        self.offset = x
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen

        Island.all.append(self)
        
    #This generate the bottom layer of the island: Just a green rectangle
    def generate_island_base(self):
        self.plain_grass_surface = pygame.image.load(f"landscape/plain_grass.png").convert_alpha()
        self.plain_grass_surface = pygame.transform.scale(self.plain_grass_surface, (self.width,self.height))
        self.plain_grass_rect = self.plain_grass_surface.get_rect(topleft = (self.x,self.y))
        self.screen.blit(self.plain_grass_surface,self.plain_grass_rect)

    #This generates the water surrounding the island
    def generateWater(self):
        self.plain_water_surface1 = pygame.image.load(f"landscape/plain_water.png").convert_alpha()
        self.plain_water_surface1 = pygame.transform.scale(self.plain_water_surface1, (self.plain_grass_rect.left, self.screen.get_height()))
        self.plain_water_rect1 = self.plain_water_surface1.get_rect(topleft = (0,0))
        self.screen.blit(self.plain_water_surface1,self.plain_water_rect1)

        self.plain_water_surface2 = pygame.image.load(f"landscape/plain_water.png").convert_alpha()
        self.plain_water_surface2 = pygame.transform.scale(self.plain_water_surface2, (self.screen.get_width(), self.plain_grass_rect.top))
        self.plain_water_rect2 = self.plain_water_surface2.get_rect(topleft = (0,0))
        self.screen.blit(self.plain_water_surface2,self.plain_water_rect2)
        
        self.plain_water_surface3 = pygame.image.load(f"landscape/plain_water.png").convert_alpha()
        self.plain_water_surface3 = pygame.transform.scale(self.plain_water_surface3, (self.screen.get_width(),self.offset))
        self.plain_water_rect3 = self.plain_water_surface3.get_rect(topleft = (0, self.plain_grass_rect.bottom))
        self.screen.blit(self.plain_water_surface3,self.plain_water_rect3)

        self.plain_water_surface4 = pygame.image.load(f"landscape/plain_water.png").convert_alpha()
        self.plain_water_surface4 = pygame.transform.scale(self.plain_water_surface4, (self.offset,self.screen.get_height()))
        self.plain_water_rect4 = self.plain_water_surface4.get_rect(topleft = (self.plain_grass_rect.right,0))
        self.screen.blit(self.plain_water_surface4,self.plain_water_rect4)

    def generateTrees(self):
        pass

    def generateRocks(self, rocks):
        pass

    def draw_island(self, screen):
        self.generate_island_base()
        self.generateWater()
 
