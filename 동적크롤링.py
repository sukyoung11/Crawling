#파파고에서 번역 결과 다섯 번 받아오기

from selenium import webdriver
import time

my_dict = {}

driver = webdriver.Chrome('./chromedriver')
papago = 'http://papago.naver.com/'
driver.get(papago)
time.sleep(3)

def get_papaga_result(question):
    driver.find_element_by_css_selector('textarea#txtSource').send_keys(question)
    driver.find_element_by_css_selector('button#btnTranslate').click()
    time.sleep(1)
    output=driver.find_element_by_css_selector('div#txtTarget').text
    my_dict[question]=output
    driver.find_element_by_css_selector('textarea#txtSource').clear()
    return()

for i in range(5):
    question=input()
    get_papaga_result(question)
print(my_dict)








