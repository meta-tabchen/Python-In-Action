from PIL import Image
import numpy as np
import random
import time


def zhatu():
    import glob, os

    os.system('adb shell screencap -p /sdcard/screen.png')
    os.system('adb pull /sdcard/screen.png')
    for i in glob.glob('screen/*'):
        # os.remove(i)
        # os.remove('screen.png')
        # os.rename(i, '{}.png'.format(random.randint(1111, 9999)))

        os.system('adb shell screencap -p /sdcard/screen.png')
        os.system('adb pull /sdcard/screen.png')
        # os.system('adb shell rm /sdcard/screen.png')
        # print("截图完成")


def zhaocha():
    a = Image.open("screen.png").convert("RGB").resize((1080, 1920))
    b = a.crop((0, 0, 500, 500))
    d = a.size

    rate = 1080 / 540

    # e=a.crop((580,1420,1080,1920))
    up = a.crop((100 * rate, 50 * rate, d[0] - 30 * rate, 460 * rate))
    down = a.crop((100 * rate, 500 * rate, d[0] - 30 * rate, 910 * rate))
    # print(up.size)
    # print(down.size)
    up_r, up_g, up_b = up.split()
    down_r, down_g, down_b = down.split()

    up_r = np.matrix(up_r, np.int16)
    up_g = np.matrix(up_g, np.int16)
    up_b = np.matrix(up_b, np.int16)
    scale = 0.5

    down_r = np.matrix(down_r, dtype=np.int16)
    down_g = np.matrix(down_g, dtype=np.int16)
    down_b = np.matrix(down_b, dtype=np.int16)

    # print(UP_R)
    # print(down_r)
    # print(up_r-down_r)

    p = abs(up_r - down_r) + abs(up_g - down_g) + abs(up_b - down_b) > 30

    number = 255
    scale = 0.6

    down_r = down_r * scale
    down_g = down_g * scale
    down_b = down_b * scale

    for i in range(0, (p.shape[0])):
        for j in range(0, (p.shape[1])):
            if p[i, j]:
                down_r[i, j] = number
                down_g[i, j] = number
                down_b[i, j] = number

    down_r = Image.fromarray(down_r).convert("L")
    down_g = Image.fromarray(down_g).convert("L")
    down_b = Image.fromarray(down_b).convert("L")

    result = Image.merge("RGB", (down_r, down_g, down_b)).show()


a = time.clock()
zhatu()
print(time.clock() - a)
# zhaocha()
