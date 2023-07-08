from utils.vec3 import *


class ray:
    def __init__(self, origin=None, direction=None) -> None:
        if origin is None:
            self.o = vec3()
            self.d = vec3()
        else:    
            self.o = origin
            self.d = direction

    def ori(self):
        return self.o
    
    def dir(self):
        return self.d
    
    def at(self, t):
        return self.o + self.d*t
    
    def set_ray(self, ori, dir):
        self.o = ori
        self.d = dir
