#코로나 검색 후 첫 페이지 뉴스 기사 제목 출력
import requests #requests라이브러리 가져오기
from bs4 import BeautifulSoup #BeautifulSoup라이브러리 가져오기

news_url='https://search.hankyung.com/apps.frm/search.news?query=코로나'
raw=requests.get(news_url) #HTML코드 불러오기
soup=BeautifulSoup(raw.text,'html.parser') #html코드로 변환

box=soup.find('ul',{'class':'article'})# ul class='article'에 있는 정보 가져오기
all_title=box.find_all('em',{'class':'tit'})

for title in all_title:
    print(title.text)