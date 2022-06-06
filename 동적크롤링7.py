#3페이지까지 뉴스 전문 출력 (제목 클릭-내용 가져오기)
from selenium import webdriver
import time

keyword = input('뉴스 검색 키워드 : ')

driver=webdriver.Chrome('./chromedriver')
for i in range(1,4):
    news='https://search.hankyung.com/apps.frm/search.news?query=' + keyword + '&mediaid_clust=HKPAPER,HKCOM&page='+str(i)
    driver.get(news)
    time.sleep(2)

    ten_articles=driver.find_elements_by_css_selector('em.tit')
    count=0

    for article in ten_articles:
        title=article.text
        article.click()
        time.sleep(1)

        driver.switch_to.window(driver.window_handles[-1])

        content=driver.find_element_by_id('articletxt').text


        count+=1
        print(f'<{count}번 뉴스-{title}>')
        print(content)


        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
driver.close()