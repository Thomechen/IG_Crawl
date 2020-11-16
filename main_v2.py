import urllib.request
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re
import os

#套件輸入
url = 'https://www.instagram.com/?hl=zh-tw'

browser = webdriver.Chrome('.\chromedriver.exe')
browser.implicitly_wait(10)
browser.get(url)

#開起網頁
username = 'austin6614@yahoo.com'
password = 'tp6w/6cj/6'

element = browser.find_element_by_name('username')
element.send_keys(username)
element = browser.find_element_by_name('password')
element.send_keys(password)

submit = browser.find_element_by_class_name('sqdOP.L3NKy.y3zKF').click()
locator = (By.CLASS_NAME,'cmbtv')
WebDriverWait(browser,5).until(EC.presence_of_element_located(locator))#等待網頁網取
submit = browser.find_element_by_class_name('sqdOP.yWX7d.y3zKF').click()
locator = (By.CLASS_NAME,'mt3GC')
WebDriverWait(browser,5).until(EC.presence_of_element_located(locator))#等待網頁網取
submit = browser.find_element_by_class_name('aOOlW.HoLwm').click()


main = ['0.search','1.close']

search_title_list = []
search_title_link_list = []
img_list = []


while True:
    for i in range(len(main)):
        print(main[i])
    fun = input('Enter your function:')
    if int(fun) == 0:
        search = input('Enter the keyword:')
        path = './'
        element = browser.find_element_by_class_name('XTCLo.x3qfX')
        element.send_keys(search)
        locator = (By.CLASS_NAME,'fuqBx')
        WebDriverWait(browser,5).until(EC.presence_of_element_located(locator))#等待網頁網取
        soup = BeautifulSoup(browser.page_source,'html.parser')
        search_title = soup.select('span.Fy4o8')
        search_title_link = soup.select('a.yCE8d')
        for t,t_1 in zip(search_title,search_title_link):
            search_title_list.append(t.text)
            search_title_link_list.append('https://www.instagram.com'+t_1.get('href'))
        for i in range(len(search_title_list)):
            print(str(i)+':'+str(search_title_list[i]))
            print(' ')
        search_no = input('Enter the No.:')
        print('')
        os.mkdir(path+search)
        browser.get(search_title_link_list[int(search_no)])
        soup = BeautifulSoup(browser.page_source,'html.parser')
        img = soup.select('img.FFVAD')
        for g in img:
            img_list.append(g.get('src'))
        for i in range(len(img_list)):
            urllib.request.urlretrieve(img_list[i], './'+search+'/'+str(i) +'.jpg')
            
        submit = browser.find_element_by_class_name('Igw0E.rBNOH.eGOV_.ybXk5._4EzTm').click()
    elif int(fun) == 1:
        browser.close()
        break
    
    