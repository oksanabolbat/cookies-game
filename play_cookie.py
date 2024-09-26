import time

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://orteil.dashnet.org/cookieclicker/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get(URL)

driver.find_element(By.CSS_SELECTOR, "button.fc-button.fc-cta-consent.fc-primary-button").click()

driver.implicitly_wait(3)
driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]').click()

is_started = False

while not is_started:
    try:
        cookie_btn = driver.find_element(By.ID, "bigCookie")
        is_started = True
    except Exception as error:
        print(error)
        driver.implicitly_wait(1)



timeout = time.time() + 6

game_duration = time.time() + 5 * 60


def get_cookies_count():
    cookies_str = driver.find_element(By.ID, "cookies").text.split(" ")
    return int(cookies_str[0].strip().replace(",", ""))


while True:
    cookie_btn.click()
    if time.time() > timeout:
        # shop_products = driver.find_elements(By.CSS_SELECTOR, "#products .enabled")
        shop_products = driver.find_elements(By.CSS_SELECTOR, "#products .unlocked")
        if len(shop_products) > 0:
            shop_products[-1].click()

        timeout += 6
    if time.time() > game_duration:
        cookies = get_cookies_count()
        print(f"Game info: {driver.find_element(By.ID, "cookies").text}")
        driver.close()
        break
