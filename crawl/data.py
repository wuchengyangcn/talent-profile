from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
options = Options()
options.add_argument('--headless')
project = 'youqing'
raw = project+'_raw.txt'
data = project+'_data.txt'

while True:
    # read file
    ids = [temp.strip().split('\t')[-1] for temp in open(query, 'r', encoding='utf-8').readlines()]
    try:
        already = len(open(data, 'r', encoding='utf-8').readlines())
    except:
        already = 0
    if len(ids) == already:
        break

    browser = webdriver.Chrome(options=options)
    WebDriverWait(browser,5,1)
    for target in ids[already:]:
        print(target)

        fail = 0
        while fail<5:
            fail+=1
            try:
                browser.get('https://preview.academic.microsoft.com/author/'+target+'/publication')
                WebDriverWait(browser,15,1).until(ec.presence_of_all_elements_located((By.CLASS_NAME,'secondary-text')))
                texts = browser.find_element_by_class_name('secondary-text').text
                old = browser.current_url
                break
            except:
                sleep(2)
        if fail==5:open(data, 'a', encoding='utf-8').write(target+'\tnone\tnone\n')

        number = int(texts.split(' ')[-1])
        start = 2018
        # papers
        papers = []
        print(number)
        for page in range(0,number,100):
            print(page)
            fail = 0
            while fail < 5:
                fail+=1
                try:
                    browser.get(old+'&skip='+str(page)+'&take=100')
                    WebDriverWait(browser,15,1).until(ec.presence_of_all_elements_located((By.CLASS_NAME,'ma-card')))
                    cards = browser.find_elements_by_class_name('ma-card')
                    break
                except:
                    sleep(2)
            if fail==5: continue
            if len(cards)==0:break
            for paper in cards:
                papers.append(paper.find_element_by_class_name('title').get_attribute('href').split('/')[-2])
                try:
                    paperyear = int(paper.find_element_by_class_name('year').text)
                    start = min(start,paperyear)
                except:
                    pass
        
        while True:
            try:
                browser.get('https://preview.academic.microsoft.com/author/'+target+'/citedby')
                WebDriverWait(browser,15,1).until(ec.presence_of_all_elements_located((By.CLASS_NAME,'header-section')))
                old=browser.current_url
                break
            except:
                sleep(2)
        
        # cites
        numbers = []
        for year in range(start, 2019):
            print(year,end=':')
            fail = 0
            while fail<5:
                fail+=1
                try:
                    browser.get(old+'&eyl=Y%3C%3D'+str(year)+'&syl=Y%3E%3D'+str(year))
                    WebDriverWait(browser,15,1).until(ec.presence_of_all_elements_located((By.CLASS_NAME,'secondary-text')))
                    texts = browser.find_element_by_class_name('secondary-text').text
                    break
                except:
                    sleep(2)
            if fail==5: times='0'
            elif 'result' in texts:
                times = '0'
            else:
                times = texts.split(' ')[-1]
            print(times)
            numbers.append(times)
            
        # write result
        open(data, 'a', encoding='utf-8').write(target+'\t'+' '.join(numbers)+'\t'+' '.join(papers)+'\n')
    browser.quit()
