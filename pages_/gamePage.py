from selenium.webdriver.common.by import By
from pages_.basePage import BasePage
from common_.utilities_.customLogger import logger


class GamePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__cookieButtonLocator = (By.ID, "bigCookie")
        self.__cookieCountLocator = (By.ID, "cookies")

    def click_to_cookie_button(self):
        cookieButtonElement = self._find_element(self.__cookieButtonLocator)
        self._click_to_element(cookieButtonElement)

    def get_cookie_count(self):
        cookieCountElement = self._find_element(self.__cookieCountLocator)
        return int(self._get_text(cookieCountElement))
