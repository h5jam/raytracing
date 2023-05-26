from abc import *
from dataclasses import dataclass
from utils.ray import *


@dataclass
class hit_record:
    p: point3 = None
    normal: vec3 = None
    t: float = None


class hittable(metaclass=ABCMeta):
    @abstractmethod
    def hit(r: ray, t_min: float, t_max: float, rec: hit_record) -> bool:
        pass
