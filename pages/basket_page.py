from .base_page import BasePage
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def is_basket_empty(self):
        empty_basket_element = self.browser.find_elements(By.CSS_SELECTOR, "#content_inner p")
        assert any("Your basket is empty" in element.text for element in empty_basket_element), "Корзина не пуста."

    def is_basket_message_present(self):
        message_element = self.browser.find_elements(By.CSS_SELECTOR, "#content_inner p")
        assert any("Your basket is empty" in element.text for element in message_element), "Текст о пустой корзине отсутствует."
        
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    