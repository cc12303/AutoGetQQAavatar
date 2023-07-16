import requests
import winreg
import os
from tkinter import *
def desktop_path():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    path = winreg.QueryValueEx(key, "Desktop")[0]
    return path
desktop= desktop_path()
os.chmod(desktop, 0o755)
window=Tk()
scheight=window.winfo_screenheight()
scwidth=window.winfo_screenwidth()
x=int(scwidth/2-300)
y=int(scheight/2-100)
size='{}x{}+{}+{}'.format(600,200,x,y)
window.title('AutoGetQQAvatar V1.1')
window.geometry(size)
txt=Label(window,text='请输入QQ号',font=(12))
txt.pack()
kuang=Entry(window,width=20,font=(15))
kuang.pack()
def click():
    userid=kuang.get()
    url="https://qlogo4.store.qq.com/qzone/"+userid+"/"+userid+"/100.jpg"
    avatar=requests.get(url)
    with open(desktop+"\\"+userid+".jpg", "wb") as f:
        f.write(avatar.content)
    txt2=Label(window,text='头像已保存到桌面')
    txt2.pack()
bt=Button(window,text='确定',width=6,height=1,command=click)
bt.pack()
window.mainloop()
