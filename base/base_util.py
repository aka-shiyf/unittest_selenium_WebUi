import time
import unittest
from selenium import webdriver


class BaseUtil(unittest.TestCase):
    # 前置
    def setUp(self) -> None:
        self.dr = webdriver.Firefox()
        self.dr.get("https://user.flashchainsign.com/#/login")

    # 后置
    def tearDown(self) -> None:
        time.sleep(5)
        self.dr.quit()
