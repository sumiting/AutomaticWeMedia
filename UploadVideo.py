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

#进入上传视频界面
driver.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/ul/li[3]/div/span").click()
driver.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/ul/li[3]/ul/li[2]/a").click()
time.sleep(2)

#开始上传视频
driver.find_element_by_xpath("//*[@id=\"xigua\"]/div/div/div/div/div[1]/div[1]/div/div/input").send_keys("G:\\python\\Video\TengXun\\张柏芝亲自凑仔返学　高度戒备.mp4")
driver.find_element_by_xpath("//*[@id=\"xigua\"]/div/div/div/div/div[1]/div[2]/div[5]/div[2]/div/div").click()#上传封面
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/input").send_keys("G:\\python\\Video\\TengXun\\timg.jpg")
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/button[1]").click()
##上传封面结束

##开始打标签选择分类
ele=driver.find_element_by_xpath("//*[@id=\"react-select-7--value\"]/div[1]")
driver.execute_script("arguments[0].focus();",ele)













