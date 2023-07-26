import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import Base_page


class Home_page(Base_page):
    WELCOME_MSG = (By.XPATH,'//header[@class="page-header"]/div[1]/div/ul/li[1]')
    ACCES_CART = (By.XPATH, "//a[@class='action showcart']")
    PERFORM_CHECKOUT = (By.ID, "top-cart-btn-checkout")
    CHECK_REVIEWS = (By.XPATH, "//div[@class='reviews-actions']")
    SUBMIT = (By.XPATH,'//button[@class="action submit primary"]')
    CHECK_MSG =(By.XPATH,'//div[@class="message-success success message"]')
    ARROW = (By.XPATH,"//a[@class='action skip contentarea']/following-sibling::ul/li[2]/span/button")
    OUT_MSG = (By.XPATH,"//*[@id='maincontent']/div[3]/div/p")
    SIGN_IN = (By.XPATH,"//a[@class='action skip contentarea']/following-sibling::ul/li[2]/a")
    ADD_COMPARE = (By.XPATH,'//*[@id="maincontent"]/div[2]/div/div[1]/div[5]/div/a[2]')
    WISH_LIST = (By.XPATH,'/html/body/div[2]/header/div[1]/div/ul/li[2]/div/ul/li[2]')

    def navigate_to_homepage(self):

        self.driver.get("https://magento.softwaretestingboard.com/")
        time.sleep(5)

    def check_url(self):
        actual_url = self.driver.current_url
        expected_url = "https://magento.softwaretestingboard.com/"
        assert actual_url==expected_url, f"Error, expected url:{expected_url} , actual:{actual_url}!"

    def check_welcome_msg(self):
        welcome_msg = self.driver.find_element(*self.WELCOME_MSG)
        assert welcome_msg.is_displayed(),"Error, the message is not displayed!"


    def click_create_account(self):
        self.driver.find_element(By.LINK_TEXT, "Create an Account").click()

    def category_men(self):
        self.driver.find_element(By.LINK_TEXT,"Men").click()

    def acces_cart(self):

        self.wait_and_click_element_by_selector(*self.ACCES_CART)
        time.sleep(4)

    def perform_checkout(self):

        self.wait_and_click_element_by_selector(*self.PERFORM_CHECKOUT)

    def search_item(self, item_name):
        self.driver.find_element(By.ID, "search").send_keys(item_name)
        self.driver.find_element(By.ID, "search").send_keys(Keys.ENTER)

    def add_to_wishlist(self):
        self.driver.find_elements(By.CLASS_NAME, "product-item-info")[0].click()
        self.driver.find_element(By.CLASS_NAME, "towishlist").click()

    def check_reviews(self):
        self.driver.find_element(*self.CHECK_REVIEWS).click()

    def rate_item(self):
        rate = self.driver.find_element(By.ID, "Rating_4_label")
        self.driver.execute_script('arguments[0].style="width:100%"; arguments[0].click()', rate)

    def write_review(self,review_title,text_review):
        self.driver.find_element(By.ID, "summary_field").send_keys(review_title)
        self.driver.find_element(By.ID, "review_field").send_keys(text_review)

    def submit_check_message(self):
        self.driver.find_element(*self.SUBMIT).click()
        message = self.driver.find_element(*self.CHECK_MSG)
        assert message.is_displayed(),"Error, message not found!"


    def click_arrow(self):
        self.driver.find_element(*self.ARROW).click()
        time.sleep(4)

    def sign_out(self):
        self.driver.find_element(By.LINK_TEXT,"Sign Out").click()

    def sign_out_msg(self):
        signout_msg = self.driver.find_element(*self.OUT_MSG)
        assert signout_msg.is_displayed(),"Error, message not found!"

    def sign_in(self):
        self.driver.find_element(*self.SIGN_IN).click()

    def click_item(self):
        self.driver.find_elements(By.CLASS_NAME, "product-item-info")[0].click()

    def add_compare(self):
        self.driver.find_element(*self.ADD_COMPARE).click()

    def check_confirmation(self):
        confi = self.driver.find_element(By.XPATH, "//div[@role='alert']")
        assert confi.is_displayed(), "Error, message not found!"

    def compare_products(self):
        self.driver.find_element(By.XPATH,"//a[@class='action compare']").click()

    def to_wish_list(self):
        self.driver.find_element(*self.WISH_LIST).click()



