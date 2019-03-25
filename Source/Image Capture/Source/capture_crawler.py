from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from time import sleep

# Site : Daum

keyword_input = str(input("�˻��� KeyWord : "))
key_str = ""
l1 = []

r = requests.get("http://search.daum.net/search?w=tot&DA=23A&rtmaxcoll=NNS&q="+keyword_input)
c = r.content
soup = BeautifulSoup(c, "html.parser")

dn = soup.find("div", {"class":"wrap_gnb"})
dn2 = dn.find("ul", {"class":"gnb_search"})
dn3 = dn2.findAll("a")

for item in dn3:
    l1.append(item.get("href"))

# ���� ����Ʈ�� ���� ����� keyword�� �˻��� ����� ����
l1 = "search"+l1[1]

# �ֽ� ���� ���� URL�� �������� �±�
r = requests.get("http://search.daum.net/"+l1)
c = r.content
soup = BeautifulSoup(c, "html.parser")
dsort_ = soup.find("div", {"class":"sort_comm"})
dsort_1 = dsort_.findAll("a")
for item in dsort_1:
    key_str = item.get("href")
site_link = []
count = []
total = []

print("========================================================================")
print("                                                                        ")
print("========================================================================")

sleep(4)

# Configure Chrome Driver Path
driver_path = ""

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1440x2192')
options.add_argument('disable-gpu')

driver = webdriver.Chrome(r'C:\Users\����\Desktop\chromes\chromedriver.exe', chrome_options=options)

r = requests.get("http://search.daum.net/search"+key_str)
c = r.content
soup = BeautifulSoup(c, "html.parser")

link_1 = soup.find("div", {"class":"coll_cont"})
link_2 = link_1.find("ul", {"id":"newsResultUL"})
link_3 = link_2.findAll("div", {"class":"wrap_count"})

for item in link_3:
    print(item.find("a").get("href"))
    site_link.append(item.find("a").get("href"))
for cnt in range(len(site_link)):
    count.append(cnt)

for to in zip(count,site_link):
    total.append(to)

for run in range(len(site_link)):
    driver.get(total[run][1])
    driver.save_screenshot("./www.daum.net"+keyword_input+"_���ñ�� "+str(total[run][0]+1)+"��"+".png")
driver.close()
print("================================��===================================")