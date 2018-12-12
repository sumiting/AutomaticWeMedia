import win32clipboard as clip
import win32con
from PIL import Image
from io import StringIO

'''
    往剪贴板中放入图片
'''
def setImage(data):
    clip.OpenClipboard() #打开剪贴板
    clip.EmptyClipboard()  #先清空剪贴板
    clip.SetClipboardData(win32con.CF_DIB, data)  #将图片放入剪贴板
    clip.CloseClipboard()



if __name__ == '__main__':
    imagepath = 'C:\\Users\\Administrator\\Pictures\\Screenshots\\屏幕截图(1).png'
    img = Image.open(imagepath)
    output = StringIO()
    img.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()
    setImage(data)
