import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base


class CatalogPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    filter_size = "//*[@id='filter_form']/div[1]/div[1]/div[1]"
    size_choice = "//*[@id='filter_form']/div[1]/div[1]/div[2]/div/label[3]/div"
    filter_colour = "//*[@id='filter_form']/div[1]/div[2]/div[1]"
    colour_choice = "//*[@id='filter_form']/div[1]/div[2]/div[2]/div/label[2]"
    filter_price = "//*[@id='filter_form']/div[1]/div[5]/div[1]"
    price_choice = "//*[@id='filter_form']/div[1]/div[5]/div[2]/div/div/div/span[2]"
    filter_sorted = "//*[@id='filter_form']/div[1]/div[6]/div[1]"
    sorted_choice = "//*[@id='filter_form']/div[1]/div[6]/div[2]/div/label[2]"

    apply_button = "//*[@id='filter-submit']"

    ad_banner_close = "//*[@id='popmechanic-form-41090']/div[1]/div[2]/div[3]"

    choice_product = "/html/body/main/div/div[1]/div[5]/div[1]/a/div[3]/div"

    filter_size_in_cart = "/html/body/main/form/div/div[2]/div/div[5]/div[2]"
    choice_size_in_cart = "/html/body/main/form/div/div[2]/div/div[5]/div[4]/div/label[2]/span/span[1]"
    button_put_cart = "//*[@id='product_tobasket']"
    button_go_to_cart = "/html/body/main/form/div/div[2]/div/div[7]/div[1]/a"

    # Getters
    def get_filter_size(self):
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.filter_size)))

    def get_size_choice(self):
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.size_choice)))

    def get_filter_colour(self):
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.filter_colour)))

    def get_colour_choice(self):
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.colour_choice)))

    def get_filter_price(self):
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.filter_price)))

    def get_price_choice(self):
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.price_choice)))

    def get_ad_banner_close(self):
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.ad_banner_close)))

    def get_apply_button(self):
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.apply_button)))

    def get_choice_product(self):
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.choice_product)))

    def get_filter_sorted(self):
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.filter_sorted)))

    def get_sorted_choice(self):
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.sorted_choice)))

    def get_filter_size_in_cart(self):
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.filter_size_in_cart)))

    def get_choice_size_in_cart(self):
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.choice_size_in_cart)))

    def get_button_put_cart(self):
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.button_put_cart)))

    def get_button_go_to_cart(self):
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.button_go_to_cart)))

    # Actions
    def click_filter_size(self):
        self.get_filter_size().click()

    def click_size_choice(self):
        self.get_size_choice().click()

    def click_filter_colour(self):
        self.get_filter_colour().click()

    def click_colour_choice(self):
        self.get_colour_choice().click()

    def click_filter_price(self):
        self.get_filter_price().click()

    def click_price_choice(self):
        self.action_method(self.get_price_choice())

    def click_filter_sorted(self):
        self.get_filter_sorted().click()

    def click_sorted_choice(self):
        self.get_sorted_choice().click()

    def click_ad_banner_close(self):
        self.get_ad_banner_close().click()

    def click_apply_button(self):
        self.get_apply_button().click()

    def click_choice_product(self):
        self.get_choice_product().click()

    def click_filter_size_in_cart(self):
        self.get_filter_size_in_cart().click()

    def click_choice_size_in_cart(self):
        self.get_choice_size_in_cart().click()

    def click_button_put_cart(self):
        self.get_button_put_cart().click()

    def click_button_go_to_cart(self):
        self.get_button_go_to_cart().click()

    # Methods
    def check_ad_banner(self):
        """ Убираем рекламный баннер """
        if self.click_ad_banner_close():
            self.click_ad_banner_close()

    def choice_and_apply_filter(self):
        """ Выбираем фильтры и нажимаем применить """
        self.get_current_url()
        self.click_filter_size()
        self.click_size_choice()
        self.click_filter_colour()
        self.click_colour_choice()
        self.click_filter_price()
        self.click_price_choice()
        self.click_filter_sorted()
        self.click_sorted_choice()
        self.click_apply_button()
        time.sleep(5)
        self.assert_word(self.get_choice_product(), 'Утепленное двустороннее полупальто с капюшоном')
        self.click_choice_product()

    def choose_product_in_cart(self):
        """ Выбираем размер продукта и кладём в корзину """
        self.click_filter_size_in_cart()
        self.click_choice_size_in_cart()
        self.click_button_put_cart()
        self.click_button_go_to_cart()
