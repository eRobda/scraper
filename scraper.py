from selenium import webdriver
from selenium.webdriver.common.by import By

jmeno = input();

driver = webdriver.Chrome()

url = 'https://prehrajto.cz/'
driver.get(url)

driver.execute_script(f"document.getElementById('search-phrase').value = '{jmeno}';")
driver.execute_script("document.querySelector('button').click();")
driver.execute_script("document.querySelectorAll('a')[7].click();")

video_elements = driver.find_elements(By.TAG_NAME, 'video')

video_src = video_elements[0].get_attribute('src')

print(video_src)