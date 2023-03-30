from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as action
from datetime import date
from pathlib import Path
import inspect
import pytest
import random


class Test_sauce:


    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.folderpath = str(date.today())
        Path(self.folderpath).mkdir(exist_ok=True)
        
    


    def teardown (self):
        self.driver.quit()

    def wait_for_element(self,locator):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(locator))


    def test_empty_username_password(self):
        self.wait_for_element((By.ID, "login-button"))
        lgnbtn = self.driver.find_element(By.ID, "login-button").click()
        self.wait_for_element((By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3"))
        required_message = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderpath}\{inspect.currentframe().f_code.co_name}.png")
        assert required_message.text == "Epic sadface: Username is required"

    def test_empty_password(self):
        self.wait_for_element((By.ID, "user-name"))
        username_input = self.driver.find_element(By.ID, "user-name")
        action(self.driver).move_to_element(username_input).click().send_keys("Merve").perform()
        self.wait_for_element((By.ID, "login-button"))
        lgnbtn = self.driver.find_element(By.ID, "login-button").click()
        required_message = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderpath}\{inspect.currentframe().f_code.co_name}.png")
        assert required_message.text == "Epic sadface: Password is required"

    def test_locked_out(self):
        self.wait_for_element((By.ID, "user-name"))
        username_input = self.driver.find_element(By.ID, "user-name")
        action(self.driver).move_to_element(username_input).click().send_keys("locked_out_user").perform()
        self.wait_for_element((By.ID, "password"))
        password_input = self.driver.find_element(By.ID, "password")
        action(self.driver).move_to_element(password_input).click().send_keys("secret_sauce").perform()
        self.wait_for_element((By.ID, "login-button"))
        lgnbtn = self.driver.find_element(By.ID, "login-button").click()
        locked_out_message = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderpath}\{inspect.currentframe().f_code.co_name}.png")
        assert locked_out_message.text == "Epic sadface: Sorry, this user has been locked out."
        

    def test_icon_x(self):
        try:
            icon_username = self.driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(1) > svg")
            icon_password = self.driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(2) > svg")
        except:
            True
        self.wait_for_element((By.ID, "login-button"))
        lgnbtn = self.driver.find_element(By.ID, "login-button").click()
        icon_username = self.driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(1) > svg")
        icon_password = self.driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(2) > svg")
        if icon_username.is_displayed() and icon_password.is_displayed():
            True
        else:
            False #Bosken logine bastik. ikonlar çikmadi sikinti var.
        self.driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error > h3 > button").click()
        try:
            icon_username.is_displayed()
            icon_password.is_displayed()
            False
        except:
            True #("ikonlar tekrar gitti her şey yolunda")
        self.driver.save_screenshot(f"{self.folderpath}\{inspect.currentframe().f_code.co_name}.png")
        



    def test_Page(self):
            self.wait_for_element((By.ID, "user-name"))
            username = self.driver.find_element(By.ID, "user-name")
            action(self.driver).move_to_element(username).click().send_keys("standard_user").perform()
            self.wait_for_element((By.ID, "password"))
            password =self.driver.find_element(By.ID, "password")
            action(self.driver).move_to_element(password).click().send_keys("secret_sauce").perform()
            self.wait_for_element((By.ID, "login-button"))
            lgnbtn = self.driver.find_element(By.ID, "login-button").click()
            Expected_url = "https://www.saucedemo.com/inventory.html"
            WebDriverWait(self.driver,5).until(EC.new_window_is_opened)
            Current_url = self.driver.current_url
            self.driver.save_screenshot(f"{self.folderpath}\{inspect.currentframe().f_code.co_name}.png")
            assert Expected_url == Current_url



            

    def test_Does_Inventory_have_six_items(self):
        self.wait_for_element((By.ID, "user-name"))
        username = self.driver.find_element(By.ID, "user-name")
        action(self.driver).move_to_element(username).click().send_keys("standard_user").perform()
        self.wait_for_element((By.ID, "password"))
        password= self.driver.find_element(By.ID, "password")
        action(self.driver).move_to_element(password).click().send_keys("secret_sauce").perform()
        self.wait_for_element((By.ID, "login-button"))
        lgnbtn = self.driver.find_element(By.ID, "login-button").click()
        WebDriverWait(self.driver,10).until(EC.new_window_is_opened)
        products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        self.driver.save_screenshot(f"{self.folderpath}\{inspect.currentframe().f_code.co_name}.png")
        assert len(products) == 6


    def test_add_to_cart(self):
        self.wait_for_element((By.ID, "user-name"))
        username_input = self.driver.find_element(By.ID, "user-name")
        action(self.driver).move_to_element(username_input).click().send_keys("problem_user").perform()
        self.wait_for_element((By.ID, "password"))
        password_input = self.driver.find_element(By.ID, "password")
        action(self.driver).move_to_element(password_input).click().send_keys("secret_sauce").perform()
        self.wait_for_element((By.ID, "login-button"))
        lgnbtn = self.driver.find_element(By.ID, "login-button").click()
        self.wait_for_element((By. ID, "inventory_container"))
        add_to_cart = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        add_to_cart.click()
        sepet = self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
        sepet.click()
        assert self.driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]')

    @pytest.mark.xfail()
    def test_image_ctrl(self):
        self.wait_for_element((By.ID, "user-name"))
        username_input = self.driver.find_element(By.ID, "user-name")
        action(self.driver).move_to_element(username_input).click().send_keys("problem_user").perform()
        self.wait_for_element((By.ID, "password"))
        password_input = self.driver.find_element(By.ID, "password")
        action(self.driver).move_to_element(password_input).click().send_keys("secret_sauce").perform()
        self.wait_for_element((By.ID, "login-button"))
        lgnbtn = self.driver.find_element(By.ID, "login-button").click()
        self.wait_for_element((By. ID, "inventory_container"))
        entry_images = self.driver.find_elements(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div/div[1]/a/img")
        entry_images_url_list=[]
        for i in entry_images:
                img_url = i.get_attribute("src")
                entry_images_url_list.append(img_url)
        num_of_img = len(entry_images)
        second_images_url_list = []
        for i in range(num_of_img):
            entry_images = self.driver.find_elements(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div/div[1]/a/img")
            WebDriverWait(self.driver,2)
            entry_images[i].click()
            WebDriverWait(self.driver,2)
            second_img = self.driver.find_element(By.CLASS_NAME, "inventory_details_img")
            second_img_url = second_img.get_attribute("src")
            second_images_url_list.append(second_img_url)
            self.driver.find_element(By.ID,"back-to-products").click()
        self.driver.save_screenshot(f"{self.folderpath}\{inspect.currentframe().f_code.co_name}.png")
        for i in range(num_of_img):
            assert entry_images_url_list[i] == second_images_url_list[i]

    @pytest.mark.xfail()
    def test_different_user(self):
        self.wait_for_element((By.ID, "user-name"))
        username_input = self.driver.find_element(By.ID, "user-name")
        action(self.driver).move_to_element(username_input).click().send_keys("problem_user").perform()
        self.wait_for_element((By.ID, "password"))
        password_input = self.driver.find_element(By.ID, "password")
        action(self.driver).move_to_element(password_input).click().send_keys("secret_sauce").perform()
        self.wait_for_element((By.ID, "login-button"))
        lgnbtn = self.driver.find_element(By.ID, "login-button").click()
        self.wait_for_element((By. ID, "inventory_container"))
        add_to_cart = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        burger_button = self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        logout_button = self.driver.find_element(By.ID,"logout_sidebar_link").click()
        self.wait_for_element((By.ID, "user-name"))
        username_input = self.driver.find_element(By.ID, "user-name")
        action(self.driver).move_to_element(username_input).click().send_keys("standard_user").perform()
        self.wait_for_element((By.ID, "password"))
        password_input = self.driver.find_element(By.ID, "password")
        action(self.driver).move_to_element(password_input).click().send_keys("secret_sauce").perform()
        self.wait_for_element((By.ID, "login-button"))
        lgnbtn = self.driver.find_element(By.ID, "login-button").click()
        self.wait_for_element((By. ID, "inventory_container"))
        sepet = self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
        sepet.click()
        self.driver.save_screenshot(f"{self.folderpath}\{inspect.currentframe().f_code.co_name}.png")
        assert not self.driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]')


    @pytest.mark.parametrize("user,secret",[("standard_user","secret_sauce"),
        ("performance_glitch_user","secret_sauce"),
        pytest.param("locked_out_user","secret_sauce", marks=pytest.mark.xfail),
        pytest.param("problem_user","secret_sauce", marks=pytest.mark.xfail)
    ])
    def test_product_num_in_basket(self,user,secret):
        self.wait_for_element((By.ID, "user-name"))
        username_input = self.driver.find_element(By.ID, "user-name")
        action(self.driver).move_to_element(username_input).click().send_keys(user).perform()
        self.wait_for_element((By.ID, "password"))
        password_input = self.driver.find_element(By.ID, "password")
        action(self.driver).move_to_element(password_input).click().send_keys(secret).perform()
        self.wait_for_element((By.ID, "login-button"))
        lgnbtn = self.driver.find_element(By.ID, "login-button").click()
        self.wait_for_element((By. ID, "inventory_container"))
        self.wait_for_element((By. XPATH, "/html/body/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/button"))
        add_cart_buttons = self.driver.find_elements(By. XPATH, "/html/body/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/button")
        random_num= random.randint(1,6)
        random_num= int(random_num)
        index = 0
        for i in range(random_num): 
            add_cart_buttons = self.driver.find_elements(By. XPATH, "/html/body/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/button")
            add_cart_buttons[index].click()
            WebDriverWait(self.driver,2)
            index+=1
        basket= self.driver.find_element(By.CLASS_NAME,"shopping_cart_badge")
        self.driver.save_screenshot(f"{self.folderpath}\{inspect.currentframe().f_code.co_name}.png")
        assert basket.text == str(random_num)

    def test_total_price_ctrl(self):
        self.wait_for_element((By.ID, "user-name"))
        username_input = self.driver.find_element(By.ID, "user-name")
        action(self.driver).move_to_element(username_input).click().send_keys("standard_user").perform()
        self.wait_for_element((By.ID, "password"))
        password_input = self.driver.find_element(By.ID, "password")
        action(self.driver).move_to_element(password_input).click().send_keys("secret_sauce").perform()
        self.wait_for_element((By.ID, "login-button"))
        lgnbtn = self.driver.find_element(By.ID, "login-button").click()
        self.wait_for_element((By. ID, "inventory_container"))
        self.wait_for_element((By. XPATH, "/html/body/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/button"))
        add_cart_buttons = self.driver.find_elements(By. XPATH, "/html/body/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/button")
        prices = self.driver.find_elements(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div")
        price_list =[]
        for i in prices:
            price = i.text.replace("$", "")
            price_list.append(price)
        add_cart_buttons_list = []
        for button in add_cart_buttons:
            add_cart_buttons_list.append(button)
        button_price_list = dict(zip(add_cart_buttons_list,price_list))
        random_num= random.randint(1,6)
        random_num= int(random_num)
        index = 0
        total_value = 0
        for i in range(random_num): 
            add_cart_buttons = self.driver.find_elements(By. XPATH, "/html/body/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/button")
            add_cart_buttons[index].click()
            WebDriverWait(self.driver,2)
            total_value += float(price_list[index])
            index+=1
        self.driver.find_element(By.CLASS_NAME,"shopping_cart_badge").click() #alışveriş sepeti görseli
        self.wait_for_element((By.ID,"checkout"))
        self.driver.find_element(By.ID,"checkout").click() #checkout button
        name = self.driver.find_element(By.ID,"first-name")
        last_name= self.driver.find_element(By.ID,"last-name")
        zip_code= self.driver.find_element(By.ID,"postal-code")
        action(self.driver).move_to_element(name).click().send_keys("Merve").perform()
        action(self.driver).move_to_element(last_name).click().send_keys("Kasal").perform()
        action(self.driver).move_to_element(zip_code).click().send_keys(20000).perform()
        self.driver.find_element(By.ID, "continue").click()
        self.wait_for_element((By.XPATH,"/html/body/div/div/div/div[2]/div/div[2]/div[8]"))
        total_movey_window= self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div[2]/div[8]")
        tax= self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div[2]/div[7]")
        tax_float = float(tax.text.replace("Tax: $",""))
        items_total_on_last_page = float(total_movey_window.text.replace("Total: $",""))
        tax_plus_value = round(total_value+tax_float,2)
        self.driver.save_screenshot(f"{self.folderpath}\{inspect.currentframe().f_code.co_name}.png")
        assert tax_plus_value == items_total_on_last_page





    

            


        






































                    
