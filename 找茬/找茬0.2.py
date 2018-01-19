from PIL import Image
import numpy as np


def zhaocha(one, two):
    one = Image.open(one).resize((500, 500))
    two = Image.open(two).resize((500, 500))

    one_r, one_g, one_b = one.split()
    two_r, two_g, two_b = two.split()

    one_r = np.matrix(one_r, np.int16)
    one_g = np.matrix(one_g, np.int16)
    one_b = np.matrix(one_b, np.int16)

    two_r = np.matrix(two_r, dtype=np.int16)
    two_g = np.matrix(two_g, dtype=np.int16)
    two_b = np.matrix(two_b, dtype=np.int16)

    p = abs(one_r - two_r) + abs(one_g - two_g) + abs(one_b - two_b) > 100

    number = 255
    scale = 0.5

    two_r = two_r * scale
    two_g = two_g * scale
    two_b = two_b * scale

    for i in range(0, (p.shape[0])):
        for j in range(0, (p.shape[1])):
            if p[i, j]:
                two_r[i, j] = number
                two_g[i, j] = number
                two_b[i, j] = number

    two_r = Image.fromarray(two_r).convert("L")
    two_g = Image.fromarray(two_g).convert("L")
    two_b = Image.fromarray(two_b).convert("L")

    result = Image.merge("RGB", (two_r, two_g, two_b)).show()


def get_images(file):
    all = Image.open(file)
    size = all.size
    one = all.crop((0, 0, size[0], size[1] // 2-3))
    two = all.crop((0, size[1] // 2+3, size[0], size[1]))
    one.save('one_temp.jpg', "JPEG")
    two.save('two_temp.jpg', 'JPEG')
    zhaocha('one_temp.jpg', 'two_temp.jpg')
    print(size)


get_images('test15.JPEG')
# zhaocha('one.jpg','two.jpg')
