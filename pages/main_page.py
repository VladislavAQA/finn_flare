from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    man_catalog = "/html/body/header/div[3]/div[3]/div/div[3]/div[1]/div/a"
    word_catalog_for_man = "/html/body/main/div/div[1]/h1"

    # Getters
    def get_man_catalog(self):
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.man_catalog)))

    def get_word_catalog_for_man(self):
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.word_catalog_for_man)))

    # Actions
    def button_catalog_for_man(self):
        self.get_man_catalog().click()

    # Methods
    def catalog_for_men(self):
        """ Проверяем в правильном ли мы каталоге """
        self.get_current_url()
        self.button_catalog_for_man()
        self.assert_word(self.get_word_catalog_for_man(), 'Коллекция мужской одежды FiNN FLARE')
        self.assert_url('https://www.finn-flare.kz/catalog/muzhskaya-odezhda/')
