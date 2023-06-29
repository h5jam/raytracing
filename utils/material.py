from utils.ray import *
from utils.vec3 import *
from abc import *
from hitting.hittable import * 


class material(metaclass=ABCMeta):
    @abstractmethod
    def scatter(r_in: ray, rec: hit_record, attenuation: color, scattered: ray) -> bool:
        pass
