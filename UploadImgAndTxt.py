from selenium import webdriver # 从selenium导入webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time,pyautogui
driver = webdriver.Chrome('C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe')
#driver.maximize_window()
driver.minimize_window()
driver.get('https://mp.toutiao.com/login/') # 获取登录
driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/div/img[3]").click()
driver.find_element_by_xpath("//*[@id=\"account\"]").send_keys("17719360720")
driver.find_element_by_xpath("//*[@id=\"password\"]").send_keys("6545qwaS")
time.sleep(8)#此时输入验证码
driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/form/input").click()#此时登录
time.sleep(5)#等待进入登陆后的页面

driver.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/ul/li[2]/div").click()
driver.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/ul/li[2]/ul/li[2]/a").click()
