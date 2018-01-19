from PIL import Image
import numpy as np
import time


# from numba import jit


def help_get_image(newMatrix, data, row_offset, col_offset, op):


    data = data[row_offset:row_offset + newMatrix.shape[0], col_offset:col_offset + newMatrix.shape[1]]
    newMatrix = data * op + newMatrix
    return newMatrix


def get_after_image(convert_data, n, m):
    a = time.clock()
    size = convert_data.shape
    # 扩充列
    ma = np.zeros((size[0], n))
    convert_data = np.hstack((ma, convert_data, ma))
    # 扩充行
    na = np.zeros((m, size[1] + n * 2))
    convert_data = np.vstack((na, convert_data, na))
    # 扩维度

    convert_data = convert_data.cumsum(axis=1)  # 加行
    '''
    这里采用转置竟然没有任何速度变化，看来这里转置只是简单变换了轴而已
    '''
    # print("专制", time.time() - a)
    convert_data = convert_data.cumsum(axis=0)  # 加列

    convert_data = np.matrix(convert_data)
    newMatrix = np.matrix(np.zeros((convert_data.shape[0] - 2 * m, convert_data.shape[1] - 2 * n)))

    newMatrix = help_get_image(newMatrix, convert_data, 2 * m, 2 * n, 1)
    newMatrix = help_get_image(newMatrix, convert_data, 0, 2 * n, -1)
    newMatrix = help_get_image(newMatrix, convert_data, 2 * m, 0, -1)
    newMatrix = help_get_image(newMatrix, convert_data, 0, 0, 1)

    newMatrix = newMatrix /(4 * m * n)
    return newMatrix


# 获取图像并加上边缘，防止越界
def addImage(m, n, file_dir="temp.jpg"):
    im = Image.open(file_dir)
    # print("raw size is ", im.size)
    r, g, b = im.split()
    # convert_im = im.convert("L")
    r = np.array(r)
    g = np.array(g)
    b = np.array(b)
    # a=time.clock()
    r = Image.fromarray(get_after_image(r, m, n)).convert("L")
    # print("tims is ",time.clock()-a)
    g = Image.fromarray(get_after_image(g, m, n)).convert("L")
    b = Image.fromarray(get_after_image(b, m, n)).convert("L")
    image = Image.merge("RGB", (r, g, b))
    # image.show()
    # image.save("woman_temp.jpg", "PNG")
    # print("after size is", image.size)


# addImage(1, 10, 'woman.jpg')
# addImage(1, 1, 'small.jpg')
# 测试性能
if __name__ == "__main__":
    # import cProfile

    # cProfile.run("addImage(50, 50, 'woman.jpg')")
    a=time.clock()
    addImage(10, 10, 'woman.jpg')
    print(time.clock()-a)