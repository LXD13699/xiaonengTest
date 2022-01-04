from unittest import TestCase
from selenium import webdriver

from tests.page import test_fenlei, test_login
from tests.page.test_fenlei import fenLei


class FenleiCase(TestCase):
    driver = None
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver =webdriver.Chrome()
        cls.driver.implicitly_wait(10)

    def test_01login(self):
        self.driver.maximize_window()
        self.driver.get("http://xiaonengedu.com:9001/admin/login")
        test_login.Login_Page(self.driver)
    def test_02add(self):
        # test_fenlei.Fenlei_Page(self.driver)
        fenLei.Fenlei_Page(self.driver)
