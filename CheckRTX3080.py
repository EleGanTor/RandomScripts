from bs4 import BeautifulSoup
from selenium import webdriver
import time

if __name__ == '__main__':
    url = 'https://www.mediamarkt.de/de/product/_msi-geforce-rtx%E2%84%A2-3080-ventus-3x-oc-10gb-v389%E2%80%90001r-2683229.html'
    driver = webdriver.Chrome('chromedriver.exe')
    driver.maximize_window()
    driver.get(url)
    site = driver.page_source

    while True:
        print(driver.page_source)
        time.sleep(60)
        driver.refresh()