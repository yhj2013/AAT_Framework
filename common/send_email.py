# encoding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from conf import email_config

"""
@author: yhj
@file: send_email.py
@time: 2020/7/18 8:25
@desc: 对发邮件功能的封装,这里用到的是163邮箱,如果后期需要发送附件或者图片等内容还需自己另行设置
"""


class Email:

    def __init__(self, smtp_host=email_config.SMTP_HOST, mail_user=email_config.USERNAME,
                 mail_pass=email_config.PASSWORD, smtp_port=email_config.SMTP_PORT):
        """

        :param smtp_host: 第三方smtp服务器的地址
        :param mail_user: 你的第三方邮箱名
        :param mail_pass: 你的邮箱授权码
        :param smtp_port: 第三方smtp服务器的端口(默认是25)
        for example:
        try:
            test = Email()
            content = "这就是一个小测试"
            test.send_email(content=content)
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")
        """
        # 创建smtp对象
        self.smtp = smtplib.SMTP()
        # 如果本地没有smtp服务器的话要先连接第三方的smtp服务器
        self.smtp.connect(smtp_host, smtp_port)
        # 连接上之后进行登录,登录成功才能发送邮件
        self.smtp.login(mail_user, mail_pass)

    def __del__(self):
        """

        退出服务
        :return:
        """
        self.smtp.quit()

    def send_email(self, subject=email_config.SUBJECT, email_from=email_config.EMAIL_FROM,
                   email_to=email_config.EMAIL_TO, content=""):
        """

        :param subject: 邮件标题
        :param email_from: 谁发的
        :param email_to: 发给谁
        :param content: 邮件正文内容
        :return:
        """
        self.email_content = MIMEText(content, 'plain', 'utf-8')
        self.email_content['Subject'] = Header(subject, 'utf-8')
        self.email_content['From'] = email_from
        self.email_content['To'] = email_to
        self.smtp.sendmail(email_from, email_to, self.email_content.as_string())

