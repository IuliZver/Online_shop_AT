import pytest
from .product_page import ProductPage
from .main_page import MainPage

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