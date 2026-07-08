from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form_validation():
    driver = webdriver.Edge()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.maximize_window()

    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((By.NAME, "first-name")))

   
    fields_to_fill = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "email": "test@skypro.com",
        "phone-number": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for name, value in fields_to_fill.items():
        field = driver.find_element(By.NAME, name)
        field.clear()
        field.send_keys(value)


    zip_code_field = driver.find_element(By.NAME, "zip-code")
    zip_code_field.clear()

    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

   
    fields = driver.find_elements(By.CSS_SELECTOR, "fieldset input")

    for field in fields:
        name = field.get_attribute("name")
        border_color = field.value_of_css_property("border-color")

       
        if name == "zip-code":
            assert "red" in border_color.lower(), f"Поле {name} должно быть красным, но цвет: {border_color}"
        else:
            assert "green" in border_color.lower(), f"Поле {name} должно быть зелёным, но цвет: {border_color}"

    driver.quit()
