import requests
import urllib
import iRSiteCreds


iracingUrlOne = 'https://members.iracing.com/membersite/login.jsp'
iracingUrlTwo ='https://members.iracing.com/membersite/Login'
iracingHomePage = 'http://members.iracing.com/membersite/member/Home.do'

HEADERS = { 'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.52 Safari/537.17'
        , 'Referer': 'https://members.iracing.com/membersite/login.jsp', 'Connection': 'keep-alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Cache-Control': 'max-age=0', 'Host': 'members.iracing.com','Accept-Encoding': 'gzip,deflate,sdch', 'Origin': 'members.iracing.com', 'Accept-Language': 'en-US,en;q=0.8'}



getIracingHtmlResp = requests.get(iracingUrlOne, headers=HEADERS, params=iRSiteCreds.passCreds())


getIracingHtmlResp= requests.post(url = 'https://members.iracing.com/membersite/Login', data=iRSiteCreds.passCreds(), headers=HEADERS)

htmlResp = getIracingHtmlResp.text

print(htmlResp)