from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time,requests,re,sendMail
chrome_options = Options()
chrome_options.add_argument('--headless')
headersHtml = {'content-type': 'text/html; charset=UTF-8',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
#driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome()
driver.get("http://www.myzaker.com/channel/12")
time.sleep(2)

#向下刷新
i=0
while 1:
    driver.find_element_by_tag_name("body").send_keys(Keys.SPACE)
    time.sleep(0.1)
    i+=1
    print(i)
    if i==230:
        break
time.sleep(2)

#获得链接
h1s=driver.find_elements_by_class_name("figcaption")
aHrefs=[]
for aH1 in h1s:
    aTag=aH1.find_element_by_tag_name("a")
    aHref=aTag.get_attribute("href")
    aHrefs.append(aHref)

#发送一个页面的数据
def getOnePageData(title,url):
    r = requests.get(url, headers=headersHtml)
    # print(r.text)
    data = re.findall("(<div class=\"article_content\".*)<div class=\"article_other\"", r.text, re.S)[0]
    print(data)
    data = data.replace("data-original", "src")
    sendMail.sendMail(title, data)

def updateData(hrefList):
    for href in hrefList:
        try:
            driver.get(href)
            title=driver.find_element_by_tag_name("h1").text
            getOnePageData(title,href)
        except:
            continue
updateData(aHrefs)