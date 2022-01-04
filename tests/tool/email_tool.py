import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import time

# 自动发送邮件
# 有的网络会拦截，切其他网络试下

class SendEmail(object):
    # 1.通过代码配置需要修改代码变量值
    # 发件人地址
    send_addr = '1156155560@qq.com'
    # 收件人地址  有多个收件人用,分隔 xxx@qq.com,qqq@qq.com
    reciver_addr = '2067663363@qq.com'
    # 发送邮箱的服务器地址 qq邮箱是'smtp.qq.com', 163邮箱是'smtp.163.com'
    mail_server = 'smtp.qq.com'
    # 发件人的邮箱及邮箱授权码
    username = '1156155560@qq.com'
    # 注意这里是邮箱的授权码而不是邮箱密码qktiet***fag
    password = 'efnthqsmkzlzgged'
    # 发送人姓名或昵称
    nickname = "刘晓栋"

    # 2. 通过文件配置  放开注释即可启用 需要修改xiaoneng.ini 文件配置
    # def __init__(self):
    #     email_config_path = path_tool.get_Base_Path() + "\\selenium_test\\unittest_demo\\config\\xiaoneng.ini"
    #     config = configparser.ConfigParser()
    #     config.read(email_config_path, encoding="utf-8")
    #     self.send_addr = config.get("email", "send_addr")
    #     self.reciver_addr = config.get("email", "reciver_addr")
    #     self.mail_server = config.get("email", "mail_server")
    #     self.username = config.get("email", "username")
    #     self.password = config.get("email", "password")
    #     self.nickname = config.get("email", "nickname")

    def send_email(self, report_path, subject_title="自动化测试报告"):
        # 读取测试报告中的内容作为邮件的内容
        # with open(new_report, 'r', encoding='utf8') as f:
        with open(report_path, 'rb') as f:
            mail_body = f.read()
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        # 邮件标题处理
        subject_title = subject_title + now

        message = MIMEMultipart('mixed')
        # 添加邮件内容
        msg_html = MIMEText(mail_body, 'html', 'utf-8')
        message.attach(msg_html)

        # 添加附件
        msg_file = MIMEText(mail_body, 'html', 'utf-8')
        # msg_file["Content-Disposition"] = 'attachment; filename="test_report.html"'
        msg_file.add_header('Content-Disposition', 'attachment', filename="test_report.html")
        message.attach(msg_file)

        # 发送人姓名
        message['From'] = self.nickname
        # 添加邮件标题
        message['Subject'] = Header(subject_title, 'utf-8').encode()

        # 发送邮件，使用的使smtp协议
        smtp = smtplib.SMTP()
        smtp.connect(self.mail_server)
        smtp.login(self.username, self.password)
        smtp.sendmail(self.send_addr, self.reciver_addr.split(','), message.as_string())
        smtp.quit()



