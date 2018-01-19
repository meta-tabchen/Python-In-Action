import os

# dir = "E:/破解/文本分析2"
number = 1
dir=input("dir\n")
f = input('前缀\n')
b = input('后缀\n')


def changeAll(dir):
    global number

    for path in os.listdir(dir):
        path = dir + "/" + path
        if (os.path.isdir(path)):
            changeAll(path)
        else:
            oldPath = path
            newPath = path.replace(path.split('/')[-1], '') + f + str(number) + '.' + b
            os.rename(oldPath, newPath)
            number = number + 1




changeAll(dir)
print(number)