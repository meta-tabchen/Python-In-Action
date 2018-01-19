from PIL import Image
import numpy as np
import time


def stackImage(file_name, number_row, number_col):
    # number_col, number_row = number_row, number_col
    im = Image.open(file_name)
    im = im.convert("L")
    # r, g, b = im.split()
    # convert_im = im.convert("L")
    # r = np.array(r)
    # g = np.array(g)
    # b = np.array(b)
    raw_image_size = [im.size[1], im.size[0]]

    raw_matrix = np.matrix(im.getdata()).reshape(raw_image_size)
    print(raw_matrix.shape)
    new_image = np.matrix(np.zeros((raw_matrix.shape[0] * number_row, raw_matrix.shape[1] * number_col)))
    # new_image_g=new_image_r
    # new_image_b=new_image_r
    for row_index in range(number_row):
        for col_index in range(number_col):
            new_image[row_index * raw_image_size[0]:(row_index + 1) * raw_image_size[0],
            col_index * raw_image_size[1]:(col_index + 1) * raw_image_size[1]] = raw_matrix

    new_image = Image.fromarray(new_image).convert("L")

    new_image.show()


# stackImage("small.jpg", 2, 3)
def stack_color_image(file_name, number_row, number_col,index):
    # number_col, number_row = number_row, number_col
    im = Image.open(file_name)
    raw_image_size = [im.size[1], im.size[0]]
    print(im.size)
    r, g, b = im.split()
    r = np.array(r)
    g = np.array(g)
    b = np.array(b)
    new_image_r = np.matrix(np.zeros((raw_image_size[0] * number_row, raw_image_size[1] * number_col)))
    new_image_g = np.matrix(np.zeros((raw_image_size[0] * number_row, raw_image_size[1] * number_col)))
    new_image_b = np.matrix(np.zeros((raw_image_size[0] * number_row, raw_image_size[1] * number_col)))
    for row_index in range(number_row):
        for col_index in range(number_col):
            new_image_r[row_index * raw_image_size[0]:(row_index + 1) * raw_image_size[0],
            col_index * raw_image_size[1]:(col_index + 1) * raw_image_size[1]] = r
            new_image_g[row_index * raw_image_size[0]:(row_index + 1) * raw_image_size[0],
            col_index * raw_image_size[1]:(col_index + 1) * raw_image_size[1]] = g
            new_image_b[row_index * raw_image_size[0]:(row_index + 1) * raw_image_size[0],
            col_index * raw_image_size[1]:(col_index + 1) * raw_image_size[1]] = b
    r = Image.fromarray(new_image_r).convert("L")
    g = Image.fromarray(new_image_g).convert("L")
    b = Image.fromarray(new_image_b).convert("L")

    new_image = Image.merge("RGB", (r, g, b))
    # new_image.show()
    new_image.save("huge_stack_{}.png".format(index), "PNG")

for i in  range(10,20):
    try:
        stack_color_image("woman.jpg", i, i,i*i)
        print("{} is over".format(i))
    except:
        print("max number is ",i)
        break
