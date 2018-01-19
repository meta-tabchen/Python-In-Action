from PIL import Image
from PIL import ImageDraw, ImageFont
import numpy as np
import random
import string
import math
import time

# 构造编码字典
letters = string.ascii_letters

encode_map = {"_": "240"}
decode_map = {"240": "_"}

for lowercase, index in zip(letters, range(len(letters))):
    encode_map[lowercase] = index
    decode_map[index] = lowercase

encode_message = "Hello_I_am_your_father"


# encode_message = encode_message.lower()


def encode_image(filename, len):
    im = Image.open(filename)

    r, g, b = im.split()
    # r = np.array(im.getdata()).reshape((im.size[1], im.size[0]))
    r = np.array(r)
    for i in range(len):
        if (encode_message[i] == ""):
            r[0][i] = 26
        r[0][i] = encode_map[encode_message[i]]
    r = Image.fromarray(r).convert("L")
    im = Image.merge("RGB", (r, g, b))
    im.save("temp_test.png", "PNG")
    return im


def decode_image(filename, len):
    im = Image.open(filename)
    # im.show()
    r, g, b = im.split()
    # r = np.array(im.getdata()).reshape((im.size[1], im.size[0]))
    r = np.array(r)
    print("**" * 10)
    decode_message = ""
    for i in range(len):
        index = r[0][i]
        if (index == 26):
            decode_message = decode_message + " "
        decode_message = decode_message + decode_map[index]
    print(decode_message)


# encode_image("temp.png", len(encode_message))
# decode_image("temp_test.png", len(encode_message))
# print(len(encode_message))

def image_encode(file_name, message="我爱你\n中国", seed=10):
    font_color_max = 20
    random_number = []
    pro_message = ""
    image_w = 0
    image_h = 0
    ttfont = "C:\Windows\Fonts\simhei.ttf"
    font_size = 40
    row_max = 10
    all_count = 0
    myFont = ImageFont.truetype(ttfont, font_size)
    row_count = 0
    for word, index in zip(message, range(len(message))):
        if word in string.ascii_letters:
            if (row_count + 1 > row_max):
                pro_message = pro_message + "\n" + word
                row_count = 0
            else:
                pro_message = pro_message + word
            row_count = row_count + 1
            all_count = all_count + 1
        else:
            if (row_count + 2 > row_max):
                pro_message = pro_message + "\n" + word
                row_count = 0
            else:
                pro_message = pro_message + word
            row_count = row_count + 2
            all_count = all_count + 2
    image_w = row_max * font_size // 2
    print(image_w)
    image_h = math.ceil((all_count / row_max) *1.12)* font_size

    # math.
    im = Image.new("L", (image_w, image_h), color="#000000")
    im = im.convert("L")
    draw = ImageDraw.Draw(im)
    # draw.text([0,0],"f")
    draw.text([0, 0], pro_message, fill=(font_color_max), font=myFont)
    # im.show()
    random.seed(seed)
    for i in range(im.size[0] * im.size[1]):
        number = random.randint(0, 255 - font_color_max)
        random_number.append(number)

    random_matrix = np.matrix(random_number).reshape((im.size[1], im.size[0]))
    array = np.matrix(im.getdata()).reshape((im.size[1], im.size[0])) + random_matrix
    im = Image.fromarray(array).convert("L")
    im.show()
    im.save(file_name, "PNG")


def image_decode(file_name, seed=10):
    font_color_max = 20
    random_number = []
    im = Image.open(file_name).convert("L")
    random.seed(seed)
    for i in range(im.size[0] * im.size[1]):
        number = random.randint(0, 255 - font_color_max)
        random_number.append(number)
    random_matrix = np.matrix(random_number).reshape((im.size[1], im.size[0]))
    array = np.matrix(im.getdata()).reshape((im.size[1], im.size[0])) - random_matrix
    array = array * (255 // font_color_max)
    im = Image.fromarray(array).convert("L")
    im.show()

# image_encode("image_magic.png", "我是陈佳豪")
image_decode("image_magic.png")
# random.seed(10)
# for i in range(10):
#     a = random.randint(1, 50)
