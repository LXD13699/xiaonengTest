import time
def Update_Page(driver):
    time.sleep(3)
    #选择一条数据
    driver.find_element_by_xpath('//*[@id="2123"]/td[3]').click()
    #点击修改按钮
    driver.find_element_by_class_name("btn.btn-info").click()
    time.sleep(2)
    #修改标题
    driver.find_element_by_id("blogName").send_keys("123456")
    time.sleep(3)
    #点击保存按钮
    driver.find_element_by_id("confirmButton").click()
    #点击确定
    driver.find_element_by_id("saveButton").click()
    driver.find_element_by_class_name("swal-button-container").click()
