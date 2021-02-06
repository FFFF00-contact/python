from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import time


def initDriver(filePath):
    chrome_options = webdriver.ChromeOptions()
    # config open chrome theo specific path
    chrome_options.add_argument("user-data-dir=" + filePath)  # chrome profile
    # config ko load anh
    """prefs = {
    "profile.managed_default_content_settings.images": 2
    }
    chrome_options.add_experimental_option("prefs", prefs)
    """
    driver = webdriver.Chrome("chromedriver.exe", chrome_options=chrome_options)
    return driver
def comment(filePath):
    driver = initDriver(filePath)
    driver.get("https://www.facebook.com/Nvthang7749/friends_all")
    time.sleep(10)


    time.sleep(10000)
    driver.close()
filePath = "request"
comment(filePath)
#\34 84165359411070 > div._2b04 > div._14v5 > div > div:nth-child(2)