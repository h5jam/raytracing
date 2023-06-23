from utils.ray import *


class Camera():
    def __init__(self) -> None:
        self.aspect_ratio = 16.0 / 9.0
        viewport_height = 2.0
        viewport_width = self.aspect_ratio * viewport_height
        self.focal_length = 1.0

        self.origin = point3(0, 0, 0)
        self.horizontal = vec3(viewport_width, 0.0, 0.0)
        self.vertical = vec3(0.0, viewport_height, 0.0)
        self.lower_left_corner = self.origin - self.horizontal/2 - self.vertical/2 - vec3(0, 0, self.focal_length)
    
    def get_ray(self, u, v):
        return ray(self.origin, self.lower_left_corner + self.horizontal*u + self.vertical*v - self.origin)
