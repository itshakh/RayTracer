import torch


class RtTupple:

    def __init__(self, x=0, y=0, z=0, w=0):
        self.x = x
        self.y = y
        self.z = z
        if w != 0 and w != 1:
            return

        self.w = w

    def __add__(self, other):
        return RtTupple(self.x + other.x, self.y + other.y, self.z + other.z, min(self.w + other.w, 1))

    def __sub__(self, other):

        return RtTupple(self.x - other.x, self.y - other.y, self.z - other.z, max(self.w - other.w, 0))

    def isPoint(self):
        if self.w == 1:
            return True
        else:
            return False

    def isVector(self):
        if self.w == 0:
            return True
        else:
            return False


class RtPoint(RtTupple):

    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y, z, 1)


class RtVector(RtTupple):

    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y, z, 0)