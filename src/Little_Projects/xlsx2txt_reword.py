import openpyxl
from datetime import date
xls_parth = r"D:\Projects\PythonProjects\Learn\words.xlsx"
txt_parth = r"D:\Projects\PythonProjects\Learn\words_" + str(date.today()) + ".txt"
wookbook = openpyxl.load_workbook(xls_parth)
worksheet = wookbook.active


def write_in_file(row_arr, file):
    text = f'\"{row_arr[0]}\";\"{row_arr[1]}\"\n'
    file.write(text)


def parse_default_words():
    with open(txt_parth, "w", encoding="UTF-8") as file:
        row_num = 3
        while True:
            row_arr = []
            for col_num in range(2, 4):
                cell = worksheet.cell(row=row_num, column=col_num).value
                if not cell:
                    return
                row_arr.append(cell)
            write_in_file(row_arr, file)
            row_num += 1


parse_default_words()
