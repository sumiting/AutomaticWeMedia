from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
import sendMail,requests,lxml,re
from bs4 import BeautifulSoup
headersHtml = {'content-type': 'text/html; charset=UTF-8',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
r=requests.get("http://www.myzaker.com/article/5c08a16a77ac6451b7660d12/",headers=headersHtml)
#print(r.text)
data=re.findall("(<div class=\"article_content\".*)<div class=\"article_other\"",r.text,re.S)[0]
print(data)
data=data.replace("data-original","src")
sendMail.sendMail("测试html",data)
quit()
driver = webdriver.Chrome()
def getGirlData(url):
    driver.get(url)
    time.sleep(3)
    title=driver.find_element_by_tag_name("h1").text
    Content=driver.find_element_by_class_name("post_text")
    print(title)
    pTags=Content.find_elements_by_tag_name("p")
    content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>'''
    for tag in pTags:
        if tag.text!="":
            content += "<p>" + tag.text + "</p>"
            print(tag.text)
        if tag.get_attribute("class")=="f_center":
            aImg=tag.find_element_by_tag_name("img")
            imgSrc=aImg.get_attribute("src")
            content+='''<img src="'''+imgSrc+'''" alt="">'''
            print(imgSrc)
    content+='''</body></html>'''
    sendMail.sendMail(title,content)
getGirlData('http://lady.163.com/18/1206/00/E2A631E600267VQQ.html')

def getImagesData(url):
    driver.get(url)
    time.sleep(3)
    pageNum=driver.find_element_by_class_name("denominator").text
    imgSrcList=[]
    labelList=[]
    #此循环得到所有图片链接地址
    for i in range(0,int(pageNum)-1):
        driver.find_element_by_tag_name("body").send_keys(Keys.RIGHT)
        try:
            aPhoto=driver.find_element_by_class_name("photo-a")
            bPhoto=driver.find_element_by_class_name("photo-b")
            imgA=aPhoto.find_element_by_tag_name("img")
            imgB=bPhoto.find_element_by_tag_name("img")
            aSrc=imgA.get_attribute("src")
            bSrc=imgB.get_attribute("src")
            imgSrcList.append(aSrc)
            imgSrcList.append(bSrc)
        except:
            pass
    imgSrcList = list(set(imgSrcList))
    title=driver.find_element_by_tag_name("h1").text
    contentInfo=driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/h2/div[2]/div/p").text
    tag=driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]")
    labels=tag.find_elements_by_tag_name("a")
    for label in labels:
        labelList.append(label.text)
    content = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
        </head>
        <body>'''
    print(title,content,labels,imgSrcList)
    for i,label in enumerate(labels):
        if i==0:
            content+="<p>"
        content+=" "+label.text
        if i==len(labels)-1:
            content+="</p></br>"
    content+="<p>"+contentInfo+"</p>"
    for imgSrc in imgSrcList:
        content += '''<img src="''' + imgSrc + '''" alt="">'''
    content += '''</body></html>'''
    sendMail.sendMail(title,content)
#getImagesData("http://lady.163.com/photoview/00A70026/114697.html")