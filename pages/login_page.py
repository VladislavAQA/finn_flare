from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base


class LoginPage(Base):
    url = 'https://www.finn-flare.kz/auth/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    username_loc = "//input[@id='login-input']"
    password_loc = "//input[@id='user-password']"
    login_button_loc = "/html/body/div[4]/form/button"
    main_word = "/html/body/main/div[2]/div/div[1]/a"

    # Getters
    def get_user_name(self):
        return WebDriverWait(self.driver, 25).until(
            ec.element_to_be_clickable((By.XPATH, self.username_loc)))

    def get_password(self):
        return WebDriverWait(self.driver, 25).until(
            ec.element_to_be_clickable((By.XPATH, self.password_loc)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 25).until(
            ec.element_to_be_clickable((By.XPATH, self.login_button_loc)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 25).until(
            ec.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions
    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)

    def input_password(self, password):
        self.get_password().send_keys(password)

    def click_login_button(self):
        self.get_login_button().click()

    # Methods
    def authorization(self):
        """ Авторизация """
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.input_user_name('ulanudevdv11@mail.ru')
        self.input_password('xXi8QwP2JAmciZb')
        self.click_login_button()
        self.assert_word(self.get_main_word(), 'ИДЕИ НОВОГОДНИХ ПОДАРКОВ')
