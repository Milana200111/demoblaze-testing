from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from faker import Faker



fake = Faker()
username= fake.user_name() + str(fake.random_number(digits=3, fix_len=False))
password= fake.password(length=12)
screenshot_path= os.path.join(os.getcwd(), "checkout_success.png")
def sign_up(driver, wait, username, password):
    driver.find_element(By.ID, "signin2").click()
    wait.until(EC.visibility_of_element_located((By.ID, "sign-username"))).clear()
    driver.find_element(By.ID, "sign-username").send_keys(username)
    driver.find_element(By.ID, "sign-password").send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='Sign up']").click()
    try:
        wait.until(EC.alert_is_present())
        alert = Alert(driver)
        print("Sign up alert:", alert.text)
        alert.accept()
    except:
        print("Sign up alert not found (maybe user already exists).")
    time.sleep(1)


def login(driver, wait, username, password):
    print("\nLogging in...")
    driver.find_element(By.ID, "login2").click()
    wait.until(EC.visibility_of_element_located((By.ID, "loginusername"))).clear()
    driver.find_element(By.ID, "loginusername").send_keys(username)
    driver.find_element(By.ID, "loginpassword").send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='Log in']").click()

    try:
        welcome = wait.until(EC.visibility_of_element_located((By.ID, "nameofuser")))
        print(f"Login successful! {welcome.text}")
    except:
        print("Login attempt failed")


def add_product(driver, wait, category, product_name):
    print(f"\nSelecting product '{product_name}' from the category '{category}'")
    driver.get("https://www.demoblaze.com")
    try:
        cat_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, category)))
        cat_link.click()
    except Exception as e:
        print(f"Could not click category '{category}':", e)
        return False

    time.sleep(1.5)

    try:
        lower_name = product_name.lower()
        xpath_expr = f"//a[@class='hrefch' and contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{lower_name}')]"

        prod = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_expr)))
        print(f"Found product: '{prod.text}', clicking it...")
        # prod = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, product_name)))
        prod.click()
        return True
    except Exception as e:
        print(f"Could not open product '{product_name}':", e)
        return False


def checkout(driver, wait, screenshot_path):
    try:
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Add to cart"))).click()
        wait.until(EC.alert_is_present())
        Alert(driver).accept()
    except Exception as e:
        print("Add to cart issue:", e)
    try:
        wait.until(EC.element_to_be_clickable((By.ID, "cartur"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']"))).click()
    except Exception as e:
        print("Failed to open cart / place order:", e)
        return False
    try:
        wait.until(EC.visibility_of_element_located((By.ID, "name"))).send_keys("Milana K")
        driver.find_element(By.ID, "country").send_keys("India")
        driver.find_element(By.ID, "city").send_keys("Hyderabad")
        driver.find_element(By.ID, "card").send_keys("1234567812345678")
        driver.find_element(By.ID, "month").send_keys("12")
        driver.find_element(By.ID, "year").send_keys("2025")
        driver.find_element(By.XPATH, "//button[text()='Purchase']").click()
    except Exception as e:
        print("checkout failed:", e)
        return False
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Thank you for your purchase!')]")))
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at: {screenshot_path}")
        driver.find_element(By.XPATH, "//button[text()='OK']").click()
        return True
    except Exception as e:
        print("checkout Failed:", e)
        return False

if __name__ == "__main__":
    print("Generated credentials using faker:")
    print(f"Username: {username}")
    print(f"Password: {password}")
    category = input("\nEnter category name (e.g., Phones, Laptops, Monitors): ").strip().capitalize()
    product_name = input("Enter product name (e.g., Samsung galaxy s6): ").strip()
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 12)
    try:
        driver.get("https://www.demoblaze.com")
        driver.maximize_window()
        sign_up(driver, wait, username, password)
        login(driver, wait,username,password)
        if add_product(driver, wait, category, product_name):
            result = checkout(driver, wait, screenshot_path)
            print("\nTest Result:", "Success" if result else "Failed")
        else:
            print("checkout failed ")

    except Exception as e:
        print("\n Unexpected error:", e)

    finally:
        time.sleep(3)
        driver.quit()
