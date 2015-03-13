from math import pi


class Sphere(object):
    r = None
    x = None
    y = None
    z = None

    def __init__(self, r=1, x=0, y=0, z=0):
        self.r = r
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        return 4.0 / 3.0 * pi * self.r ** 3

    def get_square(self):
        return 4.0 * pi * self.r ** 2

    def get_radius(self):
        return self.r

    def set_radius(self, r):
        self.r = r

    def get_center(self):
        return self.x, self.y, self.z

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        if self.r**2 >= (x - self.x)**2 + (y - self.y)**2 + (z - self.z)**2:
            return True
        else:
            return False

'''
        if self.r == 0:
            return False
        flag = False
        if (abs(self.x) + self.r >= abs(x) and
            abs(self.y) + self.r >= abs(y) and
            abs(self.z) + self.r >= abs(z)):
                flag = True
'''



s0 = Sphere(2)

print s0.r, s0.x, s0.y, s0.z
print s0.r, s0.x, s0.y, s0.z
print s0.get_volume()
print s0.get_square()
print s0.get_center()
s0.set_center(0, 0, 0)
print s0.get_center()
print s0.is_point_inside(2.1, 0, 0)

