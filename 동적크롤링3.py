#파파고 번역 결과로 csv파일 만들기
from selenium import webdriver
import time
import csv

driver = webdriver.Chrome('./chromedriver')
papago = 'http://papago.naver.com/'
driver.get(papago)
time.sleep(3)

f = open('./my_papago.csv', 'w', newline='')
wtr = csv.writer(f)
wtr.writerow(['영단어', '번역결과'])

while True:
    keyword = input('영단어입력: ')
    if keyword == '0':
        print('번역종료')
        break

    driver.find_element_by_css_selector('textarea#txtSource').send_keys(keyword)
    driver.find_element_by_css_selector('button#btnTranslate').click()
    time.sleep(1)

    output = driver.find_element_by_css_selector('div#txtTarget').text
    wtr.writerow([keyword, output])
    driver.find_element_by_css_selector('textarea#txtSource').clear()
driver.close()
f.close()
