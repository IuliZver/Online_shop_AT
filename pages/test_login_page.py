# test_login_page.py
from .login_page import LoginPage
from .main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_url()
       
def test_guest_should_see_login_form(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_form()

def test_guest_should_see_register_form(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_register_form()