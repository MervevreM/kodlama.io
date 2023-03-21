from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class sauce:
    def empty_username_password(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(5)
        lgnbtn = driver.find_element(By.ID, "login-button")
        sleep(5)
        lgnbtn.click()
        sleep(5)
        required_message = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        test_result = required_message.text == "Epic sadface: Username is required"
        print(f"TEST SONUCU: {test_result}")

    def empty_password(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(5)
        username_input = driver.find_element(By.ID, "user-name")
        username_input.click()
        sleep(2)
        username_input.send_keys("merve")
        sleep(2)
        lgnbtn = driver.find_element(By.ID, "login-button")
        sleep(5)
        lgnbtn.click()
        required_message = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        test_result = required_message.text == "Epic sadface: Password is required"
        print(f"TEST SONUCU: {test_result}")

    def locked_out(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(5)
        username_input = driver.find_element(By.ID, "user-name")
        username_input.click()
        sleep(2)
        username_input.send_keys("locked_out_user")
        sleep(2)
        password_input = driver.find_element(By.ID, "password")
        sleep(2)
        password_input.click()
        password_input.send_keys("secret_sauce")
        lgnbtn = driver.find_element(By.ID, "login-button")
        sleep(5)
        lgnbtn.click()
        locked_out_message = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        test_result = locked_out_message.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"TEST SONUCU: {test_result}")

    def icon_x(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(5)
        try:
            icon_username = driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(1) > svg")
            icon_password = driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(2) > svg")
        except:
            print("İkonlar yok her şey yolunda")
        sleep(2)
        lgnbtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        lgnbtn.click()
        sleep(5)
        icon_username = driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(1) > svg")
        icon_password = driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(2) > svg")
        if icon_username.is_displayed() and icon_password.is_displayed():
            print("ikonlar görünüyüor her şey yolunda")
        else:
            print("Bosken logine bastik. ikonlar çikmadi sikinti var.")
        carpi_isareti= driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error > h3 > button").click()
        sleep(5)
        try:
            icon_username.is_displayed()
            icon_password.is_displayed()
        except:
            print("ikonlar tekrar gitti her şey yolunda")
        
        print("sonunda yaptin kiz merve")



    def Page(self):
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get("https://www.saucedemo.com/")
            driver.maximize_window()
            sleep(5)
            username_input = driver.find_element(By.ID, "user-name")
            username_input.click()
            sleep(2)
            username_input.send_keys("standard_user")
            sleep(2)
            password_input = driver.find_element(By.ID, "password")
            sleep(2)
            password_input.click()
            password_input.send_keys("secret_sauce")
            lgnbtn = driver.find_element(By.ID, "login-button")
            sleep(5)
            lgnbtn.click()
            Expected_url = "https://www.saucedemo.com/inventory.html"
            Current_url = driver.current_url
            if Expected_url == Current_url:
                print("Yönlendirme işlemi başarili")
            else:
                print("Yönlendirme hatali")


        
            

    def Does_Inventory_have_six_items(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(5)
        username_input = driver.find_element(By.ID, "user-name")
        username_input.click()
        sleep(2)
        username_input.send_keys("standard_user")
        sleep(2)
        password_input = driver.find_element(By.ID, "password")
        sleep(2)
        password_input.click()
        password_input.send_keys("secret_sauce")
        lgnbtn = driver.find_element(By.ID, "login-button")
        sleep(5)
        lgnbtn.click()
        sleep(2)
        inventory_list = driver.find_elements(By.CLASS_NAME, "inventory_item")
        if len(inventory_list) == 6:
            print("Gösterilen ürün sayisi doğru. (6)")
        else:
            print("Gösterilen ürün sayisinda sikinti var")


testClass = sauce()
#testClass.Page()
#testClass.empty_username_password()
testClass.Does_Inventory_have_six_items()
#testClass.locked_out()
#testClass.empty_password()
#testClass.icon_x
