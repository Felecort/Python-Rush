import openpyxl

xls_parth = r"D:\Projects\PythonProjects\Learn\words.xlsx"
txt_parth = r"D:\Projects\PythonProjects\Learn\words.txt"
wookbook = openpyxl.load_workbook(xls_parth)
worksheet = wookbook.active


def write_in_file(row_arr, file):
    text = f'\"{row_arr[0]}\";\"{row_arr[1]}\"\n'
    file.write(text)


def parse_default_words(row_num):
    
    with open(txt_parth, "a", encoding="UTF-8") as file:
        while True:
            row_arr = []
            for col_num in range(2, 4):
                cell = worksheet.cell(row=row_num, column=col_num).value
                if not cell:
                    return
                row_arr.append(cell)
            write_in_file(row_arr, file)
            row_num += 1


ROW_NUM = 181
parse_default_words(ROW_NUM)
