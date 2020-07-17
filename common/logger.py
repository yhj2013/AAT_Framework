# encoding: utf-8
import os
import time
import logging
import threading

"""
@author: yhj
@file: logger.py
@time: 2020/7/14 22:35
@desc: 通过创建单例模式的日志流方法定义日志
"""


class Logging:
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(Logging, "_instance"):
            with Logging._instance_lock:
                if not hasattr(Logging, "_instance"):
                    Logging._instance = object.__new__(cls)
        return Logging._instance

    def __init__(self, level="INFO", handler="all"):
        """

        :param level: 设置日志输出的等级,默认是INFO
        :param handler: 设置日志输出到哪里,默认是输出到文件和控制台 (ALL 模式)  此外还有"console_only"模式和"file_only"
        :param abs_file_name: 设置日志输出到文件的路径, 默认输出到当前项目下的logs目录中
        """
        self.logger = logging.getLogger("Iran_Man")
        log_fmt = "%(asctime)s - %(name)s - %(filename)s - %(levelname)s : %(message)s"
        self.handler = handler
        self.logger.setLevel(level)
        self.formatter = logging.Formatter(fmt=log_fmt, datefmt="%Y-%m-%d %H:%M:%S")
        proDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        resultPath = os.path.join(proDir, 'AAT_results')
        result_Log_Path = os.path.join(resultPath, 'logs')
        result_Html_Path = os.path.join(resultPath, 'html_report')
        Log_month_Dir = os.path.join(result_Log_Path, time.strftime("%Y-%m"))
        self.log_path = os.path.join(Log_month_Dir, time.strftime("%Y-%m-%d %H-%M-%S") + '.log')
        [os.mkdir(i) for i in [resultPath, result_Log_Path, result_Html_Path, Log_month_Dir] if not os.path.exists(i)]

    def getLogger(self):

        def console_only():
            if not self.logger.handlers:
                console = logging.StreamHandler()
                console.setFormatter(self.formatter)
                self.logger.addHandler(console)

        def file_only():
            if not self.logger.handlers:
                file = logging.FileHandler(self.log_path, encoding="utf-8")
                file.setFormatter(self.formatter)
                self.logger.addHandler(file)
                return self.logger

        def all():
            if not self.logger.handlers:
                console = logging.StreamHandler()
                file = logging.FileHandler(self.log_path, encoding="utf-8")
                console.setFormatter(self.formatter)
                file.setFormatter(self.formatter)
                self.logger.addHandler(console)
                self.logger.addHandler(file)
                return self.logger

        select_pattern = {
            "console_only": console_only,
            "file_only": file_only,
            "all": all,
        }

        return select_pattern.get(self.handler)()


Iran_Man = Logging()
Iran_Man.getLogger()
