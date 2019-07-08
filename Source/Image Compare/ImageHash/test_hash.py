import time

import imagehash
from PIL import Image
from selenium import webdriver

url = r"https://obank.kbstar.com/quics?page=C029656&QSL=F#loading"
#url = "https://kbstar.com/"
def open_web():

# Configure Chrome Driver Path
    global driver
    driver_path = r'C:\Users\yjs12\Downloads\chromedriver.exe'

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1440x2192')
    options.add_argument('disable-gpu')

    driver = webdriver.Chrome(driver_path, chrome_options=options)

open_web()
driver.get(url)
st = ""
if url[:5] != 'https':
    st += url[7:]
else:
    st += url[8:]

st = st.replace("/", "!")
st = st.replace("?", "@")

time.sleep(2)
driver.save_screenshot("momomomo_win.png")
# for i in range(10):
#     time.sleep(2)
#     driver.save_screenshot("./"+str(i)+"tetest" + ".png")
#     driver.refresh()
driver.close()

hash1 = imagehash.dhash(Image.open("momomomo_win.png"))
# for i in range(10):
#     hash2 = imagehash.dhash(Image.open("./obank.kbstar.com!quics@page=C029656&QSL=F_"+str(i+1)+".png"))
#     print(abs(hash1-hash2))
#print(hash1)
#print(hash2)

#print(abs(hash1-hash2))