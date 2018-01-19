from PIL import Image
import numpy as np
import os
import random
import time


def pull_screenshot():
    os.system('adb shell screencap -p /sdcard/screen.png')
    os.system('adb pull /sdcard/screen.png')
    # os.system('adb shell rm /sdcard/screen.png')
    # print("截图完成")


def go():
    # raw=Image.open('raw_1.jpg').convert()
    w_scale = 0.4
    h_scale = 0.4
    raw = Image.open('screen.png').convert()

    raw = raw.resize((int(1080 * w_scale), int(1920 * h_scale)))

    one = raw.crop((195 * w_scale, 95 * h_scale, (835 + 195) * w_scale, (830 + 95) * h_scale))
    two = raw.crop((195 * w_scale, 995 * h_scale, (835 + 195) * w_scale, (830 + 995) * h_scale))

    r1, g1, b1, b = one.split()
    r1 = np.matrix(np.array(r1), dtype=np.int16)
    g1 = np.matrix(np.array(g1), dtype=np.int16)
    b1 = np.matrix(np.array(b1), dtype=np.int16)

    r2, g2, b2, b = two.split()
    r2 = np.matrix(np.array(r2), dtype=np.int16)
    g2 = np.matrix(np.array(g2), dtype=np.int16)
    b2 = np.matrix(np.array(b2), dtype=np.int16)
    s_m = 0
    s_n = 0
    e_m = 100
    e_n = 1

    # cost = abs(r1 - r2 + g1 - g2 + b1 - b2) > 100
    cost = abs(r1 - r2) + abs(g1 - g2) + abs(b1 - b2) > 50
    # print(cost.shape)
    # print(cost[1, 1])
    # print(r1.shape)
    number = 255
    r2 = r2 * 0.5
    g2 = g2 * 0.5
    b2 = b2 * 0.5
    for i in range(20, r1.shape[0] - 20):
        for j in range(20, r1.shape[1] - 20):

            if (cost[i, j]):
                # r1[i, j] = number
                r2[i, j] = number
                # g1[i, j] = number
                g2[i, j] = number
                # b1[i, j] = number
                b2[i, j] = number
                # else:
                # k = 0.5
                # r2[i, j] = r2[i, j] * k
                # g2[i, j] = g2[i, j] * k
                # b2[i, j] = b2[i, j] * k
    # print('ok')
    # r1 = Image.fromarray(r1).convert("L")
    # g1 = Image.fromarray(g1).convert("L")
    # b1 = Image.fromarray(b1).convert("L")
    # one = Image.merge("RGB", (r1, g1, b1))
    r2 = Image.fromarray(r2).convert("L")
    g2 = Image.fromarray(g2).convert("L")
    b2 = Image.fromarray(b2).convert("L")
    two = Image.merge("RGB", (r2, g2, b2))
    # two = two.resize((two.size[0] * 3, two.size[1] * 3))
    two.show()


# two.show()
# one.save('temp1.jpg', "JPEG")
# two.save('temp2.jpg', "JPEG")
# a = time.clock()
# pull_screenshot()
# print(time.clock() - a)
# a = time.clock()
go()
# print(time.clock() - a)
