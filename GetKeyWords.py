import requests
import json

headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
r = requests.get('https://index.baidu.com/Interface/homePage/pcConfig', headers=headers)
res=json.dumps(r.text)
ress=json.loads(res)
resss=eval(ress)
print(type(resss))
print(resss)
print(resss["data"])



