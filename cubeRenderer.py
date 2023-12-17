from customMath import Vector3

class polygon:
    def __init__(self, points, colour):
        self.shape = points
        self.colour = colour

class cube:
    def __init__(self, position, scale):
        self.position = position
        self.scale = scale

def cubeToPolys(cube, topScale):
    x = cube.position.x
    y = cube.position.y
    z = cube.position.z
    origin = (-z + x, y - z*topScale - x*topScale)
    middleBottom = (origin[0], origin[0] - cube.scale.y)

theCube = cube(Vector3(0, 0, 0), Vector3(1, 1, 1))
cubeToPolys(theCube, 0.5)