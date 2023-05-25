import array
from tqdm import tqdm
from utils.vec3 import *
from utils.color import *
from utils.ray import *


def hit_sphere(center, radius, r):
    oc = r.ori() - center
    a = r.dir().dot(r.dir())
    b = oc.dot(r.dir()) * 2.0
    c = oc.dot(oc) - radius * radius
    discriminant = b*b - a*c*4
    return discriminant > 0


def ray_color(r):
    if hit_sphere(point3(0,0,-1), 0.5, r):
        return color(1, 0, 0)
    
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

    # Camera
    viewport_height = 2.0
    viewport_width = aspect_ratio * viewport_height
    focal_length = 1.0

    origin = point3(0, 0, 0)
    horizontal = vec3(viewport_width, 0, 0)
    vertical = vec3(0, viewport_height, 0)
    lower_left_corner = origin - horizontal/2 - vertical/2 - vec3(0, 0, focal_length)
    
    # test image
    idx = 0
    for i in tqdm(range(height-1, -1, -1)):
        for j in range(width):

            u = float(j) / (width - 1)
            v = float(i) / (height - 1)
            r = ray(origin, lower_left_corner + horizontal*u + vertical*v - origin)

            c = ray_color(r)
            write_color(c, img, idx)
            idx += 3

    # save image
    with open('output/blue_example.ppm', 'wb') as f:
        f.write(bytearray(ppm_header, 'ascii'))
        img.tofile(f)

    print('Done!')


if __name__=="__main__":
    main()
