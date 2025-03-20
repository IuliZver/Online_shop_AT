from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)   
    
   #def go_to_login_page(self):
       #link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
       #link.click()
       #alert = self.browser.switch_to.alert
       #alert.accept()   разработчики добавили alert, нужно добавить обработчик. Сейчас selenium.common.exceptions.NoAlertPresentException: Message: no such alert
    
   #def __init__(self, browser, url, timeout=10):
       #self.browser = browser
       #self.url = url
       #self.browser.implicitly_wait(timeout)