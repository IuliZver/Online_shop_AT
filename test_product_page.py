import pytest
from .product_page import ProductPage
from .base_page import BasePage
from .login_page import LoginPage

@pytest.mark.parametrize('promo_code', [0,1,2,3,4,5,6, pytest.param(7, marks=pytest.mark.xfail), 8,9])
def test_guest_can_add_product_to_basket(browser, promo_code):
    PRODUCT_URL = ('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{}'.format(promo_code))
    page = ProductPage(browser, PRODUCT_URL)
    page.open()
    page.solve_quiz_and_get_code()
    page.should_add_product_to_basket()
    page.should_be_success_message()
    page.should_be_correct_basket_total()
    
 
"""@pytest.mark.parametrize('link', ["okay_link",
                                  pytest.param("bugged_link", marks=pytest.mark.xfail),
                                  "okay_link"])"""
                           

    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()