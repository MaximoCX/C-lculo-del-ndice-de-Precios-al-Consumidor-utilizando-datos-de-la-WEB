from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service

import time

def main():
    service=Service(ChromeDriverManager().install())
    option=webdriver.ChromeOptions()
    option.add_argument("--window-size=1920,1080")
    driver=Chrome(service=service, options=option)
    driver.get("https://www.google.com/")
    time.sleep(5)
    driver.quit()

    

if __name__ == "__main__":
    main()