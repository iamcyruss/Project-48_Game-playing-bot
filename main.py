from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_driver_path = "C:\\Users\\rnicosia\\Documents\\Python\\Selenium\\chromedriver.exe"
#driver = wd.Chrome(executable_path=chrome_driver_path)
driver = wd.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.amazon.com")
driver.close()
