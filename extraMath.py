import math

#A vector3 is a collection of 3 floats. Used to represent positions in 3d space, rotations(euler angles), etc.
class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def Add(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    def Subtract(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
    def Multiply(self, intIN):
        return Vector3(self.x * intIN, self.y * intIN, self.z * intIN)
    def Divide(self, intIN):
        return Vector3(self.x / intIN, self.y  / intIN, self.z  / intIN)
    def Average(self, other):
        return self.Add(other).Divide(2)

#A line represented as a line function (y = mx + b)
class slopeLine:
    def __init__(self, m, b):
        self.m = m
        self.b = b

def canBeSlopeLine(point1, point2):
    if (point2.x - point1.x != 0):
        return True
    else:
        False

def pointsToSlopeLine(point1, point2):
    m = (point2.y - point1.y) / (point2.x - point1.x)
    b = m * point1.x - point1.y
    return slopeLine(m, b)

def solveSystem(line1, line2):
    if (line1.m - line2.m != 0):
        x = (line1.b - line2.b) / (line1.m - line2.m)
    else:
        x = (line1.b - line2.b)
    y = line1.m * x + line1.b
    return Vector3(x, y, 0)

#A plane is a Quadrilateral shape in 3d space. Stored as 4 Vector3s, each representing a vertice.
class Plane:
    def __init__(self, topLeft, topRight, bottomLeft, bottomRight):
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

def PointInPerspective(camera, point):
    line1 = pointsToSlopeLine((0, 0, 0), point)
    xline = camera.lensDistance
    yline = 
    return (, solveSystem(line1, line3).x)

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