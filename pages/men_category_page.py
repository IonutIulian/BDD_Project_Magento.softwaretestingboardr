import time

from selenium.webdriver.common.by import By
from pages.base_page import Base_page

from selenium.webdriver.support.select import Select


class Men_page(Base_page):


    STYLE1 = (By.XPATH, "//div[@id='narrow-by-list']/div[1]/div[1]")
    STYLE2 = (By.XPATH, "//div[@id='narrow-by-list']/div[1]/div[2]/ol/li[6]/a")
    FABRIC1 = (By.XPATH, "//div[@id='narrow-by-list']/div[6]/div[1]")
    FABRIC2 = (By.XPATH, "//div[@id='narrow-by-list']/div[6]/div[2]/ol/li[1]/a")
    SIZE = (By.ID, "option-label-size-143-item-168")
    COLOR = (By.ID, "option-label-color-93-item-56")
    ADDCART = (By.ID, "product-addtocart-button")


    def category_jackets(self):
        self.driver.find_element(By.LINK_TEXT, "Jackets").click()

    def select_style(self):
        self.wait_and_click_element_by_selector(*self.STYLE1)
        self.wait_and_click_element_by_selector(*self.STYLE2)

    def select_performance_fabric(self):
        self.wait_and_click_element_by_selector(*self.FABRIC1)
        self.wait_and_click_element_by_selector(*self.FABRIC2)

    def sort_results(self,sort):
        sorter = Select(self.driver.find_element(By.ID, "sorter"))
        sorter.select_by_visible_text(sort)

    def cheapest(self):
        self.driver.find_elements(By.CLASS_NAME, "product-item-link")[0].click()

    def size_color(self):
        self.wait_and_click_element_by_selector(*self.SIZE)
        self.wait_and_click_element_by_selector(*self.COLOR)

    def add_cart(self):

        self.wait_and_click_element_by_selector(*self.ADDCART)
        time.sleep(3)


