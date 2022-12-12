from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    product_price = "/html/body/main/form/div/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div[1]"
    product_name = "/html/body/main/form/div/div[1]/div[2]/div/div/div[2]/p[1]/a"
    button_buy_order = "//*[@id='basketOrderButton2']"

    # Getters
    def get_product_price(self):
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.product_price)))

    def get_product_name(self):
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.product_name)))

    def get_button_buy_order(self):
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.button_buy_order)))

    # Actions
    def click_button_buy_order(self):
        self.get_button_buy_order().click()

    # Methods
    def check_cart(self):
        """ Проверяем наличие товара в корзине """
        self.get_current_url()
        self.get_screenshot()
        self.assert_url('https://www.finn-flare.kz/personal/cart/')
        self.assert_word(self.get_product_name(), 'Утепленное двустороннее полупальто с капюшоном FWB21015')
        self.assert_word(self.get_product_price(), '106 500 тг.')
        self.click_button_buy_order()
