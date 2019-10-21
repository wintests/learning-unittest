import xlrd
from config.settings import EXCEL_PATH

class ExcelUtil():

    def __init__(self, excel_path = EXCEL_PATH, sheet_name = "Sheet1"):
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheet_by_name(sheet_name)
        self.key = self.table.row_values(0)  # 读取第一行数据, 取第一行作为Key值
        self.rowNum = self.table.nrows  # 获取总行数
        self.colNum = self.table.ncols  # 获取总列数

    def read_excel(self):
        dict_data = []
        for row in range(1, self.rowNum):
            tt = {}
            row_data = self.table.row_values(row)
            for col in range(len(self.key)):
                tt[self.key[col]] = row_data[col]
            dict_data.append(tt)
        return dict_data

excelUtil = ExcelUtil()

if __name__ == '__main__':
    dict_data = excelUtil.read_excel()
    for row_data in dict_data:
        print(row_data)
