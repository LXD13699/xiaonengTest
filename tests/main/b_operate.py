import unittest

from tests.page import test_login, test_add, test_dels, test_update
from selenium import webdriver

class BokeCase(unittest.TestCase):
    driver = None
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
    def test_01Login(self):
        self.driver.maximize_window()
        self.driver.get("http://xiaonengedu.com:9001/admin/login")
        test_login.Login_Page(self.driver)

    def test_02Add(self):
        test_add.Add_Page(self.driver)

    def test_03Update(self):
        test_update.Update_Page(self.driver)

    def test_04Del(self):
        test_dels.Del_Page(self.driver)

if __name__ == '__main__':
    unittest.main()
