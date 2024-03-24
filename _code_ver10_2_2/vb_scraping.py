import tkinter
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pandas as pd

#! chromedriverの指定
chrome_path = r"C:\Users\takac\AppData\Local\Programs\Python\Python311\work__crowdworks\chromedriver.exe"

service = Service(executable_path=chrome_path)
#シークレットモードで行う場合に使うが、ダウンロードの保存先を手動で指定しなければならない
# options = Options()
# options.add_argument("--incognito")
# driver = webdriver.Chrome(service=service,option=options)
driver = webdriver.Chrome(service=service)
d_list =[]



# Italian Serie A1
url = "https://volleybox.net/men-italian-serie-a1-2023-24-o28894/classification"

driver.get(url)
teamlinks = driver.find_elements(By.TAG_NAME,"a")
for teamlink in teamlinks:
  teamlink.text

len(teamlinks)
# Modena
teamlinks[288].text
elementurl = teamlinks[288].get_attribute("href")
driver.get(elementurl)
