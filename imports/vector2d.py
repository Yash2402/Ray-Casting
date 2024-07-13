class Vector2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coordinates = (x, y)

    def add(self, vector):
        return Vector2D(self.x + vector.x, self.y + vector.y)

    def __add__(self, vector):
        return self.add(vector)

    def sub(self, vector):
        return Vector2D(self.x - vector.x, self.y - vector.y)

    def __sub__(self, vector):
        return self.sub(vector)

    def dot(self, vector):
        return self.x*vector.x + self.y*vector.y

    def mag(self):
        return (self.x**2 + self.y**2)**(1/2)

    def magSq(self):
        return (self.x**2 + self.y**2)

    def unit(self):
        if self.mag() != 0:
            return Vector2D(self.x/self.mag(), self.y/self.mag())
        else:
            return Vector2D(self.x/0.00001, self.y/0.00001)

    def unit_tangent(self):
        return Vector2D(-self.unit().y, self.unit().x)

    def mult(self, s):
        return Vector2D(s*self.x, s*self.y)

    def __mul__(self, scalar):
        return self.mult(scalar)

    def __truediv__(self, scalar):
        return self*(1/scalar)
