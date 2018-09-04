# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 16:53:12 2018

@author: ying.zhang01
"""

import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import Log


class Email:
    """邮件类。

    用来给指定用户发送邮件，可指定多个收件人，可带附件。
    """

    def __init__(self, server, sender, password,
                 receiver, title, message=None, path=None):
        """初始化Email

        Attributes:
            server: smtp服务器，必填。
            sender: 发件人，必填。
            password: 发件人密码，必填。
            receiver: 收件人，传入list，必填。
            title: 邮件标题，必填。
            message: 邮件正文，非必填。
            path: 附件路径，可传入list（多附件）或str（单个附件），非必填。
        """
        # 设置smtplib所需的参数
        self.server = server
        self.sender = sender
        self.receiver = receiver
        self.password = password

        # 设置email模块所需的参数
        self.title = title
        self.message = message
        self.files = path

        self.msg = MIMEMultipart('mixed')

    def _attach_file(self, att_file):
        """将单个文件添加到邮件附件中"""
        # 构造附件
        with open(att_file, 'rb') as f:
            atta = MIMEText(f.read(), 'base64', 'utf-8')
            atta["Content-Type"] = 'application/octet-stream'
            # 附件重命名
            file_name = re.split(r'[\\|/]', att_file)
            atta["Content-Disposition"] = 'attachment; filename="%s"' % file_name[-1]
            self.msg.attach(atta)

    def send(self):
        """发送邮件"""
        # 构造邮件对象MIMEMultipart对象
        self.msg['Subject'] = self.title
        self.msg['From'] = self.sender
        self.msg['To'] = ';'.join(self.receiver)

        # 构造邮件正文html内容，同时作为附件发送
        if self.message:
            text_html = MIMEText(self.message, 'html', 'utf-8')
            self.msg.attach(text_html)

        # 添加附件，支持多个附件（传入list），或者单个附件（传入str）
        if self.files:
            if isinstance(self.files, list):
                for file in self.files:
                    self._attach_file(file)
            elif isinstance(self.files, str):
                self._attach_file(self.files)

        # smtplib模块负责发送邮件
        try:
            smtp_server = smtplib.SMTP(self.server, 25)  # SMTP协议默认端口是25
        except Exception as e:
            Log.error("发送邮件失败,无法连接到SMTP服务器，检查网络以及SMTP服务器." +
                      "异常提示：" + str(repr(e)))
        else:
            try:
                smtp_server.login(self.sender, self.password)  # 登录
            except Exception as e:
                Log.error("用户登录失败，请检查密码!异常提示：" + str(repr(e)))
            else:
                smtp_server.sendmail(self.sender,
                                     self.receiver,
                                     self.msg.as_string())  # 邮件发送
            finally:
                smtp_server.quit()  # 断开服务器连接
                Log.info('发送邮件"{0}"成功! 收件人：{1}。'
                         .format(self.title, self.receiver))
