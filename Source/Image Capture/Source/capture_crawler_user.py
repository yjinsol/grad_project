from selenium import webdriver
import os

driver_path = r'C:\Users\yjs12\Downloads\chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1440x2192')
options.add_argument('disable-gpu')

driver = webdriver.Chrome(driver_path, chrome_options=options)
#driver.get('http://192.168.182.128')
if os.stat(r"C:\Users\yjs12\PycharmProjects\grad_project/test/").st_size == 0:
    print("yes")
    driver.get('https://spot.wooribank.com/pot/Dream?withyou=PODEP0019&cc=c007095:c009166;c012263:c012399&PLM_PDCD=P010000234&PRD_CD=P010000234&ALL_GB=ALL&depKind=')
    driver.refresh()
    dir_path = r"C:\Users\yjs12\PycharmProjects\grad_project/test/"
    driver.save_screenshot(dir_path + "spot$wooribank$com!pot!Dream@withyou=PODEP0019&cc=c007095%c009166;c012263%c012399&PLM_PDCD=P010000234&PRD_CD=P010000234&ALL_GB=ALL&depKind=_1" + ".png")
