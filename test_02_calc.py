import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_slow_calculator():
    
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    try:
        
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        wait = WebDriverWait(driver, 65) 
       
        delay_input = wait.until(EC.presence_of_element_located((By.ID, "delay")))
        delay_input.clear()
        delay_input.send_keys("45")
        
       
        buttons = ["7", "+", "8", "="]
        for btn in buttons:
            button = wait.until(EC.presence_of_element_located((By.XPATH, f"//span[text()='{btn}']")))
            
            driver.execute_script("arguments[0].scrollIntoView(true);", button)
            
            driver.execute_script("arguments[0].click();", button)
          
        
        wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
        result_text = driver.find_element(By.CLASS_NAME, "screen").text
       
        
        assert result_text == "15"
       
    
    finally:
        driver.quit()      
  