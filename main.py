import array
import random
from tqdm import tqdm
from utils.vec3 import *
from utils.color import *
from utils.ray import *
from utils.camera import *
from hitting.hittable_list import *
from hitting.sphere import *
from utils.material import *


deg_to_rad = lambda d: d * math.pi / 180.0
INF = math.inf

def hit_sphere(center, radius, r):
    oc = r.ori() - center
    a = r.dir().length_squared()
    half_b = oc.dot(r.dir())
    c = oc.length_squared() - radius*radius
    discriminant = half_b*half_b - a*c
    if discriminant < 0:
        return -1.0
    else:
        return (-half_b - math.sqrt(discriminant)) / a


def ray_color(r, world, depth):
    rec = hit_record()

    if depth <= 0:
        return color(0, 0, 0)
    
    # hit
    if world.hit(r, 0.001, INF, rec):
        attenuation = color()
        scattered = ray()
        if rec.mat.scatter(r, rec, attenuation, scattered):
            return attenuation * ray_color(scattered, world, depth-1)

    # scene background
    unit_dir = unit_vector(r.dir())
    t = 0.5*(unit_dir.y() + 1.0)
    return color(1.0, 1.0, 1.0)*(1.0-t) + color(0.5, 0.7, 1.0)*t


def main():
    # INT8
    max_val = 255

    # Image
    aspect_ratio = 16.0 / 9.0
    width = 400
    height = int(width / aspect_ratio)
    ppm_header = f'P6 {width} {height} {max_val}\n'
    samples_per_pixel = 50
    max_depth = 50

    # unsigned int8 image
    img = array.array('B', [0,0,0]*width*height)

    print(f'elements: {len(img)}')
    print(f'size of one element: {img.itemsize}')

    # World
    world = hittable_list()

    material_ground = lambertian(color(0.8, 0.8, 0.0))
    material_center = lambertian(color(0.7, 0.3, 0.3))
    material_left = metal(color(0.8, 0.8, 0.8))
    material_right = metal(color(0.8, 0.6, 0.2))

    world.add(sphere(point3(0.0, -100.5, -1.0), 100.0, material_ground))
    world.add(sphere(point3(0.0, 0.0, -1.0), 0.5, material_center))
    world.add(sphere(point3(-1.0, 0.0, -1.0), 0.5, material_left))
    world.add(sphere(point3(1.0, 0.0, -1.0), 0.5, material_right))

    # Camera
    cam = Camera()

    # render
    idx = 0
    for i in tqdm(range(height-1, -1, -1)):
        for j in range(width):
            pixel_color = color(0, 0, 0)
            for _ in range(samples_per_pixel):
                u = float(j+random.random()) / (width - 1)
                v = float(i+random.random()) / (height - 1)
                r = cam.get_ray(u, v)
                pixel_color += ray_color(r, world, max_depth)

            write_color(pixel_color, samples_per_pixel, img, idx)
            idx += 3

    # save image
    with open('output/blue_example.ppm', 'wb') as f:
        f.write(bytearray(ppm_header, 'ascii'))
        img.tofile(f)

    print('Done!')


if __name__=="__main__":
    main()
