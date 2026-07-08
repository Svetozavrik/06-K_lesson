from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_shop_checkout():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)


    user_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#user-name")))
    user_name.send_keys("standard_user")

    password = driver.find_element(By.CSS_SELECTOR, "#password")
    password.send_keys("secret_sauce")

    login_button = driver.find_element(By.CSS_SELECTOR, "#login-button")
    login_button.click()


    products_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]


    for product_name in products_to_add:
        add_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//div[contains(@class, 'inventory_item')]//div[text()='{product_name}']/../../div[@class='pricebar']/button")
            )
        )
        add_button.click()

   
    cart_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".shopping_cart_container a")))
    cart_icon.click()

    checkout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout")))
    checkout_button.click()

    first_name_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#first-name")))
    first_name_input.send_keys("Svetlana")

    last_name_input = driver.find_element(By.CSS_SELECTOR, "#last-name")
    last_name_input.send_keys("Bazhenova")

    postal_code_input = driver.find_element(By.CSS_SELECTOR, "#postal-code")
    postal_code_input.send_keys("123456")

    continue_button = driver.find_element(By.CSS_SELECTOR, "#continue")
    continue_button.click()

   
    total_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".summary_total_label")))
    total_text = total_element.text

    expected_total = "Total: $58.29"
    assert total_text == expected_total, f"Ожидалась сумма {expected_total}, но получено: {total_text}"

    driver.quit()
