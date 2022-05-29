# -*- coding: utf-8 -*-
"""
Created on Sun May 29 16:01:22 2022

@author: mfgim
"""
#필요한 라이브러리
#url을 가져와서 처리할 수 있는 변수처럼
from urllib.request import urlopen
#url을 처리하는 함수들
from bs4 import BeautifulSoup as bs
#원하는 url
wanted_url = "https://www.korea.kr/news/pressReleaseList.do"
#url 열기
html = urlopen(wanted_url)
#url을 가져오고 html 기준으로 쪼개서 다룰 수 있게
bs_obj = bs(html, "html.parser")
#원하는 내용에 접근하는 과정, find_all의 경우 리스트처럼 return함
bs_obj = bs_obj.find("div", class_ = "article-content").find("div", class_ = "list-type")

bs_obj = bs_obj.find_all("a")

#내용과 url을 나눠준다, url을 wanted랑 그냥 합치면 중복이 생겨서 적절한 전처리 필요
for i in bs_obj:
    content_url = "https://www.korea.kr" + i["href"]
    content = i.span.strong.string
    print(content, content_url)
    
  