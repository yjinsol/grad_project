from selenium import webdriver
import os
import time

browser = webdriver.Chrome(r'C:\Users\성윤\Desktop\chromes\chromedriver.exe')
#browser = webdriver.Edge(r'C:\Users\성윤\Desktop\chromes\MicrosoftWebDriver.exe')
browser.set_page_load_timeout(30)
r = open('C:\ddd\ddd.txt', mode='rt', encoding='utf-8')

for line in r:
    print('C:\kkk/'+str(line)+'.png')
    browser.get('http://'+line)
    file_url = str(line)
    #time.sleep(5)
    browser.save_screenshot('c:\kkk\ddd.png')
    time.sleep(5)
    #os.rename('c:/ttt/ddd.png' , 'c:/ttt/'+(file_url.replace('\n', ''))+'.png')

browser.quit()
r.close()