import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
    jmeno = request.form["url"]
    driver = webdriver.Chrome()

    url = 'https://prehrajto.cz/'
    driver.get(url)

    driver.execute_script(f"document.getElementById('search-phrase').value = '{jmeno}';")
    driver.execute_script("document.querySelector('button').click();")
    driver.execute_script("document.querySelectorAll('a')[7].click();")

    video_elements = driver.find_elements(By.TAG_NAME, 'video')

    video_src = video_elements[0].get_attribute('src')

    return video_src
