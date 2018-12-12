from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time,requests,re,sendMail
chrome_options = Options()
chrome_options.add_argument('--headless')
#driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome()
driver.get("http://fashion.163.com/")
time.sleep(2)

#向下刷新
i=0
while 1:
    driver.find_element_by_tag_name("body").send_keys(Keys.SPACE)
    i+=1
    if i==150:
        break

time.sleep(2)

#得到首页数据，分成图集和女人两个分类
def getData():
    oldData = {"女人":[],"图集":[]}
    dataList=driver.find_elements_by_class_name("data_row")
    print(dataList)
    for aData in dataList:
        aEles=aData.find_elements_by_tag_name("a")
        aHref=aEles[0].get_attribute("href")
        aTitle=aEles[0].text
        aFlag=aData.find_element_by_class_name("link").text
        print(aHref,aTitle,aFlag)
        #http://v.163.com/static/1/VK1G23RGQ.html 奚梦瑶聊了聊今年的维密大秀 女人
        if "v.163.com" in aHref: #这种链接是带视频的，筛选掉
            continue
        if aFlag=="女人":
            oldData["女人"].append(aHref)
        elif aFlag=="图集":
            oldData["图集"].append(aHref)
    return oldData

#得到女人页面的数据
def getGirlData(url):
    driver.get(url)
    time.sleep(5)
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
            try:
                aImg=tag.find_element_by_tag_name("img")
            except:
                continue
            imgSrc=aImg.get_attribute("src")
            content+='''<img src="'''+imgSrc+'''" alt="">'''
            print(imgSrc)
    content+='''</body></html>'''
    sendMail.sendMail(title,content)

#得到图集页面的数据

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

def updateDatas(girlDatas,imageDatas):

    for girl in girlDatas:
        print(girl)
        try:
            getGirlData(girl)
        except:
            continue
    for aImg in imageDatas:
        print(aImg)
        try:
            getImagesData(aImg)
        except:
            pass
while 1:
    oldData=getData()
    updateDatas(oldData["女人"],oldData["图集"])
    quit()
    driver.refresh()
    time.sleep(5)
    newData=getData()

    updateGirl=[]#需要更新的女人类型数据
    updateImages=[]#需要更新的图集数据
    if oldData["女人"][0]!=newData["女人"][0]:
        for girlDatas in newData["女人"]:
            if girlDatas!=oldData["女人"][0]:
                updateGirl.append(girlDatas)
    if oldData["图集"][0]!=newData["图集"][0]:
        for imgData in newData["图集"]:
            if imgData !=newData["图集"][0]:
                updateImages.append(imgData)



            
            




