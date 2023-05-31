import array
from tqdm import tqdm
from utils.vec3 import *
from utils.color import *
from utils.ray import *
from hitting.hittable_list import *
from hitting.sphere import *


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


def ray_color(r, world):
    rec = hit_record()

    # hit
    if world.hit(r, 0, INF, rec):
        return (rec.normal + color(1, 1, 1)) * 0.5

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

    # unsigned int8 image
    img = array.array('B', [0,0,0]*width*height)

    print(f'elements: {len(img)}')
    print(f'size of one element: {img.itemsize}')

    # World
    world = hittable_list()
    world.add(sphere(point3(0,0,-1), 0.5))
    world.add(sphere(point3(0,-100.5,-1), 100))

    # Camera
    viewport_height = 2.0
    viewport_width = aspect_ratio * viewport_height
    focal_length = 1.0

    origin = point3(0, 0, 0)
    horizontal = vec3(viewport_width, 0, 0)
    vertical = vec3(0, viewport_height, 0)
    lower_left_corner = origin - horizontal/2 - vertical/2 - vec3(0, 0, focal_length)
    
    # render
    idx = 0
    for i in tqdm(range(height-1, -1, -1)):
        for j in range(width):

            u = float(j) / (width - 1)
            v = float(i) / (height - 1)
            r = ray(origin, lower_left_corner + horizontal*u + vertical*v - origin)

            c = ray_color(r, world)
            write_color(c, img, idx)
            idx += 3

    # save image
    with open('output/blue_example.ppm', 'wb') as f:
        f.write(bytearray(ppm_header, 'ascii'))
        img.tofile(f)

    print('Done!')


if __name__=="__main__":
    main()
