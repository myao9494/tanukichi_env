# import lib
import pandas as pd
import numpy as np

# create data
dates = pd.date_range("20130101", freq='D', periods=6)
df = pd.DataFrame(np.random.randn(6,4),index = dates, columns = list("ABCD"))

# set data
fileName = "hoge.xlsx"
writer = pd.ExcelWriter(fileName)
df.to_excel(writer, sheet_name="hoge1")
df.T.to_excel(writer, sheet_name="hoge2")

workbook  = writer.book
worksheet1 = writer.sheets['hoge1']
worksheet2 = writer.sheets['hoge2']

# Add some cell formats.
format1 = workbook.add_format()
format1.set_font_color('red')

index = workbook.add_format({'align': 'left'})
index.set_font_color('blue')

# Set the column width and format.
worksheet1.set_column('C:C', None, index)
worksheet2.set_column('B:B', 20, format1)

# save
writer.save()


# import lib
import pandas as pd

# read xlsx file
xlsFile = "hoge.xlsx"
sheetName = "hoge1"
xls_data = pd.read_excel(xlsFile, sheetname=sheetName)
print(xls_data)



#https://github.com/python-excel/tutorial/tree/master/students
【xlwt　エクセルブックへの書き込み】
#新規でワークブックを作って保存する
# -*- coding: utf-8 -*-
from xlwt import Workbook
wb = Workbook()
ws = wb.add_sheet('Type examples')
#B2に"10"を書き込む
ws.write(1,1,"10")
wb.save('borders.xls')

【エクセル読み】
# -*- coding: utf-8 -*-
import xlrd
book = xlrd.open_workbook('株式記録.xlsx')
sheet = book.sheet_by_index(0)
cell = sheet.cell(2,2)
print(cell.value)
