# encoding: utf-8

import paramiko
from conf import ssh_config

"""
@author: yhj
@file: connect_ssh.py
@time: 2020/7/17 23:54
@desc: 通过对数据库pymysql库的封装,从而方便了对pymsql模块的使用
"""


class SSHConnect:

    def __init__(self, hostname=ssh_config.HOST, port=ssh_config.PORT, username=ssh_config.USER,
                 password=ssh_config.PASSWORD):
        """

        :param hostname: 想连接的主机地址
        :param port: ssh服务所监听的端口号
        :param username: 想连接的主机用户名
        :param password: 想连接的主机密码
        for example:
            ssh = SSHConnect()
            stdin, stdout, stderr = ssh.exec_command("ls")
            print(stdout)
        """
        # 建立一个sshclient对象
        self.ssh = paramiko.SSHClient()
        # 调用connect方法连接服务器
        self.ssh.connect(hostname=hostname, port=port, username=username, password=password)

    def exec_command(self, command):
        """

        :param command: 执行的
        :return: stdin: 标准输入, stdout: 标准输出, stderr: 错误输出
        """
        if isinstance(command, str):
            stdin, stdout, stderr = self.ssh.exec_command(command)
            return stdin, stdout, stderr

    def __del__(self):
        self.ssh.close()
