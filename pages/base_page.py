from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser import Browser



class Base_page(Browser):


    def wait_and_click_element_by_selector(self, by, selector):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, selector)))
        self.driver.find_element(by, selector).click()