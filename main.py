from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.python.org/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)

driver.get(URL)
upcoming_events = {}
events_html = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul.menu li")
for event in events_html:
    event_time_tag = event.find_element(By.TAG_NAME, "time")
    event_time = event_time_tag.get_attribute("datetime")
    upcoming_events[len(upcoming_events)+1] = {"time": event_time[0:10], "name": event.find_element(By.TAG_NAME, "a").text}

print(upcoming_events)
driver.close()
# driver.quit()

