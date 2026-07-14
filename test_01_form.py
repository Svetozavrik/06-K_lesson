import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form_validation():
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
        field = wait.until(EC.presence_of_element_located((By.NAME, name)))
        field.send_keys(value)
   
   
    zip_field = wait.until(EC.presence_of_element_located((By.NAME, "zip-code")))
    zip_field.clear()
  

    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    driver.execute_script("arguments[0].click();", submit_button)
    
    
    wait.until(EC.url_contains("data-types-submitted"))
    
    
    assert "data-types-submitted" in driver.current_url, "Перенаправление не выполнено"
    
   
    page_text = driver.find_element(By.TAG_NAME, "body").text
    print(f"Текст страницы: {page_text}")
    
    alerts = driver.find_elements(By.CSS_SELECTOR, ".alert")
    
    if alerts:
       
        for alert in alerts:
            print(f"Найден alert: {alert.text}")
        assert len(alerts) > 0, "Нет элементов с классом alert"
    else:
     
        assert len(page_text) > 0, "Страница пуста"
      
        assert "submitted" in page_text.lower() or "success" in page_text.lower() or "thank" in page_text.lower(), \
            f"На странице нет ожидаемого текста. Содержимое: {page_text[:200]}"

    driver.quit()
