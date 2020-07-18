# encoding: utf-8
import xlrd
from conf import excel_config
import json

"""
@author: yhj
@file: excel_operator.py
@time: 2020/7/19 00:35
@desc: 对操作excel进行封装
"""


class Excel:

    def __init__(self, file_path=excel_config.EXCEL_PATH):
        """

        :param file_path: 打开excel文件的路径(文件路径的绝对值+文件名)
        for example:
            excel = Excel()

        """
        self.book = xlrd.open_workbook(file_path, formatting_info=False)
        self.pages = self.book.sheets()

    def query_sum_pages(self):
        """

        :return: int
        """
        return len(self.pages)

    def query_page(self, index):
        """

        :param index: int,book中的第几页(0是第一页)
        :return:
        """

        return self.book.sheet_by_index(index)

    def page_rows_and_cols(self, index):
        """

        :param index: 第几个sheet
        :return: 所选sheet的所有行和列,rows是总行数, cols是总列数
        """
        self.page = self.book.sheet_by_index(index)
        rows = self.page.nrows
        cols = self.page.cols
        return rows, cols

    def all_jsons(self, index):
        """

        :param index: 想读取第几个sheet中的数据
        :return:
        for example: 获取指定excel文件中第一个sheet的所有请求参数
        for i in excel.all_jsons(0):
                print(i)
        """
        self.page = self.book.sheet_by_index(index)
        dict = {}
        sum_rows = self.page.nrows
        sum_cols = self.page.ncols
        for i in range(1, sum_rows):
            for j in range(sum_cols):
                title = self.page.cell_value(0, j)
                value = self.page.cell_value(i, j)
                dict[title] = value
            yield dict
