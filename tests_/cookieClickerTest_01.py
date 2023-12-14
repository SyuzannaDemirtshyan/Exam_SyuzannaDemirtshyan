from pages_.gamePage import GamePage
from testData_.testData import mainPageUrl
from tests_.baseTest import BaseTest


class CookieClicker(BaseTest):

    def test_1_click_to_cookie(self):
        self.driver.get(mainPageUrl)
        gamePageObject = GamePage(self.driver)
        gamePageObject.click_to_cookie_button()

        self.assertEqual("Amazon.com. Spend less. Smile more.", self.driver.title)
