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

    driver.find_element(By.NAME, "first-name").clear()
    driver.find_element(By.NAME, "first-name").send_keys("Иван")

    driver.find_element(By.NAME, "last-name").clear()
    driver.find_element(By.NAME, "last-name").send_keys("Петров")

    driver.find_element(By.NAME, "address").clear()
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")

    driver.find_element(By.NAME, "email").clear()
    driver.find_element(By.NAME, "email").send_keys("test@skypro.com")

    driver.find_element(By.NAME, "phone-number").clear()
    driver.find_element(By.NAME, "phone-number").send_keys("+7985899998787")

    
    zip_code_field = driver.find_element(By.NAME, "zip-code")
    zip_code_field.clear()

    driver.find_element(By.NAME, "city").clear()
    driver.find_element(By.NAME, "city").send_keys("Москва")

    driver.find_element(By.NAME, "country").clear()
    driver.find_element(By.NAME, "country").send_keys("Россия")

    driver.find_element(By.NAME, "job-position").clear()
    driver.find_element(By.NAME, "job-position").send_keys("QA")

    driver.find_element(By.NAME, "company").clear()
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    fields = driver.find_elements(By.CSS_SELECTOR, "fieldset input")
      
    for field in fields:
        name = field.get_attribute("name")
        border_color = field.value_of_css_property("border-color")

    if name == "zip-code":
           
            assert "red" in border_color.lower()
    else:
            assert "green" in border_color.lower()
    

            driver.quit()
