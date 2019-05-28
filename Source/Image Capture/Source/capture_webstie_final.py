import time

from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from time import sleep
import os
from pathlib import Path

print("========================================================================")
print("                                                                        ")
print("========================================================================")

sleep(4)

def open_web():

# Configure Chrome Driver Path
    global driver
    driver_path = r'C:\Users\yjs12\Downloads\chromedriver.exe'

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1440x2192')
    options.add_argument('disable-gpu')

    driver = webdriver.Chrome(driver_path, chrome_options=options)

site_link = []
count = []
total = []
httplink = []
strangelink = []
se_st = []

def request_link(): #국민은행 사이트를 요청받아서 html내용을 받아온다.
    r = requests.get("https://www.kbstar.com/")
    c = r.content
    global soup
    soup = BeautifulSoup(c, "html.parser")

def html_search_link(): #html내용을 분류한다.
    link = soup.findAll("a") #html에서 a인것을 찾음
    for item in link:
        site_link.append(item.get("href")) #href를 찾음
    print('site_link: ' + str(site_link))

def httplink_save(): #분류된 html내용에서 http로 시작하는 링크와 아닌 링크를 구분하여 저장한다.
    global httplink
    global strangelink
    for link in site_link:
        if 'http' in link:
            httplink.append(link)
        else:
            strangelink.append(link)

    print('httplink: ' + str(httplink))
    print('strangelink: ' + str(strangelink))

def link_format(): #URL개수 확인과 정렬을 위한 함수
    for cnt in range(len(httplink)):
        count.append(cnt)

    for to in zip(count,httplink):
        total.append(to)
    print(total)

def url_save(): #URL을 텍스트 파일에 저장하는 함수
    f = open("test.txt", 'a')
    f.write('\n'.join(save_list))
    f.write("\n")
    f.close()

def make_directory(st): #이미지 이름으로 폴더를 생성후 폴더에 이미지를 저장하는 함수
    dir_path = r"C:\Users\yjs12\PycharmProjects\grad_project\image capture\kb"
    st = st.replace(":", "%")
    st = st.replace(".", "$")
    file_name = st
    print(file_name)
    dest_directory = (dir_path + "/" + file_name + "/")
    my_file = Path(dest_directory)
    if not my_file.exists():
        os.mkdir(dir_path + "/" + file_name + "/")
    return dest_directory

def link_save_img(): #각각의 URL이미지를 URL이름으로 저장하기 위한 포멧팅과 이미지를 특정경로에 저장하는 함수
    global se_st
    print(len(httplink))
    for run in range(len(httplink)):
        driver.get(total[run][1])
        st = ""
        st += total[run][1][8:]
        se_st.append(total[run][1])
        st = st.replace("/", "!")
        st = st.replace("?", "@")
        #print(str(total[run][0]+1) + ' ' + st)

        dest_directory = make_directory(st)

        for i in range(20): #같은 url에 대해 새로고침한 10개의 이미지
            time.sleep(1)
            driver.save_screenshot(dest_directory + st + "_" + str(i+1)+ ".png")
            driver.refresh()

    del se_st[0]
    print(se_st)
    httplink.clear()
    site_link.clear()
    count.clear()
    total.clear()
    soup.clear()

open_web()
request_link()
html_search_link()
httplink_save()
#httplink[0] = 'https://www.wooribank.com/'
save_list = httplink
url_save()
link_format()
link_save_img()

driver.close()
print("================================끝===================================")

print("========================================================================")
print("                                                                        ")
print("========================================================================")

sleep(4)

open_web()

def second_request(): #다음 트랜잭션에 대한 URL과 이미지를 저장하기 위한 함수
    global save_list
    print(se_st)
    for i in range(len(se_st)):
        r = requests.get(se_st[i])
        print(se_st[i])
        c = r.content
        global soup
        soup = BeautifulSoup(c, "html.parser")
        html_search_link()
        httplink_save()
        save_list = httplink
        url_save()
        link_format()
        print(se_st)
        #se_st.clear()
        link_save_img()

second_request()

driver.close()
print("================================끝===================================")