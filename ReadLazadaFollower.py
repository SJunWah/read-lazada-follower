import urllib
import urllib.request
import re
from bs4 import BeautifulSoup
import time
import random
import json
import math
import requests

targetFollowerNumber=4990

myfile = open("tm_fz_gn_1_1_1.txt","a")
stop = random.uniform(0.5,2)

url = 'https://www.lazada.com.my/shop/renderApi/pcPageData?pageId=7890567&shopId=118&clientType=pc&lang=en&pageType=1'
wbdata = requests.get(url).text
data = json.loads(wbdata)
followerNumber = data['result']['components']['111284']['moduleData']['followUserNumber']

while followerNumber<targetFollowerNumber:
    print(followerNumber,'<', targetFollowerNumber)
    time.sleep(3)  
else:
    print(followerNumber)

    
myfile.close()
