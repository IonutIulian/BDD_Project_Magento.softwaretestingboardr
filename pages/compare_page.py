import time

from pages.base_page import Base_page
from selenium.webdriver.common.by import By


class Compare_page(Base_page):

    CANCEL = (By.XPATH,'//table[@id="product-comparison"]/thead/tr/td[1]/a')
    OK_BUTTON = (By.XPATH,'//footer[@class="modal-footer"]/button[2]')
    WISH_BUTTON = (By.XPATH,"//table[@id='product-comparison']/tbody[1]/tr/td/div[2]/div[2]/a")
    def cancel_item(self):
        self.wait_and_click_element_by_selector(*self.CANCEL)

        self.wait_and_click_element_by_selector(*self.OK_BUTTON)

    def add_wishlist(self):
        time.sleep(3)
        self.wait_and_click_element_by_selector(*self.WISH_BUTTON)