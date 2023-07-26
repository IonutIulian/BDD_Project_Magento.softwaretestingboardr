import time
from selenium.webdriver.common.by import By
from pages.base_page import Base_page
from selenium.webdriver.support.select import Select



class Checkout_page(Base_page):

    STREET = (By.XPATH, "//input[@name='street[0]']")
    COUNTRY = (By.XPATH, "//select[@name='country_id']")
    REGION = (By.XPATH, "//select[@name='region_id']")
    POSTCODE = (By.XPATH, "//input[@name='postcode']")
    CITY = (By.XPATH, "//input[@name='city']")
    PHONE = (By.XPATH, "//input[@name='telephone']")
    NEXT = (By.XPATH, '//*[@id="shipping-method-buttons-container"]/div/button')
    PLACE = (By.XPATH,'//*[@id="checkout-payment-method-load"]/div/div/div[2]/div[2]/div[4]/div/button')

    def street_address(self, street):
        self.driver.find_element(*self.STREET).send_keys(street)

    def country_region(self, state, province):
        country = Select(self.driver.find_element(*self.COUNTRY))
        country.select_by_visible_text(state)
        region = Select(self.driver.find_element(*self.REGION))
        region.select_by_visible_text(province)


    def postcode_city(self, postcode, city):
        self.driver.find_element(*self.POSTCODE).send_keys(postcode)
        self.driver.find_element(*self.CITY).send_keys(city)

    def phone_number(self,phone):
        self.driver.find_element(*self.PHONE).send_keys(phone)
        time.sleep(5)


    def next_place_order(self):

        self.wait_and_click_element_by_selector(*self.NEXT)
        time.sleep(5)
        self.wait_and_click_element_by_selector(*self.PLACE)


