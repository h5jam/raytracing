import copy
from hitting.hittable import *


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
            if object.hit(r, t_min, closest_so_far, temp_rec):
                hit_anything = True
                closest_so_far = temp_rec.t
                # check the address in memory
                # print('in: ', id(rec))
                rec.copy_from(temp_rec)
                # print('in: ', id(rec))

        return hit_anything
