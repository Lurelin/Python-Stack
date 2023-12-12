import math
from extraMath import *

class transform:
    def __init__(self, position, rotation):
        self.position = position
        self.rotation = rotation

class Camera:
    def __init__(self, transform, lensSize, lensDistance):
        self.transform = transform
        lensSize = abs(lensSize)
        lensDistance = abs(lensDistance)
        self.lens = Plane(Vector3(-lensSize, lensSize, lensDistance), Vector3(lensSize, lensSize, lensDistance), Vector3(-lensSize, -lensSize, lensDistance), Vector3(lensSize, -lensSize, lensDistance))
        self.shapeList = []
    
    def DrawCubeToShapeList():
        pass
    def DrawPlaneToShapeList():
        pass
    def DrawPointToShapeList():
        pass

    #returns the camera's shapelist, ordered from farthest to closest to camera(intended draw order, may have bugs but should suffice for game)
    def shapeList(self):
        return self.shapeList

class Block:
    def __init__(self):
        self.topLeft = Vector3(0, 0, 0)
        self.bottomRight = Vector3(0, 0, 0)