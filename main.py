import pygame
pygame.init()
clock = pygame.time.Clock()

width = 1000
height = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Testing!!")

def drawIsland(x, y):
    color = (0,135,102)
    pygame.draw.rect(screen, color, pygame.Rect(x,y,width - x*2 ,height - y*2))
    # pygame.draw.circle(screen, color, (width/2,height/2), 350, 500)
    # pygame.draw.ellipse(screen, color, (100,25, 800, 750))

def drawPlayer(x,y):
    color = (0,0,0)
    pygame.draw.rect(screen, color, pygame.Rect(x,y,10,10))

islandX = 60
islandY = 60
playerX = width/2
playerY = height/2
playerSpeed = 6
running = True
while running:
    clock.tick(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            playerX -= playerSpeed
        if keys[pygame.K_w]:
            playerY -= playerSpeed
        if keys[pygame.K_d] and playerX < (width - islandX):
            playerX += playerSpeed
        if keys[pygame.K_s]:
            playerY += playerSpeed
    
    screen.fill((70,188,239))
    drawIsland(islandX, islandY)
    drawPlayer(playerX,playerY)
    pygame.display.update()