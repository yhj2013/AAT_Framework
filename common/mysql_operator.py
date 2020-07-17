# encoding: utf-8
import pymysql
from conf import mysql_config

"""
@author: yhj
@file: mysql_operator.py
@time: 2020/7/17 23:54
@desc: 通过对数据库pymysql库的封装,从而方便了对pymsql模块的使用
"""


class MysqlConnect(object):

    def __init__(self, host=mysql_config.HOST, user=mysql_config.USER, password=mysql_config.PASSWD,
                 database=mysql_config.DBNAME, port=mysql_config.PORT):
        """

        :param host: 想要连接的数据所在的IP地址
        :param user: 想要连接的数据库的用户名
        :param password: 想要连接的那个数据库的密码
        :param database: 想要连接的那个数据库名
        for example:
        Thunder_God = MysqlConnect('127.0.0.1', 'root', '123456', 'pythondb')
        Thunder_God.exec('insert into test(id, text) values(%s, %s)' % (1, repr('哈送到附近')))
        Thunder_God.exec_data('insert into test(id, text) values(%s, %s)' % (1, repr('哈送到附近')))
        Thunder_God.select('select * from test')
        """

        self.db = pymysql.connect(host=host, user=user, password=password,
                                  port=port, database=database, charset='utf8')
        self.cursor = self.db.cursor()

    # 将要插入的数据写成元组传入
    def exec_data(self, sql, data=None):
        self.cursor.execute(sql, data)
        self.db.commit()

    def exec(self, sql):
        """

        :param sql: 原生sql语句,sql拼接时使用repr()，将字符串原样输出
        :return:
        """
        self.cursor.execute(sql)
        self.db.commit()

    def select(self, sql):
        """

        :param sql: 原生sql语句
        :return: results
        """
        return self.cursor.execute(sql).fetchall()

    def __del__(self):
        """

        :return: None, 析构化函数
        """
        self.cursor.close()
        self.db.close()
