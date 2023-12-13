import math
from extraMath import *

class Camera:
    def __init__(self, lensSize, lensDistance, tilt):
        self.lensSize = abs(lensSize)
        self.lensDistance = abs(lensDistance)
        self.lensTilt = tilt
        self.shapeList = [Plane(Vector3(-1, 1, -10), Vector3(1, 1, -10), Vector3(-1, -1, -10), Vector3(1, -1, -10))]
    #returns the camera's shapelist, ordered from farthest to closest to camera(intended draw order, may have bugs but should suffice for game)
    def returnShapeList(self):
        modifiedShapes = []
        modifiedLens = self.lens
        for plane in self.shapeList:
            pointList = []
            pointList.append(PointInPerspective(self.position, modifiedLens, plane.topLeft))
            pointList.append(PointInPerspective(self.position, modifiedLens, plane.topRight))
            pointList.append(PointInPerspective(self.position, modifiedLens, plane.bottomLeft))
            pointList.append(PointInPerspective(self.position, modifiedLens, plane.bottomRight))
            modifiedShapes.append(pointList)
        return modifiedShapes

class Block:
    def __init__(self):
        self.topLeft = Vector3(0, 0, 0)
        self.bottomRight = Vector3(0, 0, 0)