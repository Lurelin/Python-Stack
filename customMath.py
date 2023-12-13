import math
class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, num):
        return Vector3(self.x * num, self.y * num, self.z * num)
    def __pow__(self, num):
        return Vector3(self.x ** num, self.y ** num, self.z ** num)
    def __truediv__(self, num):
        return Vector3(self.x / num, self.y / num, self.z / num)
    
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)
    def __ne__(self, other):
        return (self.x != other.x) or (self.y != other.y) or (self.z != other.z)
    
    def __str__(self):
        return f"(X: {str(self.x)} Y: {str(self.y)} Z: {str(self.z)})"
    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)
    def __abs__(self):
        return Vector3(abs(self.x), abs(self.y), abs(self.z))
    def __round__(self, n):
        return Vector3(round(self.x, n), round(self.y, n), abs(self.z, n))
    def __floor__(self):
        return Vector3(math.floor(self.x), math.floor(self.y), math.floor(self.z))
    def __ceil__(self):
        return Vector3(math.ceil(self.x), math.ceil(self.y), math.ceil(self.z))