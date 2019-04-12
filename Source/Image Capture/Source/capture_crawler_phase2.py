from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from time import sleep

print("========================================================================")
print("                                                                        ")
print("========================================================================")

sleep(4)

def open_web():

# Configure Chrome Driver Path
    global driver
    driver_path = r'C:\Users\성윤\Desktop\chromes\chromedriver.exe'

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1440x2192')
    options.add_argument('disable-gpu')

    driver = webdriver.Chrome(driver_path, chrome_options=options)
open_web()

site_link = []
count = []
total = []
httplink = []
strangelink = []
se_st = []

def request_link():
    r = requests.get("https://www.wooribank.com/")
    c = r.content
    global soup
    soup = BeautifulSoup(c, "html.parser")


request_link()



def html_search_link():
    link = soup.findAll("a") #html에서 a인것을 찾음
    for item in link:
        site_link.append(item.get("href")) #href를 찾음
    print(site_link)


html_search_link()

def httplink_save():
    global httplink
    global strangelink
    for link in site_link:
        if 'http' in link:
            httplink.append(link)
        else:
            strangelink.append(link)
    print(httplink)
    httplink[0] = 'https://www.wooribank.com/'

    print(httplink)
    print(strangelink)

httplink_save()

def httplink_save2():
    global httplink
    global strangelink
    for link in site_link:
        if 'http' in link:
            httplink.append(link)
        else:
            strangelink.append(link)

    print(httplink)
    print(strangelink)

def link_format():
    for cnt in range(len(httplink)):
        count.append(cnt)

    for to in zip(count,httplink):
        total.append(to)
    print(total)

link_format()



def link_save_img():
    global se_st
    for run in range(len(httplink)):
        driver.get(total[run][1])
        st = ""
        st += total[run][1][8:]
        se_st.append(total[run][1])
        st = st.replace("/", "!")
        st = st.replace("?", "@")
        print(st)
        #driver.save_screenshot("./bankimages/"+st+".png")
    del se_st[0]
    print(se_st)
    httplink.clear()
    site_link.clear()
    count.clear()
    total.clear()
    soup.clear()



link_save_img()

driver.close()
print("================================끝===================================")

print("========================================================================")
print("                                                                        ")
print("========================================================================")

sleep(4)

open_web()

def second_request():
    print(se_st)
    for i in range(len(se_st)):
        r = requests.get(se_st[i])
        print(se_st[i])
        c = r.content
        global soup
        soup = BeautifulSoup(c, "html.parser")
        html_search_link()
        httplink_save2()
        link_format()
        print(se_st)
        #se_st.clear()
        link_save_img()




second_request()

driver.close()
print("================================끝===================================")