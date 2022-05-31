#csv파일에 저장된 한국어->영어로 변환
from selenium import webdriver
import time
import csv

driver = webdriver.Chrome('./chromedriver')
papago = 'http://papago.naver.com/'
driver.get(papago)
time.sleep(3)

f = open('./my_papago.csv', 'r')
rdr = csv.reader(f)
next(rdr)
outputlist = []
for row in rdr:
    korean = row[1]
    outputlist.append(korean)

f.close()

for i in range(len(outputlist)):
    driver.find_element_by_css_selector('textarea#txtSource').send_keys(outputlist[i])
    driver.find_element_by_css_selector('button#btnTranslate').click()
    time.sleep(1)

    output = driver.find_element_by_css_selector('div#txtTarget').text
    driver.find_element_by_css_selector('textarea#txtSource').clear()
    print(f'{outputlist[i]} : {output}')
driver.close()
f.close()
