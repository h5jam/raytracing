import array
import math
import random


class vec3:
    def __init__(self, e1=0, e2=0, e3=0) -> None:
        self.e = array.array('d', [e1, e2, e3])
        self.length = math.sqrt(self.length_squared())
    
    def x(self):
        return self.e[0]

    def y(self):
        return self.e[1]
    
    def z(self):
        return self.e[2]
    
    def __add__(self, v):
        return vec3(self.e[0] + v.e[0], 
                    self.e[1] + v.e[1], 
                    self.e[2] + v.e[2])

    def __neg__(self):
        return vec3(-self.e[0], -self.e[1], -self.e[2])
    
    def __truediv__(self, t):
        return vec3(self.e[0] * 1/t, 
                    self.e[1] * 1/t, 
                    self.e[2] * 1/t)
    
    def __mul__(self, v):
        if isinstance(v, (int,float)):
            return vec3(self.e[0] * v, 
                        self.e[1] * v, 
                        self.e[2] * v)
        return vec3(self.e[0] * v.e[0], 
                        self.e[1] * v.e[1], 
                        self.e[2] * v.e[2])

    def __sub__(self, v):
        if isinstance(v, (int,float)):
            return vec3(self.e[0] - v,
                        self.e[1] - v,
                        self.e[2] - v)
        return vec3(self.e[0] - v.e[0], 
                    self.e[1] - v.e[1], 
                    self.e[2] - v.e[2])

    def length_squared(self):
        return self.e[0]*self.e[0] + self.e[1]*self.e[1] + self.e[2]*self.e[2]

    def __len__(self):
        return math.sqrt(self.length_squared())
    
    def __str__(self) -> str:
        return f'{self.e[0]} {self.e[1]} {self.e[2]}'

    # vector utility
    def dot(self, u):
        return self.e[0] * u.e[0]\
        + self.e[1] * u.e[1]\
        + self.e[2] * u.e[2]
    
    def cross(self, u):
        return vec3(
        self.e[1] * u.e[2] - self.e[2] * u.e[1],
        self.e[2] * u.e[0] - self.e[0] * u.e[2],
        self.e[0] * u.e[1] - self.e[1] * u.e[0]
        )


def unit_vector(e):
    return e / e.length


def random_vector(min=None, max=None):
    if min is None or max is None:
        return vec3(random.random(), random.random(), random.random())
    else:
        return vec3(random.uniform(min, max), random.uniform(min, max), random.uniform(min, max))


def random_in_unit_sphere():
    while True:
        p = random_vector(min=-1, max=1)
        if p.length_squared() < 1:
            break
    return p


def random_unit_vector():
    return unit_vector(random_in_unit_sphere())


def random_in_hemisphere(normal):
    in_unit = random_in_unit_sphere()
    if in_unit.dot(normal) > 0.0:
        return in_unit
    else:
        return -in_unit


# type aliases
point3 = vec3
color = vec3


if __name__=="__main__":
    point3 = vec3()
    color = vec3()

    print(point3+color)