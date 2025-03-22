import pytest
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from .pages.main_page import MainPage

@pytest.mark.need_review
@pytest.mark.parametrize('promo_code', [0,1,2,3,4,5,6, pytest.param(7, marks=pytest.mark.xfail), 8,9])
def test_guest_can_add_product_to_basket(browser, promo_code):
    PRODUCT_URL = ('https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{}'.format(promo_code))
    page = ProductPage(browser, PRODUCT_URL)
    page.open()
    page.should_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_success_message()
    page.should_be_correct_basket_total()
    

    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
 
@pytest.mark.need_review 
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review 
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_text()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):        
        link = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user()
        page.should_be_authorized_user()
        
    def test_user_cant_see_success_message(self, browser):
        link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
        
    @pytest.mark.need_review    
    def test_user_can_add_product_to_basket(self, browser):
        link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_add_product_to_basket()
        page.should_be_success_message()
        page.should_be_correct_basket_total()


@pytest.mark.xfail                                                    
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()
    
def test_guest_cant_see_success_message(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
 
@pytest.mark.xfail 
def test_message_disappeared_after_adding_product_to_basket(browser): 
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_disappear_success_message()  
