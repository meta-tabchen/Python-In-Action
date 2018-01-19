# 一个小列表占满父容器
from tkinter import *
import requests
import re
import downloadPdf
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
        self.home = Button(master, text="主页", command=self.homepage)
        self.start = Button(master, text="开始访问主页", command=self.gethomepage)
        self.downloadb = Button(master, text="全部下载", command=self.downloadall)
        self.listbox = Listbox(master)
        self.listbox.bind('<Double-Button-1>', self.get_select_item)

        self.homeurl = StringVar()
        self.home_url_entry = Entry(master, textvariable=self.homeurl)
        self.homeurl.set("https://chenfutu.ctfile.com/u/13762377")

        self.frame.pack()
        self.listbox.pack(fill=X)
        self.home_url_entry.pack(fill=X)
        self.home.pack(fill=X)
        self.start.pack(fill=X)
        self.downloadb.pack(fill=X)
        self.homepage()

    def downloadall(self):
        downloadPdf.start(self.nowurl)
        download.go()

    def setItems(self, items):
        self.listbox.delete(0, END)
        for item in items:
            if (item['type'] == 'folder'):
                self.listbox.insert(END, item['name'] + '>>')
            else:
                self.listbox.insert(END, item['name'])

    def gethomepage(self):
        url = self.homeurl.get()
        print('homeurl is ',url)
        self.nowurl = url
        self.homeurl=url
        self.host=url
        self.homedata = downloadPdf.get_home_file(url)[0]
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
            url = downloadPdf.get_detail_url(item['value'])
            downloadPdf.download(url, item['name'])
        else:
            url = self.host +'/'+ item['value']
            print(url)
            self.nowurl=url
            self.items = downloadPdf.get_home_file(url)[0]
            print(self.items)
            self.setItems(self.items)


root = Tk()
root.title('城通网盘下载器')
root.geometry('600x300')
app = myColud(root)
root.mainloop()
