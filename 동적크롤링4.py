#csv파일에 번역 결과 추가하기

from selenium import webdriver
import time
import csv

driver=webdriver.Chrome('./chromedriver')
papago='http://papago.naver.com/'
driver.get(papago)
time.sleep(3)

f=open('./my_papago.csv','r')

rdr=csv.reader(f)

next(rdr)

my_dict={}

for row in rdr:
    keyword=row[0]
    korean=row[1]
    my_dict[keyword]=korean

f.close()

f=open('./my_papago.csv','a',newline='')
wtr=csv.writer(f)

while True:
    keyword=input('번역할 영단어 입력 (0 입력하면 종료) ')
    if keyword == '0':
        print('번역종료')
        break
    if keyword in my_dict.keys():
        print(f'이미 번역한 영단어 입니다. 뜻은 {my_dict[keyword]}입니다. ')
    else:
        driver.find_element_by_css_selector('textarea#txtSource').send_keys(keyword)
        driver.find_element_by_css_selector('button#btnTranslate').click()
        time.sleep(1)

        output = driver.find_element_by_css_selector('div#txtTarget').text
        wtr.writerow([keyword, output])
        my_dict[keyword]=output
        driver.find_element_by_css_selector('textarea#txtSource').clear()
driver.close()
f.close()

