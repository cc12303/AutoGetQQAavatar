import requests
import winreg
import os
def desktop_path():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    path = winreg.QueryValueEx(key, "Desktop")[0]
    return path
desktop= desktop_path()
os.chmod(desktop, 0o755)
userid=str(input("输入QQ号："))
url="https://qlogo4.store.qq.com/qzone/"+userid+"/"+userid+"/100.jpg"
avatar=requests.get(url)
with open(desktop+"\\头像.jpg", "wb") as f:
    f.write(avatar.content)
print("头像已保存到桌面!")
input("按回车键退出")
