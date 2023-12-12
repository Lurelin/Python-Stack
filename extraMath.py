import math

#A vector3 is a collection of 3 floats. Used to represent positions in 3d space, rotations(euler angles), etc.
class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

#A plane is a Quadrilateral shape in 3d space. Stored as 4 Vector3s, each representing a vertice.
class Plane:
    def __init__(self, topLeft, topRight, bottomLeft, bottomRight):
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

def PointInPerspective(viewpoint, lens, point):
    pass

#Point rotation function. View: "https://academo.org/demos/rotation-about-point/" for math
def rotatePointByPoint(point1, point2, angle):
    angleInRadians = (angle * math.pi) / 180
    pX = point1.x - point2.x
    pY = point1.y - point2.y
    x = (pX * math.cos(angleInRadians)) - (pY * math.sin(angleInRadians))
    y = (pX * math.sin(angleInRadians)) + (pY * math.cos(angleInRadians))
    return Vector3(x + point2.x, y + point2.y, 0)

#Point rotation function, except point2 = 0, 0, 0
def rotatePointByOrigin(point, angle):
    angleInRadians = (angle * math.pi) / 180
    pX = point.x
    pY = point.y
    x = (pX * math.cos(angleInRadians)) - (pY * math.sin(angleInRadians))
    y = (pX * math.sin(angleInRadians)) + (pY * math.cos(angleInRadians))
    return Vector3(x, y, 0)