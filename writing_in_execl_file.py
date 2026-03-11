import openpyxl

path ="E:\companies.xlsx"
#file-> workbook -> sheets -> excels
workbook = openpyxl.load_workbook(path)
sheet =workbook.active

for r in range(1,6):
    for c in range(1,4):
        sheet.cell(r,c).value='welcome'

workbook.save(path)