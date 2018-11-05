import re
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from pypinyin import lazy_pinyin as pinyin
options = Options()
options.add_argument('--headless')
project = 'bajian'
infile = project + '_todo.txt'
query = project+'_raw.txt'

# read file
names = [temp.strip() for temp in open(infile, 'r', encoding='utf-8').readlines()]
try:
    already = int(open(query, 'r', encoding='utf-8').readlines()[-1].split('\t')[0])
except:
    already = 0

browser = webdriver.Chrome(options=options)
WebDriverWait(browser,5,1)
for loc in range(already,len(names)):
    elements = names[loc].strip().split('\t')
    q = elements[-2].replace(' ','%20')
    institute = elements[-1]
    if 'a'<=institute[0]<='z': q += '%20'+institute.replace(' ','%20')
    # search for a name
    while True:
        try:
            browser.get('https://preview.academic.microsoft.com/search?q='+q)
            WebDriverWait(browser,10,1).until(ec.presence_of_all_elements_located((By.CLASS_NAME,'name-section')))
            links = [temp.find_element_by_tag_name('a').get_attribute('href') for temp in browser.find_elements_by_class_name('name-section')]
            cites = [int(re.sub('\D','',temp.find_elements_by_tag_name('a')[-1].text)) for temp in browser.find_elements_by_class_name('flex-segment')]
            targets = [links[temp] for temp in range(len(cites)) if cites[temp]>=100]
            break
        except:
            sleep(2)
    
    # scholars with 100+
    for target in targets:
        print(target)
        fail=0
        while fail<10:
            fail+=1
            try:
                browser.get(target)
                WebDriverWait(browser,10,1).until(ec.presence_of_all_elements_located((By.CLASS_NAME,'data')))
                old = browser.current_url
                authorid = target.split('/')[-2]
                authorname = browser.find_element_by_class_name('name-section').find_element_by_class_name('name').text
                try:
                    institute=browser.find_element_by_class_name('affiliation').text
                except:
                    institute='UNKNOWN INSTITUTE'
                break
            except:
                sleep(2)
        if fail==10: continue
        
        # write result
        open(query, 'a', encoding='utf-8').write(str(loc+1)+'\t'+names[loc]+'\t'+authorname+'\t'+institute+'\t'+authorid+'\n')
browser.quit()
