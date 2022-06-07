#최근 로또 당첨 번호 출력
import requests #requests라이브러리 가져오기
from bs4 import BeautifulSoup #BeautifulSoup라이브러리 가져오기

lotto_url='https://dhlottery.co.kr/gameResult.do?method=byWin'
raw=requests.get(lotto_url) #HTML코드 불러오기
soup=BeautifulSoup(raw.text,'html.parser') #html코드로 변환

box=soup.find('div',{'class':'nums'})# div class='nums'에 있는 정보 가져오기
numbers=box.find_all('span')#span에 있는 정보 불러오기

print('<최근 로또 당첨 번호>')
for number in numbers:
    print(number.text)#한줄 씩 text형태로 출력