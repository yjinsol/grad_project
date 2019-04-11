from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from time import sleep

# Site : Daum

# keyword_input = str(input("검색할 KeyWord : "))
# key_str = ""
# l1 = []
#
# r = requests.get("http://search.daum.net/search?w=tot&DA=23A&rtmaxcoll=NNS&q="+keyword_input)
# c = r.content
# soup = BeautifulSoup(c, "html.parser")
#
# dn = soup.find("div", {"class":"wrap_gnb"})
# dn2 = dn.find("ul", {"class":"gnb_search"})
# dn3 = dn2.findAll("a")
#
# for item in dn3:
#     l1.append(item.get("href"))
#
# # 다음 사이트의 뉴스 목록을 keyword로 검색한 결과를 저장
# l1 = "search"+l1[1]
#
# # 최신 순위 정렬 URL를 가져오는 태그
# r = requests.get("http://search.daum.net/"+l1)
# c = r.content
# soup = BeautifulSoup(c, "html.parser")
# dsort_ = soup.find("div", {"class":"sort_comm"})
# dsort_1 = dsort_.findAll("a")
#
# for item in dsort_1:
#     key_str = item.get("href")

site_link = []
count = []
total = []

print("========================================================================")
print("                                                                        ")
print("========================================================================")

sleep(4)

# Configure Chrome Driver Path
driver_path = r'C:\Users\yjs12\Downloads\chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1440x2192')
options.add_argument('disable-gpu')

driver = webdriver.Chrome(driver_path, chrome_options=options)

r = requests.get("https://www.wooribank.com/")
c = r.content
soup = BeautifulSoup(c, "html.parser")

# link_1 = soup.find("div", {"class":"coll_cont"})
# link_2 = link_1.find("ul", {"id":"newsResultUL"})
# link_3 = link_2.findAll("div", {"class":"wrap_cont"}) #한 페이지에 뜨는 기사 10개
#print(soup)
#print("---------------------------------------------------------------------------")
#print(soup.findAll("a"))
link = soup.findAll("a")
for item in link:
    #print(item.get("href"))
    site_link.append(item.get("href"))

httplink=[]
strangelink=[]
for link in site_link:
    if 'http' in link:
        httplink.append(link)
    else:
        strangelink.append(link)
httplink[0] = 'https://www.wooribank.com/'
print(httplink)
print(strangelink)

for cnt in range(len(httplink)):
    count.append(cnt)

for to in zip(count,httplink):
    total.append(to)
print(total)

for run in range(len(httplink)):
    driver.get(total[run][1])
    st = ""
    st += total[run][1][8:]
    st = st.replace("/", "!")
    st = st.replace("?", "@")
    print(st)
    driver.save_screenshot("./bankimages/"+st+".png")

driver.close()
print("================================끝===================================")