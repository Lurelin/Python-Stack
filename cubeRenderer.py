from customMath import Vector3

class polygon:
    def __init__(self, shapes, colour):
        self.shapes = shapes
        self.colour = colour

class cube:
    def __init__(self, position, scale):
        self.position = Vector3(position)
        self.scale = Vector3(scale)

def cubeToPolys(cube):
    pass
