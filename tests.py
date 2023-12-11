import math

class Vector3:
    def __init__(this, xI, yI, zI):
        this.x = xI
        this.y = yI
        this.z = zI
#Point rotation function. View: "https://academo.org/demos/rotation-about-point/" for math
def rotatePointByPoint(point1, point2, angle):
    angleInRadians = (angle * math.pi) / 180
    pX = point1.x - point2.x
    pY = point1.y - point2.y
    x = (pX * math.cos(angleInRadians)) - (pY * math.sin(angleInRadians))
    y = (pX * math.sin(angleInRadians)) + (pY * math.cos(angleInRadians))
    return Vector3(x + point2.x, y + point2.y, 0)
print("Hello World!")

point1 = Vector3(-4.54, 3, 0)
point2 = Vector3(8, -3, 0)
angle = 45
pointPrime = rotatePointByPoint(point1, point2, angle)
print("X: " + str(pointPrime.x) + " Y: " + str(pointPrime.y))