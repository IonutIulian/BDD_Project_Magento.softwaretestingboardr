from selenium.webdriver.common.by import By
from pages.base_page import Base_page
from selenium.webdriver.common.keys import Keys



class Account_page(Base_page):

    PASS_MSG = (By.ID, "password-strength-meter")
    PASS_CONFI = (By.ID, "password-confirmation")
    CREATE_BUTTON = (By.XPATH, "//button[@title='Create an Account']")
    REGIST_MSG = (By.XPATH,"//div[@class='message-success success message']")


    def enter_names_email(self,first_name,last_name,email):
        self.driver.find_element(By.ID, "firstname").send_keys(first_name)
        self.driver.find_element(By.ID, "lastname").send_keys(last_name)
        self.driver.find_element(By.ID, "email_address").send_keys(email)

    def sign_newsletter(self):
        self.driver.find_element(By.ID, "is_subscribed").click()

    def weak_password(self,pass_1):
        self.driver.find_element(By.ID,"password").send_keys(pass_1)

    def strong_pass_check_msg(self,pass_2):
        securemsg = self.driver.find_element(*self.PASS_MSG).text
        if securemsg != "Password Strength: Strong" or securemsg != "Password Strength: Very Strong":
            try:

                self.driver.find_element(By.ID, "password").send_keys(Keys.CONTROL + "a")
                self.driver.find_element(By.ID, "password").send_keys(Keys.BACK_SPACE)
                self.driver.find_element(By.ID, "password").send_keys(pass_2)
            except:
                pass

    def confirm_pass(self,same_pass):
        self.driver.find_element(*self.PASS_CONFI).send_keys(same_pass)

    def click_create(self):
        self.driver.find_element(*self.CREATE_BUTTON).click()

    def regist_msg(self):
        regist_msg=self.driver.find_element(*self.REGIST_MSG)
        assert regist_msg.is_displayed(),"Error, message not found!"

