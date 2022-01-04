import unittest
#创建测试套件
from tests.lib.HTMLTestRunner_CN import HTMLTestRunner
from tests.main.b_operate import BokeCase
from tests.main.f_operate import FenleiCase
from tests.tool.email_tool import SendEmail

suit = unittest.TestSuite()
#创建类加载器
loader = unittest.TestLoader()
boke = loader.loadTestsFromTestCase(BokeCase)
fenlei = loader.loadTestsFromTestCase(FenleiCase)

suit.addTest(boke)
suit.addTest(fenlei)
# unittest.TextTestRunner().run(suit)
xpath_report="D:\\software\\pycharmTest\CCC\\tests\\report\\report.html"
with open(xpath_report,mode="wb") as f:
    HTMLTestRunner(f).run(suit)

SendEmail().send_email(xpath_report,"自动化")