from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import ProductPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(By.CSS_SELECTOR, ".basket-items"), "Basket is not empty"

    def should_be_empty_basket_text(self):
        assert self.is_element_present(By.ID, "content_inner"), "Element with id 'content_inner' is not present"
        empty_basket_text = self.browser.find_element(*ProductPageLocators.EMPTY_BASKET_TEXT).text
        assert "Your basket is empty" in empty_basket_text, f"Expected 'Your basket is empty' but got '{empty_basket_text}'"
        
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
    