from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "http://secure-retreat-92358.herokuapp.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)

driver.get(URL)

driver.find_element(By.NAME, "fName").send_keys("Oksana")
driver.find_element(By.NAME, "lName").send_keys("my last name")
driver.find_element(By.NAME, "email").send_keys("email@email.com", Keys.ENTER)


# driver.close()