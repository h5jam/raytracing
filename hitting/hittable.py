from abc import *
from dataclasses import dataclass
from utils.ray import *


@dataclass
class hit_record:
    p: point3
    normal: vec3
    t: float
    front_face: bool

    def set_face_normal(self, r, outward_normal):
        self.front_face = r.dir().dot(outward_normal) < 0
        self.normal = outward_normal if self.front_face else -outward_normal


class hittable(metaclass=ABCMeta):
    @abstractmethod
    def hit(r: ray, t_min: float, t_max: float, rec: hit_record) -> bool:
        pass
