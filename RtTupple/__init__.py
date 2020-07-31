import numpy


class RtTupple:

    def __init__(self, x=0, y=0, z=0, w=1):
        """

        :param x:
        :param y:
        :param z:
        :param w: 1 = point, 0 = vector
        """
        self.x = x
        self.y = y
        self.z = z
        self.w = w

        # TODO: check if checking the w == 1 or 0 is necessary eventually.
        '''
        if w != 0 and w != 1:
            return
        '''

    def __add__(self, other):
        return RtTupple(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)

    def __sub__(self, other):
        return RtTupple(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)

    def __mul__(self, val):
        return RtTupple(self.x * val, self.y * val, self.z * val, self.w * val)

    def __truediv__(self, val):
        if val > 0:
            return RtTupple(float(self.x) / float(val),
                        float(self.y) / float(val),
                        float(self.z) / float(val),
                        float(self.w) / float(val))
        else:
            return 0

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z and self.w == other.w

    def __neg__(self):
        return RtTupple(-self.x, -self.y, -self.z, -self.w)

    def __repr__(self):
        return str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ", " + str(self.w)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z + self.w * other.w

    def cross(self, other):
        return RtTupple(self.y * other.z - self.z * other.y,
                        self.z * other.x - other.z * self.x,
                        self.x * other.y - self.y * other.x, 0)

    def is_point(self):
        if self.w == 1:
            return True
        else:
            return False

    def is_vector(self):
        if self.w == 0:
            return True
        else:
            return False

    def magnitude(self):
        return numpy.sqrt(self.x * self.x + self.y * self.y + self.z * self.z + self.w * self.w)

    def normalize(self):
        m = self.magnitude()
        return self.__truediv__(m)


class RtPoint(RtTupple):

    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y, z, 1)


class RtVector(RtTupple):

    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y, z, 0)