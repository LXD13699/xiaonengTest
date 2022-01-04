import time
def Login_Page(driver):
    #输入账号
    driver.find_element_by_id("userName").send_keys("admin")
    #输入密码
    driver.find_element_by_id("password").send_keys("xn123456")
    #点击验证码
    driver.find_element_by_class_name("pointer").click()
    time.sleep(2)
    #输入验证码
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/form/div[3]/div[1]/input').send_keys("5cwwg")
    #点击登录
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/form/div[5]/div[2]/button').click()