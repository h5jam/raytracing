import array
import math


class vec3:
    def __init__(self, e1=0, e2=0, e3=0) -> None:
        self.e = array.array('d', [e1, e2, e3])
    
    def x(self):
        return self.e[0]

    def y(self):
        return self.e[1]
    
    def z(self):
        return self.e[2]
    
    def __add__(self, v):
        self.e[0] += v.e[0]
        self.e[1] += v.e[1]
        self.e[2] += v.e[2]
        return vec3(self.e[0], self.e[1], self.e[2])

    def __neg__(self):
        self.e[0] = -self.e[0]
        self.e[1] = -self.e[1]
        self.e[2] = -self.e[2]
        return vec3(self.e[0], self.e[1], self.e[2])
    
    def __truediv__(self, t):
        self.e[0] *= 1/t
        self.e[1] *= 1/t
        self.e[2] *= 1/t
        return vec3(self.e[0], self.e[1], self.e[2])
    
    def __mul__(self, v):
        self.e[0] *= v.e[0]
        self.e[1] *= v.e[1]
        self.e[2] *= v.e[2]
        return vec3(self.e[0], self.e[1], self.e[2])

    def _length_squared(self):
        return self.e[0]*self.e[0] + self.e[1]*self.e[1] + self.e[2]*self.e[2]

    def __len__(self):
        return math.sqrt(self._length_squared())
    
    def __str__(self) -> str:
        return f'{self.e[0]} {self.e[1]} {self.e[2]}'

    # vector utility
    def dot(self, u):
        return self.e[0] * u.e[0], \
        self.e[1] * u.e[1], \
        self.e[2] * u.e[2]
    
    def cross(self, u):
        self.e[0] = self.e[1] * u.e[2] - self.e[2] * u.e[1]
        self.e[1] = self.e[2] * u.e[0] - self.e[0] * u.e[2]
        self.e[2] = self.e[0] * u.e[1] - self.e[1] * u.e[0]
        return vec3(self.e[0], self.e[1], self.e[2])

    def unit_vector(self):
        return self.e / self.e.length()

# type aliases
point3 = vec3
color = vec3


if __name__=="__main__":
    point3 = vec3()
    color = vec3()

    print(point3+color)