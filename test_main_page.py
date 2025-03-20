from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from selenium.common.exceptions import NoAlertPresentException
    
def test_guest_can_go_to_login_page(browser):
    link = "https://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    
def test_guest_should_see_login_link(browser):
    link = "https://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    page.should_be_login_link()
    
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "https://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_basket_empty()
    basket_page.is_basket_message_present()