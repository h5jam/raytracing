from hittable import *


class hittable_list(hittable):
    def __init__(self) -> None:
        self.objects = set()

    def add(self, object):
        self.objects.add(object)
    
    def clear(self):
        self.objects = set()

    def hit(self, r, t_min, t_max, rec):
        temp_rec = hit_record()
        hit_anything = False
        closest_so_far = t_max

        for object in self.objects:
            if object.hit(r, t_min, t_max, temp_rec):
                hit_anything = True
                closest_so_far = temp_rec.t
                rec = temp_rec

        return hit_anything
