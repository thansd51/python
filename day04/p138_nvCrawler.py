import datetime
from http import client
import os
from symbol import parameters
import sys
import urllib.request
import json
import time

client_id = 'OQzLcKeLQwyaZ85INd7T'
client_secret = 'EtOC76hzvJ'

def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header('x-naver-Client-id', client_id)
    req.add_header('x-naver-Client-secret', client_secret)
    
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print('[%s] Url Request Success' % datetime.datetime.now())
        return response.read().decode('utf-8')
    except:
        return None

def getNaverSearch(node, srcText, start, display):
    base = "https://openapi.naver.com/v1/search"
    node = "/news.json"
    parameters = "?query=%s&start=%s&display=%s"%(urllib.parse.quote(srcText), start, display)
    url = base + node + parameters
    print(url)
    responseDecode = getRequestUrl(url)

    if(responseDecode == None):
        return None
    else: #성공했다면 json 문자열을 python 객체로 리턴 : loads()
        return json.loads(responseDecode)

jsonResult =[]

def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']
    pDate = post['pubDate']

    jsonResult.append({'cnt': cnt, 'title': title, 'description': description, 'org_link': org_link, 'link' : link, 'pdate': pDate})

node = 'news'
srcText = input('검색어를 입력하세요(ex 선거)')
# srcText = '선거'
cnt = 0


jsonResponse = getNaverSearch(node, srcText, 1, 100)
print(jsonResponse)
total = jsonResponse['total']


while((jsonResponse != None) and (jsonResponse['display']!=0)):
    for post in jsonResponse['items']:
        cnt += 1
        getPostData(post, jsonResult, cnt)
    start = jsonResponse['start'] + jsonResponse['display']
    jsonResponse = getNaverSearch(node, srcText, start, 10)

print('전체 검색 : %d건' %total)

with open('%s_naver_%s.json' %(srcText, node), 'w', encoding='utf-8') as outfile:
    jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
    outfile.write(jsonFile)

print("가져온 데이터 : %d 건" %(cnt))
print('%s_naver_%s.json SAVED' %(srcText, node))
