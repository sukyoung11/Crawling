#코뮤니티 카페 들어가서 원하는 게시판에서 원하는 정보 가져오기
from selenium import webdriver
import time

driver=webdriver.Chrome('./chromedriver')
login = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'
driver.get(login)
time.sleep(2)

my_id='su981210'
my_pw='*'

driver.execute_script("document.getElementsByName('id')[0].value = \'" + my_id + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value = \'" + my_pw + "\'")
time.sleep(1)

driver.find_element_by_id('log.login').click()
time.sleep(1)

comu= 'https://cafe.naver.com/codeuniv'
driver.get(comu)
time.sleep(1)

driver.find_element_by_id('menuLink90').click()

driver.switch_to.frame('cafe_main')
time.sleep(1)

driver.find_element_by_xpath('//*[@id="main-area"]/div[4]/table/tbody/tr[1]/td[1]/div[2]/div/a').click()
time.sleep(1)

for i in range(1,21):
    content=driver.find_element_by_css_selector('div.se-component-content').text
    driver.find_element_by_css_selector('a.BaseButton.btn_next').click()
    print(f'{i}.{content}')
    time.sleep(1)

driver.close





