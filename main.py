import sys
import pygame
import cameraEngine
from extraMath import Vector3, Plane

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))

cam = cameraEngine.Camera(1, 1, 0)

def planeToList(plane):
    print(plane)
    return plane
while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  
            sys.exit(0)
    list = cam.returnShapeList()
    for i in list:
        pygame.draw.polygon(screen, (255, 255, 255), planeToList(i))
    pygame.display.flip()
    fpsClock.tick(fps)