import os

path = input('输入目录:\n')

if (path[-1] != '\\'):
    path = path + "\\"


def changeType(path):
    number = 1
    type = input('输入类型:\n')
    for file in os.listdir(path):
        oldPath = path + file.title()
        newPath = path + str(number) + '.' + type
        os.rename(oldPath, newPath)
        number = number + 1
    print("更改完成")


def changeName(path):
    number = 1
    middle = input("更改后名称\n")

    type = input('类型\n')
    for file in os.listdir(path):
        oldPath = path + file.title()
        newPath = path + middle + str(number) + '.' + type
        os.rename(oldPath, newPath)
        number = number + 1


def main(method):
    if (method == 1):
        # print('更改类型')
        changeType(path)
    else:
        # print("更改名称")
        changeName(path)


method = int(input('1表示改类型,2表示改名称\n'))
print(method)
main(method)
