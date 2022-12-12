from selenium import webdriver

from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_smoke_buy_product():
    """ Smoke test buy product """
    driver = webdriver.Chrome(executable_path="D:\\PyDoc\\resource\\chromedriver.exe")
    print('Start: ' + test_smoke_buy_product.__name__)

    lp = LoginPage(driver)
    lp.authorization()

    mp = MainPage(driver)
    mp.catalog_for_men()

    cp = CatalogPage(driver)
    cp.check_ad_banner()
    cp.choice_and_apply_filter()
    cp.choose_product_in_cart()

    cart = CartPage(driver)
    cart.check_cart()

    print('Finish: ' + test_smoke_buy_product.__name__)
