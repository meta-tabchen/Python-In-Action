from bs4 import BeautifulSoup
import requests
import time
import os
import shutil


def convert_to_md(path='C:/Users/TabChen/Desktop/word.txt'):
    data = open(path, 'r', encoding='UTF-8').read()
    soup = BeautifulSoup(data, 'lxml')
    words = soup.select('body > table > tbody > tr > td:nth-of-type(2) ')
    explains = soup.select('body > table > tbody > tr > td:nth-of-type(3)')

    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    filename = time.strftime("%Y-%m-%d", time.localtime()) + '-word.md'
    title = "阅读词汇 " + time.strftime("%m/%d", time.localtime())

    f = open(filename, 'w', encoding='utf-8')

    pattern = '''---
title: 阅读词汇 01/11
categories: [English,Words,Reading]
date: 2018-01-11 09:50:18
tags: [English,Words,Reading]
---
这是阅读需要背的词汇
<!--more-->\n'''.format(title, date)

    f.write(pattern)

    for word, explain in zip(words, explains):
        f.write('# {}\n'.format(word.string))
        f.write(explain.string + '\n\n')
    f.flush()
    newpath = 'E:/blog/source/_posts/' + filename
    # os.rename(path,postpath+
    shutil.copyfile(filename, newpath)


convert_to_md()
