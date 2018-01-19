# 一个小列表占满父容器
from tkinter import *
import requests
import re
import core_chengtong
import download


class myColud:
    def __init__(self, master):

        self.homedata = [{'name': '20170107.epub', 'value': '173744140', 'type': 'file'},
                         {'name': '20171104.epub', 'value': '226939355', 'type': 'file'},
                         {'name': '2017.11.11.epub', 'value': '227845411', 'type': 'file'}]
        # self.homedata = downloadPdf.get_home_file()[0]
        self.host = 'https://chenfutu.ctfile.com/u/13762377'
        self.nowurl = 'https://chenfutu.ctfile.com/u/13762377'
        self.items = self.homedata
        self.frame = Frame(master, bg='blue')
        self.home_btn = Button(master, text="主页", command=self.homepage)
        self.start_btn = Button(master, text="开始访问主页", command=self.gethomepage)
        self.all_links_btn = Button(master, text="获取当前所有链接", command=self.get_all_links)
        self.download_btn = Button(master, text="全部下载", command=self.downloadall)
        self.listbox = Listbox(master)
        self.listbox.bind('<Double-Button-1>', self.get_select_item)

        self.input = StringVar()
        self.url_entry = Entry(master, textvariable=self.input)
        self.input.set("https://chenfutu.ctfile.com/u/13762377")

        self.frame.pack()
        self.listbox.pack(fill=X)
        self.url_entry.pack(fill=X)
        self.home_btn.pack(fill=X)
        self.start_btn.pack(fill=X)
        self.all_links_btn.pack(fill=X)
        self.download_btn.pack(fill=X)
        self.homepage()

    def get_all_links(self):
        core_chengtong.start(self.nowurl)

    def downloadall(self):
        download.download_all()

    def setItems(self, items):
        self.listbox.delete(0, END)
        if (len(items) == 0):
            self.listbox.insert(END, "你仿佛来到了没有我的世界")
            return
        for item in items:
            if (item['type'] == 'folder'):
                self.listbox.insert(END, item['name'] + '>>')
            else:
                self.listbox.insert(END, item['name'])

    def gethomepage(self):
        url = self.input.get()
        # print('homeurl is ', url)
        self.nowurl = url
        self.host = url
        self.homedata = core_chengtong.get_home_file(url)[0]
        self.items = self.homedata
        self.setItems(self.homedata)

    def homepage(self):
        self.setItems(self.homedata)
        self.items = self.homedata

    def get_select_item(self, event):
        # host = 'https://chenfutu.ctfile.com/u/13762377/'
        select = self.listbox.get(self.listbox.curselection()).strip('>')
        item = {}
        for i in self.items:
            if (i['name'] == select):
                item = i
                break
        if (item['type'] == 'file'):
            url = core_chengtong.get_detail_url(item['value'])
            core_chengtong.download(url, item['name'])
        else:
            url = self.host + '/' + item['value']
            print(url)
            self.nowurl = url
            self.items = core_chengtong.get_home_file(url)[0]
            # print(self.items)
            self.setItems(self.items)


root = Tk()
root.title('城通网盘下载器')
root.geometry('600x330')
app = myColud(root)
root.mainloop()
