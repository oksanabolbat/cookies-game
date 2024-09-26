from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://en.wikipedia.org/wiki/Main_Page"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get(URL)
count_tag = driver.find_element(By.CSS_SELECTOR, "div#articlecount a")
print(count_tag.text)
driver.close()
