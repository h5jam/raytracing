from utils.ray import *
from utils.vec3 import *
from abc import *
from hitting.hittable import * 


class material(metaclass=ABCMeta):
    @abstractmethod
    def scatter(r_in: ray, rec: hit_record, attenuation: color, scattered: ray) -> bool:
        pass


class lambertian(material):
    def __init__(self, a: color) -> None:
        self.albedo = a

    def scatter(self, r_in, rec, attenuation, scattered):
        scatter_dir = rec.normal + random_unit_vector()
        if scatter_dir.near_zero():
            scatter_dir = rec.normal
        scattered.set_ray(rec.p, scatter_dir)
        attenuation.copy_from(self.albedo)

        return True


class metal(material):
    def __init__(self, a: color) -> None:
        self.albedo = a

    def scatter(self, r_in, rec, attenuation, scattered):
        reflected = reflect(unit_vector(r_in.dir()), rec.normal)
        scattered.set_ray(rec.p, reflected)
        attenuation.copy_from(self.albedo)

        return scattered.dir().dot(rec.normal) > 0
