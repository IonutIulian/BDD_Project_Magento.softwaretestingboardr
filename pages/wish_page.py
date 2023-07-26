import time

from pages.base_page import Base_page
from selenium.webdriver.common.by import By


class Wish_page(Base_page):

    SHARE_BUTTON1 = (By.XPATH,"//button[@name='save_and_share']")
    SHARE_BUTTON2 = (By.XPATH,'//button[@title="Share Wish List"]')
    MESSAGE = (By.XPATH,'//main[@id="maincontent"]/div[1]/div[2]/div')

    def share_wish(self):
        time.sleep(3)
        self.driver.find_element(*self.SHARE_BUTTON1).click()

    def enter_emails(self, emails):
        self.driver.find_element(By.ID,"email_address").send_keys(emails)

    def enter_message(self, message):
        self.driver.find_element(By.ID,"message").send_keys(message)

    def share(self):
        self.driver.find_element(*self.SHARE_BUTTON2).click()

    def confirm(self):
        confirm_msg = self.driver.find_element(*self.MESSAGE)
        assert confirm_msg.is_displayed(),"Error, message not found!"
