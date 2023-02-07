from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#^ is webdriver-manager in pycharm for package

#chrome_driver_path = "C:\\Users\\rnicosia\\Documents\\Python\\Selenium\\chromedriver.exe"
allbirds_site = "https://www.allbirds.com/products/trino-sprinters-low-navy-night"
mysite = "https://rnicosia.pythonanywhere.com/"
#driver = wd.Chrome(executable_path=chrome_driver_path)
driver = wd.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(mysite)
driver.implicitly_wait(3)
sock_price = driver.find_element(By.XPATH, "/html/body/main/div/div/div/div/div/div/div/div/div/div/div/p[@class_name='jsx-3188494938 Paragraph PdpMasterProductDetails__paragraph']")
print(sock_price.text)
driver.quit()
