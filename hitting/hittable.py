from abc import *
from dataclasses import dataclass
from utils.ray import *


# @dataclass
class hit_record:
    def __init__(self, p=None, normal=None, t=None, front_face=None, mat=None) -> None:
        self.p: point3 = p
        self.normal: vec3 = normal
        self.t: float = t
        self.front_face: bool = front_face
        self.mat = mat

    def set_face_normal(self, r, outward_normal):
        self.front_face = r.dir().dot(outward_normal) < 0
        self.normal = outward_normal if self.front_face else -outward_normal

    # temporary..
    def copy_from(self, other_rec):
        self.p = other_rec.p
        self.t = other_rec.t
        self.normal = other_rec.normal
        self.front_face = other_rec.front_face
        self.mat = other_rec.mat


class hittable(metaclass=ABCMeta):
    @abstractmethod
    def hit(r: ray, t_min: float, t_max: float, rec: hit_record) -> bool:
        pass
