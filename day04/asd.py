from urllib import response
import urllib.request ;
import datetime
import json


client_id = 'OQzLcKeLQwyaZ85INd7T'
client_secret = 'EtOC76hzvJ'

def getRequestUrl(url):
    req =urllib.request.Request(url)
    req.add_header("x-naver-Client-id", client_id)
    req.add_header("x-naver-Client-secret",client_secret)

    try:
             
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] url Request Success" % datetime.datetime.now())
        return response.read().decode('utf-8')
    except:    

       return None

def  getNaverSearch(node, srcText,start,display):
    base = "https://openapi.naver.com/v1/search"
    node = "/news.json"
    paramaters ="?query=%s&start=%s&display=%s" %(urllib.parse.quote(srcText),start,display)
    url = base+node+paramaters
    print(url)
    responseDecode =   getRequestUrl(url)

    if(responseDecode ==None):
        return None
    else: # 성공했다면 json 문자열을 python 객체로 리턴 : load()
        return json.loads(responseDecode)
     

node ="news"
srcText='선거'


jsonResponse =getNaverSearch(node,srcText,1,100)
print(jsonResponse)

getNaverSearch(node, srcText, 1, 100)  # 1에서 100까지 찾아달라 