import array
from tqdm import tqdm


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

            r = float(j) / (w-1)
            g = float(i) / (h-1)
            b = 0.25

            ir = int(255 * r)
            ig = int(255 * g)
            ib = int(255 * b)

            img[idx] = ir
            img[idx+1] = ig
            img[idx+2] = ib

            idx += 3

    # save image
    with open('output/blue_example.ppm', 'wb') as f:
        f.write(bytearray(ppm_header, 'ascii'))
        img.tofile(f)

    print('Done!')


if __name__=="__main__":
    main()
