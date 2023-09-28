import openpyxl
wb = openpyxl.load_workbook('BI-Analytics master sheet April 14 2017.xlsx')
###print wb
##print wb.get_sheet_names()
sheet = wb.get_sheet_by_name('Readme')
sheet1= wb.get_sheet_by_name('Data')
##sheet['G9']='2017-04-17 15:00:00'
sheet['G9']=''
print sheet['G9'].value
##for col in sheet1.iter_cols(min_row=1, max_col=17, max_row=1162):
##        for cell in col:
##            cell=''
cell_range = sheet1['A1':'T1600']
cell_range=None
wb.save("BI-Analytics master sheet April 14 2017.xlsx")


