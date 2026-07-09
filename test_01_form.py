import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    wait = WebDriverWait(driver, 10)

    data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for name, value in data.items():
        wait.until(EC.presence_of_element_located((By.NAME, name))).send_keys(value)

    zip_field = wait.until(EC.presence_of_element_located((By.NAME, "zip-code")))
    zip_field.clear()

    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    driver.execute_script("arguments[0].click();", submit_button)


    driver.back()
    wait.until(EC.presence_of_element_located((By.NAME, "zip-code")))

    
    zip_color = driver.find_element(By.NAME, "zip-code").value_of_css_property("border-color").lower()
    assert "#dc3545" in zip_color or "rgb(220, 53, 69)" in zip_color, \
        f"Zip code должен быть красным, а он {zip_color}"

    for name in data.keys():
        color = driver.find_element(By.NAME, name).value_of_css_property("border-color").lower()
        assert "#198754" in color or "rgb(25, 135, 84)" in color, \
            f"Поле {name} должно быть зеленым, а оно {color}"

    driver.quit()
