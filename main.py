import sys
import pygame
import blockEngine

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  
            sys.exit(0)
    pygame.display.flip()
    fpsClock.tick(fps)