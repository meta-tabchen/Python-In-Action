from PIL import Image
import numpy as np
import time


def help_get_image(newMatrix, data, m, n):
    ops = [[2 * m, 2 * n, 1], [0, 2 * n, -1], [2 * m, 0, -1], [0, 0, 1]]
    for op in ops:
        temp = (data[op[0]:op[0] + newMatrix.shape[0], op[1]:op[1] + newMatrix.shape[1]])
        if (op[2] == 1):
            newMatrix = newMatrix + temp
        else:
            newMatrix = newMatrix - temp
    newMatrix = newMatrix / (4 * m * n)
    return newMatrix


def get_after_image(convert_data, n, m):
    size = convert_data.shape
    # 扩充列
    ma = np.zeros((size[0], n))
    convert_data = np.hstack((ma, convert_data, ma))
    # 扩充行
    na = np.zeros((m, size[1] + n * 2))
    convert_data = np.vstack((na, convert_data, na))
    # 扩维度
    # a = time.clock()

    convert_data = convert_data.cumsum(axis=0)  # 加行
    # print("行", time.clock() - a)
    '''
    这里采用转置竟然没有任何速度变化，看来这里转置只是简单变换了轴而已
    '''
    # convert_data = np.transpose(convert_data)
    # a=time.clock()
    convert_data = convert_data.cumsum(axis=1)  # 加列
    # print("列", time.clock() - a)
    # convert_data = np.transpose(convert_data)
    convert_data = np.matrix(convert_data)

    newMatrix = np.matrix(np.zeros((convert_data.shape[0] - 2 * m, convert_data.shape[1] - 2 * n)))
    newMatrix = help_get_image(newMatrix, convert_data, m, n)

    return newMatrix


# 获取图像并加上边缘，防止越界
def addImage(m, n, file_dir="temp.jpg"):
    im = Image.open(file_dir)
    r, g, b = im.split()
    r = np.array(r)
    g = np.array(g)
    b = np.array(b)
    r = Image.fromarray(get_after_image(r, m, n)).convert("L")
    g = Image.fromarray(get_after_image(g, m, n)).convert("L")
    b = Image.fromarray(get_after_image(b, m, n)).convert("L")
    image = Image.merge("RGB", (r, g, b))
    # image.show()
    # image.save("woman_temp.jpg", "PNG")


# 测试性能
if __name__ == "__main__":
    # import cProfile
    # cProfile.run("addImage(1, 1, 'woman.jpg')", sort=1)
    a = time.clock()
    addImage(3, 3, 'woman.jpg')
    print(time.clock() - a)
# x = np.arange(4).reshape((2,2))
# print(x)
# c=x.T
# print(c)
# print(x)