import urllib.request
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re

#套件輸入
url = 'https://www.instagram.com/?hl=zh-tw'

browser = webdriver.Edge('F:\Python\Web__Crawler\msedgedriver.exe')
browser.implicitly_wait(10)
browser.get(url)
#locator = (By.CLASS_NAME,'col3f')
#開起網頁