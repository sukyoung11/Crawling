#한국경제 사이트에서 뉴스 기사 검색 후 2페이지까지 시각 - 기사 제목 출력

import requests #requests라이브러리 가져오기
from bs4 import BeautifulSoup #BeautifulSoup라이브러리 가져오기

count=0
keyword=input('뉴스 검색 키워드: ')
for page in range(1,3):
    news_url='https://search.hankyung.com/apps.frm/search.news?query='+keyword+'&mediaid_clust=HKPAPER,HKCOM&page='+str(page)
    raw=requests.get(news_url) #HTML코드 불러오기
    soup=BeautifulSoup(raw.text,'html.parser') #html코드로 변환

    box=soup.find('ul',{'class':'article'})# ul class='article'에 있는 정보 가져오기
    all_title=box.find_all('em',{'class':'tit'})
    all_datetime=box.find('span',{'class':'date_time'})

    for title in all_title:
        for datetime in all_datetime:
            count+=1
            t=title.text
            d=datetime
            print(f'{count}-[{d.strip()}]{t.strip()}')


