import  time
from selenium.webdriver import ActionChains


def Add_Page(driver):
    #点击菜单
    driver.find_element_by_xpath('/html/body/div/aside/div/nav/ul/li[5]/a/i').click()
    time.sleep(3)
    #点击新增按钮
    driver.find_element_by_class_name("btn.btn-success").click()
    time.sleep(2)
    #输入标题
    driver.find_element_by_id("blogName").send_keys("测试测试")
    #输入标签
    driver.find_element_by_id("blogTags_tag").send_keys("测试测试标签")
    #输入路径
    driver.find_element_by_id("blogSubUrl").send_keys("测试123")
    time.sleep(2)
    #点击富文本
    driver.find_element_by_class_name("CodeMirror-scroll").click()
    time.sleep(2)
    #c操作键盘
    ActionChains(driver).send_keys("测试内容").perform()
    #点击保存文章
    driver.find_element_by_id("confirmButton").click()
    #选择随机封面
    driver.find_element_by_id("randomCoverImage").click()
    #点击确定
    driver.find_element_by_id("saveButton").click()
    driver.find_element_by_class_name("swal-button-container").click()
