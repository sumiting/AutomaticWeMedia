# coding=utf-8

from selenium import webdriver
import os,time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import win32clipboard as wc
import win32con
import win32api
print(range(0,7))
for i in range(0,7):
    print( i)
def setText(aString):  # 写入剪切板
    wc.OpenClipboard()
    wc.EmptyClipboard()
    wc.SetClipboardData(win32con.CF_TEXT, aString)
    wc.CloseClipboard()
    #并且ctrl+v复制下来 然后enter
    win32api.keybd_event(17, 0, 0, 0)  # ctrl的键位码是17
    win32api.keybd_event(86, 0, 0, 0)  # v的键位码是86
    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(13, 0, 0, 0)  # Enter的键位码是13
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
# 引入 chromedriver.exe
chromedriver = "C:\\Users\\Administrator\\AppData\Local\\Google\\Chrome\\Application\\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)
browser.maximize_window()
# 设置浏览器需要打开的 url
url = "https://mp.toutiao.com/login/"
browser.get(url)

# 在百度搜索框中输入关键字 " python "
#browser.find_element_by_class("i3").send_keys("python")
browser.find_element_by_class_name("i3").click()#点击登陆
#user:17719360720
#pass:6545qwaS
browser.find_element_by_id("account").send_keys("17719360720")
browser.find_element_by_id("password").send_keys("6545qwaS")
time.sleep(10)#这个时间输入验证码
browser.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/form/input").click()#登录按钮点击
time.sleep(5)
browser.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/ul/li[3]/div/span").click()#点击西瓜视频
browser.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/ul/li[3]/ul/li[2]/a").click()#点击发表视频
time.sleep(5)
browser.find_element_by_xpath("//*[@id='xigua']/div/div/div/div/div[1]/div[1]/div/div/input").send_keys('G:\\python\\Video\\TengXun\\张柏芝亲自凑仔返学　高度戒备.mp4')#上传视频
browser.find_element_by_xpath("//*[@id=\"xigua\"]/div/div/div/div/div[1]/div[2]/div[5]/div[2]/div/div").click()#点击上传封面
time.sleep(5)
browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/input").send_keys("G:\\python\\Video\\TengXun\\timg.jpg")
browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/button[1]").click()
labelList=["张柏芝","张柏芝男友","张柏芝别墅"]
inputLabel=browser.find_element_by_xpath("//*[@id=\"xigua\"]/div/div/div/div/div[1]/div[2]/div[8]/div[2]/div[1]")
ActionChains(browser).move_to_element(inputLabel).click(inputLabel).perform()#定位鼠标到指定元素

#browser.find_element_by_xpath("//*[@id=\"xigua\"]/div/div/div/div/div[1]/div[2]/div[8]/div[2]/div[1]").click()
for label in labelList:
    setText(label)


#browser.find_element_by_xpath("//*[@id=\"react-select-3--value\"]").send_keys("6666")
#browser.find_element_by_xpath("//*[@id=\"react-select-3--value\"]/div[2]/input").send_keys(Keys.ENTER)



quit()
for label in labelList:
    browser.find_element_by_class_name("Select-control").click()
    browser.find_element_by_class_name("Select-control").send_keys(label)
    browser.find_element_by_class_name("Select-control").send_keys(Keys.ENTER)

#写入粘贴板




# 关闭浏览器
#browser.quit()