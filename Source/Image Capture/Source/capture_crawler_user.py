from selenium import webdriver
import os

driver_path = r'C:\Users\yjs12\Downloads\chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1440x2192')
options.add_argument('disable-gpu')

driver = webdriver.Chrome(driver_path, chrome_options=options)
driver.get('http://192.168.182.128')
driver.refresh()
dir_path = r"C:\Users\yjs12\PycharmProjects\grad_project/test/"
driver.save_screenshot(dir_path + "test" + ".png")
