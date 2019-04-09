from selenium.webdriver import Chrome
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.keys import Keys


# driver = Chrome(executable_path=r'C:\Users\yjs12\Desktop\논문\chromedriver.exe')
# print(driver.current_url)
# browser = webdriver.Chrome('/Users\yjs12\Desktop\논문\chromedriver.exe')
# browser.get('http://wikipedia.org')
# print(browser.current_url)

# from odoo.http import request
#
# print(request.httprequest.url_root)


# from urllib.parse import urlsplit
#
# from flask import request
#
#
# def extract_url_path_and_query(full_url=None, no_query=False):
#     """
#     Convert http://foo.bar.com/aaa/p.html?x=y to /aaa/p.html?x=y
#
#     :param no_query:
#     :type full_url: str
#     :param full_url: full url
#     :return: str
#     """
#     if full_url is None:
#         full_url = request.url
#     split = urlsplit(full_url)
#     result = split.path or "/"
#     if not no_query and split.query:
#         result += '?' + split.query
#     return result
#
#
# # ################# End Client Request Handler #################
#
#
# # ################# Begin Middle Functions #################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r'C:\Users\yjs12\Desktop\논문\chromedriver.exe')
url = driver.current_url
print(url)