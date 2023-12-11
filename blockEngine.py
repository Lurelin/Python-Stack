import math
class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

#Point rotation function. View: "https://academo.org/demos/rotation-about-point/" for math
def rotatePointByPoint(point1, point2, angle):
    angleInRadians = (angle * math.pi) / 180
    pX = point1.x - point2.x
    pY = point1.y - point2.y
    x = (pX * math.cos(angleInRadians)) - (pY * math.sin(angleInRadians))
    y = (pX * math.sin(angleInRadians)) + (pY * math.cos(angleInRadians))
    return Vector3(x + point2.x, y + point2.y, 0)

class Plane:
    def __init__(self, topLeft, topRight, bottomLeft, bottomRight):
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Camera:
    def __init__(self, x, y, z, lensSize, lensDistance):
        self.x = 0
        self.y = 0
        self.z = 0
        self.lensSize = abs(lensSize)
        self.lensDistance = abs(lensDistance)
        
        
class Block:
    def __init__(self):
        self.topLeft = Vector3(0, 0, 0)
        self.bottomRight = Vector3(0, 0, 0)