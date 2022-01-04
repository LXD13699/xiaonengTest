import time
class fenLei:
    def Fenlei_Page(driver):
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div/aside/div/nav/ul/li[7]/a/i').click()
        #点击新增按钮
        time.sleep(2)
        driver.find_element_by_class_name("btn.btn-info").click()
        #输入标题
        driver.find_element_by_id("categoryName").send_keys("哈哈哈12312")
        #选择图标
        driver.find_element_by_xpath('//*[@id="categoryForm"]/div[3]/ul/li[2]/div/img').click()
        #点击确认按钮
        driver.find_element_by_class_name("btn.btn-primary").click()
        time.sleep(2)
        driver.find_element_by_class_name("swal-button.swal-button--confirm").click()