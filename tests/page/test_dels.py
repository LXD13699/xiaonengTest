import time


def Del_Page(driver):
    time.sleep(3)
    # 选择一条数据
    driver.find_element_by_xpath('//*[@id="2707"]/td[3]').click()
    # 点击删除按钮
    driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div[2]/div[1]/button[3]').click()
    # 是否确认删除
    time.sleep(2)
    driver.find_element_by_class_name("swal-button.swal-button--confirm").click()