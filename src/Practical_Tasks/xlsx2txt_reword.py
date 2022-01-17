import openpyxl
from datetime import date


def write_in_file(row_arr, file):
    text = f'\"{row_arr[0]}\";\"{row_arr[1]}\"\n'
    file.write(text)


def parse_default_xlsx_file():
    with open(parth_2_txt_file, "w", encoding="UTF-8") as file:
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


if __name__ == "__main__":
    GENERAL_PARTH = r"D:\Projects\PythonProjects\Python-rush\data\words"

    parth_2_xlsx_file = f"{GENERAL_PARTH}.xlsx"
    parth_2_txt_file = f"{GENERAL_PARTH}_{date.today()}.txt"

    wookbook = openpyxl.load_workbook(parth_2_xlsx_file)
    worksheet = wookbook.active

    parse_default_xlsx_file()
