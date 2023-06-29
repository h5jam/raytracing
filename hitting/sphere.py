import math

from hitting.hittable import *
from utils.vec3 import *


class sphere(hittable):
    def __init__(self, center, radius, m) -> None:
        self.center = center
        self.radius = radius
        self.mat = m
    
    def hit(self, r, t_min, t_max, rec):
        oc = r.ori() - self.center
        a = r.dir().length_squared()
        half_b = oc.dot(r.dir())
        c = oc.length_squared() - self.radius**2
        discriminant = half_b**2 - a*c

        if discriminant < 0:
            return False

        sqrtd = math.sqrt(discriminant)

        # search the nearest root lying in the acceptable range
        root = (-half_b - sqrtd) / a
        if root < t_min or t_max < root:
            root = (-half_b + sqrtd) / a
            if root < t_min or t_max < root:
                return False
        # record hitting
        rec.t = root
        rec.p = r.at(rec.t)
        rec.mat = self.m
        outward_normal = (rec.p - self.center) / self.radius
        rec.set_face_normal(r, outward_normal)

        return True
