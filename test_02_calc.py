from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 45)  
delay_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#delay")))
delay_input.clear()
delay_input.send_keys("45")

buttons = {
        "7": "//button[text()='7']",
        "+": "//button[text()='+']",
        "8": "//button[text()='8']",
        "=": "//button[text()='=']"
    }

for key in ["7", "+", "8", "="]:
        btn = wait.until(EC.element_to_be_clickable((By.XPATH, buttons[key])))
        btn.click()


result_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#result")))
result_text = result_element.text.strip()
assert result_text == "15"

driver.quit()