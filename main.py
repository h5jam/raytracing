import array
from tqdm import tqdm
from utils.vec3 import vec3, point3, color
from utils.color import *

def main():
    # ppm header
    h = 256
    w = 256
    max_val = 255
    ppm_header = f'P6 {w} {h} {max_val}\n'

    # unsigned int8 image
    img = array.array('B', [0,0,0]*w*h)

    print(f'elements: {len(img)}')
    print(f'size of one element: {img.itemsize}')
    
    # test image
    idx = 0
    for i in tqdm(range(h-1, -1, -1)):
        for j in range(w):

            pixel_color = color(float(j) / (w-1), float(i) / (h-1), 0.25)
            write_color(pixel_color, img, idx)
            idx += 3

    # save image
    with open('output/blue_example.ppm', 'wb') as f:
        f.write(bytearray(ppm_header, 'ascii'))
        img.tofile(f)

    print('Done!')


if __name__=="__main__":
    main()
