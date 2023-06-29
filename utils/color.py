from utils.misc import *
import math


def write_color(pixel_color, samples_per_pixel, img, idx):

    r = pixel_color.x()
    g = pixel_color.y()
    b = pixel_color.z()

    scale = 1.0 / samples_per_pixel

    r = math.sqrt(scale * r)
    g = math.sqrt(scale * g)
    b = math.sqrt(scale * b)

    img[idx] = int(256*clamp(r, 0.0, 0.999))
    img[idx+1] = int(256*clamp(g, 0.0, 0.999))
    img[idx+2] = int(256*clamp(b, 0.0, 0.999))
