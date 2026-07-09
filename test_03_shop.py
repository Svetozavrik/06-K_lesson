import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def test_shop_checkout():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("https://www.saucedemo.com/")
        
       
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))
        
      
        products = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt"]
        for product in products:
            add_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, f"//div[text()='{product}']/ancestor::div[@class='inventory_item']//button"))
            )
            add_button.click()
          
        
      
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()
       
        fields = {
            "first-name": "Светлана",
            "last-name": "Баженова",
            "postal-code": "123456"
        }
        for name, value in fields.items():
            field = wait.until(EC.presence_of_element_located((By.ID, name)))
            field.send_keys(value)
          
        
        driver.find_element(By.ID, "continue").click()
        
       
        total_text = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        ).text
        
        
        assert total_text.startswith("Total: $")
        
    finally:
        driver.quit()
