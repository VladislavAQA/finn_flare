import datetime

from selenium.webdriver.common.action_chains import ActionChains


class Base:
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        """ Method get current url """
        get_url = self.driver.current_url
        print('Current url: ' + get_url)

    @staticmethod
    def assert_word(word, result):
        """ Method assert word """
        value_word = word.text
        print(word.text)
        assert value_word == result
        print('Good value: ' + value_word)

    def get_screenshot(self):
        """ Method get screenshots """
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot("D:\\PyDoc\\finn_flare\\screen\\" + name_screenshot)

    def assert_url(self, result):
        """ Method assert url """
        get_url = self.driver.current_url
        assert get_url == result
        print('Good value url: ' + get_url)

    def action_method(self, method):
        """ Method action """
        action = ActionChains(self.driver)
        action.click_and_hold(method).move_by_offset(-95, 0).release().perform()
