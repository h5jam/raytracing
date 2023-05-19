def write_color(pixel_color, img, idx):

    r = int(255*pixel_color.x())
    g = int(255*pixel_color.y())
    b = int(255*pixel_color.z())

    img[idx] = r
    img[idx+1] = g
    img[idx+2] = b