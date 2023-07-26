from pages.base_page import Base_page
from selenium.webdriver.common.by import By


class Login_page(Base_page):

    def enter_email(self, email):
        self.driver.find_element(By.ID, "email").send_keys(email)

    def enter_password(self ,passowrd):
        self.driver.find_element(By.ID,"pass").send_keys(passowrd)

    def click_signin(self):
        self.driver.find_element(By.ID,"send2").click()