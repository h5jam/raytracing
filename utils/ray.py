from utils.vec3 import *


class ray:
    def __init__(self, origin, direction) -> None:
        self.o = origin
        self.d = direction

    def o(self):
        return self.o
    
    def d(self):
        return self.d
    
    def at(self, t):
        return self.o + t*self.d
    